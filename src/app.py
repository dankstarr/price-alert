from flask import Flask, make_response, render_template, session, request
import src.models.users.views as Users
from src.models.alerts.views import alert_blueprint
import src.models.items.views as Items
import src.models.stores.views as Stores

from src.common.database import Database

app = Flask(__name__)
app.config.from_object('src.config')
app.secret_key = '123'

app.register_blueprint(Users.user_blueprint, url_prefix='/users')
app.register_blueprint(alert_blueprint, url_prefix='/alerts')
app.register_blueprint(Items.item_blueprint, url_prefix='/items')
app.register_blueprint(Stores.store_blueprint, url_prefix='/stores')


@app.before_first_request
def db_init():
    Database.initialize()


@app.route('/')
def home():
    return render_template('home.jinja2')


@app.route('/drive', methods=['POST', 'GET'])
def drive():
    if request.method == 'GET':
        return render_template('/drive/drivelink.jinja2')
    elif request.method == 'POST':

        lines = request.form['lines']
        if lines.count('export=downloadhttps://drive.google')>=1:
            all = lines.split('https://')
        else:
            all = lines.split('\n')
        arr = []
        all = filter(None, all)

        for i in all:
            id = i.split("id=")[1]
            id = id.split('&export=download')[0]
            arr.append("https://drive.google.com/file/d/" + id + "/view")
        print(arr)
        return render_template('/drive/converted.jinja2', lines=arr)

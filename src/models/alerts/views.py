from flask import Blueprint, render_template, session, request, redirect, url_for

from src.models.alerts.alert import Alert
from src.models.items.item import Item

alert_blueprint = Blueprint('balert', '__name__')


@alert_blueprint.route('/')
def alerts():
    alerts = Alert.get_by_email(session['email'])


    return render_template('alerts/alerts.jinja2', alerts=alerts)


@alert_blueprint.route('/new', methods=['GET','POST'])
def create_alert():
    if request.method == 'POST':
        name = request.form['name']
        url= request.form['url']
        limit = request.form['limit']
        item = Item(name, url)
        item.save_to_mongo()
        alert=Alert(session['email'], limit, item._id, True)
        alert.save_to_mongo()
        return redirect(url_for('.alert', _id=alert._id))
    return render_template('alerts/new.jinja2')


@alert_blueprint.route('/<string:_id>')
def alert(_id):

    return render_template('alerts/alert.jinja2', alert=Alert.get_by_alertid(_id))
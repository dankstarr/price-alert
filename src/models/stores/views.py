import json

from flask import Blueprint, render_template, request, redirect, url_for

from src.models.stores.store import Store

store_blueprint = Blueprint('bstore',__name__)

@store_blueprint.route('/')
def stores():
    stores = Store.all_stores()
    return render_template('stores/stores.jinja2', stores=stores)

@store_blueprint.route('/new',  methods=['GET','POST'])
def create():
    if request.method=='POST':
        name=request.form['name']
        url=request.form['url']
        tag=request.form['tag']
        query=request.form['query']
        query=query.replace("'", '"')
        query=json.loads(query)
        headers=request.form['headers']
        headers=headers.replace("'", '"')
        headers=json.loads(headers)
        store=Store(name, url, tag, query, header=headers)
        store.save_to_mongo()
        return redirect(url_for('.stores'))

    return render_template('stores/new.jinja2')


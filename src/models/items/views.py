from flask import Blueprint

item_blueprint = Blueprint('bitem', '__name__')

@item_blueprint.route('/')
def item():
    return "Kutriya"

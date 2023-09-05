from flask import Blueprint
from controllers.husband_call import get_score

husband_call_bp = Blueprint('husband_call', __name__)

@husband_call_bp.route('/<string:name>/')
def score(name):
    return get_score(name)
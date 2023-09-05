from flask import Blueprint, request
from controllers.contestants import get_contestants, add_contestant

contestants_bp = Blueprint('contestants', __name__)

@contestants_bp.route('/', methods = ['POST', 'GET'])
def contestants():
    if request.method == 'POST':
        return add_contestant(request.json)
    else: 
        return get_contestants(request.args)



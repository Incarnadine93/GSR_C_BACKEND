from flask import request, Blueprint
from ..models import User
from flask_cors import cross_origin



api = Blueprint('api', __name__, url_prefix='/api')

@api.post('/users')
def create_user():
    uid = request.json.get('uid')
    name = request.json.get('displayName')

    user = User.query.filter_by(uid=uid).first()

    if user:
        return {'status': 'ok', 'message': 'Unable to create user. User already exists', 'user': user.to_dict()}
    user = User(uid=uid, name=name)
    user.create()
    return {'status': 'ok', 'user': user.to_dict()}
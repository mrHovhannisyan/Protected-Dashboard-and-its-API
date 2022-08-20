from http import HTTPStatus

from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from marshmallow import ValidationError

from app.models import User
from app.schemas.auth import UserLoginSchema

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route("/login", methods=['POST'])
def login():
    try:
        validated_data = UserLoginSchema().load(request.json)
    except ValidationError as err:
        return {'errors': err.messages}, HTTPStatus.UNPROCESSABLE_ENTITY

    user = User.query.filter_by(email=validated_data['email']).first()

    if not user or not user.check_password(validated_data['password']):
        return {'errors': ['Invalid credentials']}, HTTPStatus.FORBIDDEN

    access_token = create_access_token(identity=str(user.id))

    return {'access_token': access_token}, HTTPStatus.OK

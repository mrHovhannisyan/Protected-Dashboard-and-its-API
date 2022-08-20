from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models import Score
from app.schemas.score import ScoreResponseSchema

bp = Blueprint('score', __name__, url_prefix='/score')


@bp.route("/my")
@jwt_required()
def get_user_score():
    user_id = get_jwt_identity()
    score = Score.query.filter_by(user_id=user_id).first()

    return {"data": ScoreResponseSchema().dump(score)}

from flask import Blueprint
from flask_cors import CORS
from flask_restful import Api

gempaBp = Blueprint("Gempa", __name__)
CORS(gempaBp)

api_gempa = Api(gempaBp)

from app.gempa import api
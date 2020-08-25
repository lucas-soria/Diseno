from flask import Blueprint
from flask_restful import Api
from resources.Welcome import Welcome
from resources.Persona import PersonaResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(Welcome, '/Welcome')
api.add_resource(PersonaResource, '/Persona')

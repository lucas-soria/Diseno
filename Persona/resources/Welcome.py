from flask_restful import Resource


class Welcome(Resource):
    def get(self):
        return "Bienvenido a la API de Diseno de Sistemas"

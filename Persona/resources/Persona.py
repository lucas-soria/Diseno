from flask import request
from flask_restful import Resource
from Model import db, Persona, PersonaSchema

personas_schema = PersonaSchema(many=True)
persona_schema = PersonaSchema()


class PersonaResource(Resource):
    def get(self):
        personas = Persona.query.all()
        personas = personas_schema.dump(personas).data
        return {'status': 'success', 'data': personas}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = persona_schema.load(json_data)
        if errors:
            return errors, 422
        persona = Persona.query.filter_by(id=data['id']).first()
        if persona:
            return {'message': 'Person already exists'}, 400
        persona = Persona(id=json_data['id'],
                          name=json_data['name'],
                          surname=json_data['surname'],
                          age=json_data['age'])
        db.session.add(persona)
        db.session.commit()
        result = persona_schema.dump(persona).data
        return {"status": 'success', 'data': result}, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = persona_schema.load(json_data)
        if errors:
            return errors, 422
        persona = Persona.query.filter_by(id=data['id']).first()
        if not persona:
            return {'message': 'Person does not exist'}, 400
        persona.name = data['name']
        persona.surname = data['surname']
        persona.age = data['age']
        db.session.commit()
        result = persona_schema.dump(persona).data
        return {"status": 'success', 'data': result}, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = persona_schema.load(json_data)
        if errors:
            print(errors)
            return errors, 422
        persona = Persona.query.filter_by(id=data['id']).delete()
        db.session.commit()
        result = persona_schema.dump(persona).data
        return {"status": 'success', 'data': result}, 204

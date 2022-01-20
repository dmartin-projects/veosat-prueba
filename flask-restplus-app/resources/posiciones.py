from flask import request
from flask_restplus import Resource, fields, Namespace

from models.posiciones import PosicionesModel
from schemas.posiciones import Posicioneschema

POSICION_NOT_FOUND = "Posicion no encontrada."


posicion_ns = Namespace('posicion', description='Operaciones que puedes realizar con POSICION')
posiciones_ns = Namespace('posiciones', description='Operaciones que puedes realizar con POSICIONES')

posicion_schema = Posicioneschema()
posiciones_list_schema = Posicioneschema(many=True)


posicion = posiciones_ns.model('Posicion', {
    'latitud': fields.Float,
    'longitud': fields.Float,
    'velocidad': fields.Float,
    'id_vehiculo': fields.Integer,

})


class Posicion(Resource):

    def get(self, id):
        posicion_data = PosicionesModel.find_by_id(id)
        if posicion_data:
            return posicion_schema.dump(posicion_data)
        return {'message': POSICION_NOT_FOUND}, 404

    def delete(self,id):
        posicion_data = PosicionesModel.find_by_id(id)
        if posicion_data:
            posicion_data.delete_from_db()
            return {'message': "Posicion borrada con exito"}, 200
        return {'message': POSICION_NOT_FOUND}, 404

    @posicion_ns.expect(posicion)
    def put(self, id):
        posicion_data = PosicionesModel.find_by_id(id)
        posicion_json = request.get_json();

        if posicion_data:
            posicion_data.latitud = posicion_json['latitud']
            posicion_data.longitud = posicion_json['longitud']
            posicion_data.velocidad = posicion_json['velocidad']
        else:
            return {'message': POSICION_NOT_FOUND}, 404

        posicion_data.save_to_db()
        return posicion_schema.dump(posicion_data), 200


class PosicionList(Resource):
    @posiciones_ns.doc('Todas las posiciones')
    def get(self):
        return posiciones_list_schema.dump(PosicionesModel.find_all()), 200

    @posiciones_ns.expect(posicion)
    @posiciones_ns.doc('Crear una Posicion')
    def post(self):
        posicion_json = request.get_json()
        posicion_data = posicion_schema.load(posicion_json)
        posicion_data.save_to_db()

        return posicion_schema.dump(posicion_data), 201
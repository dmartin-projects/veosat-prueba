from flask import request
from flask_restplus import Resource, fields, Namespace

from models.vehiculos import VehiculosModel
from schemas.vehiculos import Vehiculoschema

VEHICULO_NOT_FOUND = "Vehiculo no encontrado."
Vehiculo_ALREADY_EXISTS = "Vehiculo '{}' ya existe"

vehiculo_ns = Namespace('vehiculo', description='Operaciones que puedes realizar con VEHICULO')
vehiculos_ns = Namespace('vehiculos', description='Operaciones que puedes realizar con VEHICULOS')

vehiculo_schema = Vehiculoschema()
vehiculo_list_schema = Vehiculoschema(many=True)


vehiculo = vehiculos_ns.model('Vehiculo', {
    'matricula': fields.String('Matricula del vehiculo'),
    'id_estado': fields.Integer
})


class VehiculoListByIdEstado(Resource):
    @vehiculos_ns.doc('obtiene todos los vehiculos con el mismo estado')
    def get(self, id_estado):
        vehiculo_data = VehiculosModel.find_by_id_estado(id_estado)
        
        if vehiculo_data:
            return vehiculo_list_schema.dump(vehiculo_data)
        return {'message': VEHICULO_NOT_FOUND}, 404


class Vehiculo(Resource):
    def get(self, id):
        vehiculo_data = VehiculosModel.find_by_id(id)
        if vehiculo_data:
            return vehiculo_schema.dump(vehiculo_data)
        return {'message': VEHICULO_NOT_FOUND}, 404


    def delete(self, id):
        vehiculo_data = VehiculosModel.find_by_id(id)
        if vehiculo_data:
            vehiculo_data.delete_from_db()
            return {'message': "vehiculo borrado con exito"}, 200
        return {'message': VEHICULO_NOT_FOUND}, 404

    @vehiculo_ns.expect(vehiculo)
    def put(self, id):
        vehiculo_data = VehiculosModel.find_by_id(id)
        vehiculon_json = request.get_json();

        if vehiculo_data:
            vehiculo_data.matricula = vehiculon_json['matricula']
            vehiculo_data.id_estado = vehiculon_json['id_estado']
            
        else:
            return {'message': VEHICULO_NOT_FOUND}, 404

        vehiculo_data.save_to_db()
        return vehiculo_schema.dump(vehiculo_data), 200



class VehiculoList(Resource):
    @vehiculos_ns.doc('obtener todos los vehiculos')
    def get(self):
        return vehiculo_list_schema.dump(VehiculosModel.find_all()), 200

    @vehiculos_ns.expect(vehiculo)
    @vehiculos_ns.doc('Crear un vehiculo')
    def post(self):
        vehiculo_json = request.get_json()
        matricula = vehiculo_json['matricula']
        id_estado = vehiculo_json['id_estado']

        if VehiculosModel.find_by_id_matricula(matricula):
            return {'message': Vehiculo_ALREADY_EXISTS.format(matricula)}, 400

        vahiculo_data = vehiculo_schema.load(vehiculo_json)
        vahiculo_data.save_to_db()

        return vehiculo_schema.dump(vahiculo_data), 201
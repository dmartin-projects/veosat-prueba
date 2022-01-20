from flask import Flask, Blueprint, jsonify
from flask_restplus import Api
from ma import ma
from db import db
from connection_db import host,user,passwd,database

from resources.vehiculos import Vehiculo, VehiculoList, VehiculoListByIdEstado ,vehiculo_ns, vehiculos_ns
from resources.posiciones import Posicion, PosicionList, posicion_ns, posiciones_ns

from marshmallow import ValidationError

app = Flask(__name__)
bluePrint = Blueprint('api', __name__, url_prefix='/api')
api = Api(bluePrint, doc='/doc', title='Flask-RestPlus Microservice - VEOSAT PRUEBA TECNICA de David Martin Vergues ')
app.register_blueprint(bluePrint)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{passwd}@{host}/{database}' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

api.add_namespace(vehiculo_ns)
api.add_namespace(vehiculos_ns)
api.add_namespace(posicion_ns)
api.add_namespace(posiciones_ns)


@app.before_first_request
def create_tables():
    db.create_all()


@api.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400


vehiculo_ns.add_resource(Vehiculo, '/<int:id>')
vehiculo_ns.add_resource(VehiculoListByIdEstado, '/id_estado/<int:id_estado>')
vehiculos_ns.add_resource(VehiculoList, "")
posicion_ns.add_resource(Posicion, '/<int:id>')
posiciones_ns.add_resource(PosicionList, "")

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000, debug=True)
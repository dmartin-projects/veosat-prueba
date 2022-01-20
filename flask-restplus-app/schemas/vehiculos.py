from ma import ma
from models.vehiculos import VehiculosModel
from models.posiciones import PosicionesModel
from schemas.posiciones import Posicioneschema


class Vehiculoschema(ma.SQLAlchemyAutoSchema):

    posiciones = ma.Nested(Posicioneschema, many=True)

    class Meta:
        model = VehiculosModel
        load_instance = True
        include_fk= True
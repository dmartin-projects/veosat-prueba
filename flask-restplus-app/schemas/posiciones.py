from ma import ma
from models.vehiculos import VehiculosModel
from models.posiciones import PosicionesModel


class Posicioneschema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PosicionesModel
        load_instance = True
        load_only = ("vehiculo",)
        include_fk= True
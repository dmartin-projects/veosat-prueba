from db import db
from typing import List

class PosicionesModel(db.Model):

    __tablename__ = 'POSICIONES'

    id          = db.Column(db.Integer, primary_key=True)
    latitud     = db.Column(db.Float, nullable=False)
    longitud    = db.Column(db.Float, nullable=False)
    velocidad   = db.Column(db.Float, nullable=False)

    id_vehiculo = db.Column(db.Integer,db.ForeignKey('VEHICULOS.id',ondelete="CASCADE"),nullable=False)
    vehiculo    = db.relationship("VehiculosModel",back_populates="posiciones")

    def __init__(self, latitud, longitud,velocidad,id_vehiculo):
        self.latitud     = latitud
        self.longitud    = longitud
        self.velocidad   = velocidad
        self.id_vehiculo = id_vehiculo
    
    def __repr__(self):
        return f'PosicionesModel(latitud={self.latitud}, longitud={self.longitud},velocidad={self.velocidad},id_vehiculo={self.id_vehiculo} )'

    # def json(self):
    #     return {'latitud': self.latitud, 
    #             'longitud': self.longitud,
    #             'velocidad': self.velocidad,
    #             'id_vehiculo': self.id_vehiculo
                
    #             }

    @classmethod
    def find_by_id(cls, _id) -> "PosicionesModel":
        return cls.query.filter_by(id=_id).first()
    
    @classmethod
    def find_all(cls) -> List["PosicionesModel"]:
        return cls.query.all()
    
    def save_to_db(self) -> None:
        
       db.session.add(self)
       db.session.commit()

    def delete_from_db(self) -> None:
       db.session.delete(self)
       db.session.commit()
    









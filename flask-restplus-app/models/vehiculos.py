from db import db
from typing import List

class VehiculosModel(db.Model):

    __tablename__ = 'VEHICULOS'

    id          = db.Column(db.Integer, primary_key=True)
    matricula   = db.Column(db.String(10), nullable=False)
    id_estado   = db.Column(db.Integer, nullable=False)

    posiciones  = db.relationship("PosicionesModel",back_populates="vehiculo",cascade="all, delete", lazy="dynamic",primaryjoin="VehiculosModel.id == PosicionesModel.id_vehiculo")

    def __init__(self, matricula, id_estado):
        self.matricula     = matricula
        self.id_estado    = id_estado
    
    def __repr__(self):
        return f'VehiculosModel(matricula={self.matricula}, id_estado={self.id_estado})'

    def json(self):
        return {'matricula': self.matricula, 
                'id_estado': self.id_estado
                
               }

    @classmethod
    def find_by_id(cls, _id) -> "VehiculosModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_id_estado(cls, id_estado) -> "VehiculosModel":
        return cls.query.filter_by(id_estado=id_estado)

    @classmethod
    def find_by_id_matricula(cls, matricula) -> "VehiculosModel":
        return cls.query.filter_by(matricula=matricula).first()
    
    @classmethod
    def find_all(cls) -> List["VehiculosModel"]:
        return cls.query.all()
    
    def save_to_db(self) -> None:
       db.session.add(self)
       db.session.commit()

    def delete_from_db(self) -> None:
       db.session.delete(self)
       db.session.commit()
    









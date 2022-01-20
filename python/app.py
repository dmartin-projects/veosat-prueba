from connection import cursor,db


# 2.- hacer un aplicativo que seleccione las posiciones de los vehículos i actualice el estado a 1 solo de los vehículos con la velocidad superior a 10.

def update_id_estado(cursor):
    cursor.execute('select * from POSICIONES')
    posiciones = cursor.fetchall()
    
    vehiculos_to_update = [ posicion[4] for posicion in posiciones if posicion[3]>10]

    vehiculos_to_update_str = ''

    for (i,v) in enumerate(vehiculos_to_update):
        if i<len(vehiculos_to_update)-1:
            vehiculos_to_update_str+=f'{v},'
        else:
            vehiculos_to_update_str+=f'{v}'
    
    query = f'UPDATE VEHICULOS SET id_estado=1 WHERE id IN ({vehiculos_to_update_str})'

    cursor.execute(query)
    db.commit()


# Guardar los valores en un diccionario (este paso es sólo para ver conocimientos)

def save_data_in_dict(cursor):
    cursor.execute("select v.id id_vehiculo, matricula, id_estado estado, p.id id_posicion, latitud, longitud, velocidad   from VEHICULOS v right join POSICIONES p on v.id=p.id_vehiculo;")
    records = cursor.fetchall()
    
    data = []
    columnNames = [column[0] for column in cursor.description]
    for item in records:
        data.append( dict(zip( columnNames , item ) ) )
    return data
   

if __name__ == '__main__':
    update_id_estado(cursor)
    print(save_data_in_dict(cursor))

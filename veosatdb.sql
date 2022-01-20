CREATE DATABASE veosatdb;

use veosatdb;


CREATE TABLE VEHICULOS(
id int NOT NULL AUTO_INCREMENT,
matricula varchar(10) NOT NULL,
id_estado TINYINT,
PRIMARY KEY (id)
);


CREATE TABLE POSICIONES(

id int NOT NULL AUTO_INCREMENT,
latitud FLOAT NOT NULL,
longitud FLOAT NOT NULL,
velocidad FLOAT NOT NULL,
id_vehiculo int,
PRIMARY KEY(id),
CONSTRAINT
FOREIGN KEY (id_vehiculo) REFERENCES VEHICULOS(id) ON DELETE CASCADE

);

delimiter //
CREATE TRIGGER actualizarEstadoVehiculo
AFTER INSERT ON POSICIONES
FOR EACH ROW 
BEGIN
	IF NEW.velocidad>10
   		THEN
   			UPDATE VEHICULOS SET id_estado = 1 WHERE id=NEW.id_vehiculo;
   	ELSE
   		UPDATE VEHICULOS SET id_estado = 0 WHERE id=NEW.id_vehiculo;
	END IF;
END;//
delimiter ;

INSERT INTO VEHICULOS (id, matricula,id_estado) values(1001,'1234BCN',0);
INSERT INTO VEHICULOS (id, matricula,id_estado) values(1002,'2468BCN',0);
INSERT INTO VEHICULOS (id, matricula,id_estado) values(1003,'4826BCN',0);
INSERT INTO VEHICULOS (id, matricula,id_estado) values(1004,'8642BCN',0);
INSERT INTO VEHICULOS (id, matricula,id_estado) values(1005,'6284BCN',0);
INSERT INTO VEHICULOS (id, matricula,id_estado) values(1006,'8643BCN',0);
INSERT INTO VEHICULOS (id, matricula,id_estado) values(1007,'2826BCN',0);

INSERT INTO POSICIONES (id, latitud,longitud,velocidad,id_vehiculo) values(2001,'38.904','-74.006',90.5,1001);
INSERT INTO POSICIONES (id, latitud,longitud,velocidad,id_vehiculo) values(2002,'55.554','14.006',70.5,1001);
INSERT INTO POSICIONES (id, latitud,longitud,velocidad,id_vehiculo) values(2003,'-44.69','54.006',0,1001);
INSERT INTO POSICIONES (id, latitud,longitud,velocidad,id_vehiculo) values(2004,'32.996','-24.006',0,1002);
INSERT INTO POSICIONES (id, latitud,longitud,velocidad,id_vehiculo) values(2005,'12.001','14.006',63,1003);
INSERT INTO POSICIONES (id, latitud,longitud,velocidad,id_vehiculo) values(2006,'6.123','34.006',19.5,1004);
INSERT INTO POSICIONES (id, latitud,longitud,velocidad,id_vehiculo) values(2007,'88.123','94.006',60.5,1005);
INSERT INTO POSICIONES (id, latitud,longitud,velocidad,id_vehiculo) values(2008,'87.123','4.006',66.5,1006);
INSERT INTO POSICIONES (id, latitud,longitud,velocidad,id_vehiculo) values(2009,'87.123','4.006',0,1007);



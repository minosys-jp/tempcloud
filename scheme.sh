#!/bin/sh
cat >/tmp/scheme.db <<EOF
-- SENSOR TYPE
-- type=1: temperature only 2:humidity only 3:temperature/humidity
create table SENSOR_TYPE (id int primary key, type int, name varchar(40), description varchar(255));
insert into SENSOR_TYPE (id, type, name, description) values (1, 3, "sht11", "Parallax SHT11 Temperature/Humudity sensor");
insert into SENSOR_TYPE (id, type, name, description) values (2, 1, "max31855", "adafruit MAX13855 based K-thurmocouple amplifier");
insert into SENSOR_TYPE (id, type, name, description) values (3, 3, "am2302", "AM2302 Temperature/Humidity sensor (0.1 degree)");

-- ROOM
create table ROOM (id int primary key, name varchar(40), description varchar(255));
insert into ROOM (id, name, description) values (60, "Dining Room", "");
insert into ROOM (id, name, description) values (61, "Aquarium", "");

-- DATA SUMMARY
create table SUMMARY (id int primary key, tablename varchar(40), name varchar(80), description varchar(255), room int, sensor_type int, foreign key(room) references ROOM(id), foreign key(sensor_type) references SENSOR_TYPE(id));
insert into SUMMARY (id, tablename, name, description, room, sensor_type) values (1, "DATA1", "Dining Room temperature/humidity", "", 60, 1);
insert into SUMMARY (id, tablename, name, description, room, sensor_type) values (2, "DATA2", "Aquirium water temperature", "", 61, 2);

-- DATA1 (Room temperature/humidity)
create table DATA1 (elapsed int(64) primary key, datetime varchar(40), status int, temperature int, humidity int);

-- DATA2 (Aquarium temperature)
create table DATA2 (elapsed int(64) primary key, datetime varchar(40), status int, temperature int, humidity int);
EOF

sqlite3 Temperatures.db </tmp/scheme.db
rm /tmp/scheme.db

#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3

con = sqlite3.connect("Temperatures.db");

c = con.execute("select * from ROOM");
for row in c:
	print row[0], row[1], row[2]

con.close()

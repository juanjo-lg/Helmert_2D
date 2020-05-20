# -*- coding: utf-8 -*-
"""
Created on Tue May 21 08:46:04 2019

@author: Usuario1
"""

import sqlite3 as sql
from sqlite3 import Error

global conn

def create_connection(database):
    # Creates a db file.
    try:
        connection = sql.connect(database)
        print("Conexión creada con " + "SQlite" + sql.version)
        return connection
    except Error as e:
        print("Error al crear la conexión")
        print(e)

def create_table(conn):
    # Creates a table.

    sql_table = """CREATE TABLE IF NOT EXISTS puntos (
                    id integer PRIMARY KEY,
                    X REAL NOT NULL,
                    Y REAL NOT NULL,
                    Z REAL NOT NULL,
                    cod TEXT,
                    n TEXT
                    ); """
    try:
        c = conn.cursor()
        c.execute(sql_table)
        c.close() # Si se cierra la conexión, despues hay que volverla a abrir.
        conn.close()
    except Error as e:
        print("Error al crear la tabla")
        print(e)

def create_point(point, conn):
    # Creates a point into db.
    sql_into = """INSERT INTO puntos("X","Y","Z","cod","n") VALUES(?,?,?,?,?)"""

    try:
        c = conn.cursor()
        c.execute(sql_into, (point.x, point.y, point.z, point.cod, point.n))
        conn.commit()
        c.close()
    except Error as e:
        print("Error al insertar datos")
        c.close()
        print(e)

class Point:
    # Point3D class.
    def __init__(self, x, y, z=0,**kwargs):
        try:
            self.x, self.y, self.z = float(x), float(y), float(z)
        except:
            raise TypeError("Los datos introducidos no son correctos.")

        if "cod" in kwargs:
            self.cod = kwargs["cod"]
        else:
            self.cod = ""
        if "n" in kwargs:
            self.n = kwargs["n"]
        else:
            self.n = ""
        try:
            create_point(self, conn)
        except Error as e:
            print("Error al crear puntos.")
            print(e)

def main():
    # Función que ejecuta el script completo.


    db_file = ("puntos.db")

    # conn as global.
    global conn

    conn = create_connection(db_file)

    if conn is not None:
        create_table(conn)
    else:
        print("No es posible crear la conexión")

    conn = create_connection(db_file)

    p1 = Point(100,100,200, cod = "hola")
    p2 = Point(200,500,1000)

if __name__ == '__main__':
    main()

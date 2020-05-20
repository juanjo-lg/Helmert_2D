# -*- coding: utf-8 -*-

"""CALCULO DE PARAMETROS DE TRANSFORMACION ENTRE DOS SISTEMAS CONOCIDAS LAS
COORDENADAS DE DOS O MAS PUNTOS (HELMERT 2D)"""

import numpy as np
import os

# Apertura archivo de puntos en coord absolutas.
def abs_points(file_name_abs):
    # Lista donde se guardan los puntos.
    lst_abs_pnt = []

    # Abriendo fichero de bases separado por comas y añadiendo los puntos.
    with open(file_name_abs) as raw:

        for line in raw:
            # Punto en un diccionario
            #pnt = {}
            # Extrayendo cada punto en cada línea, coord separadas por coma.
            line = line.split(",")
            # Creando puntos como diccionario.
            pnt = line[0],line[1],line[2]
            # Lista de puntos.
            lst_abs_pnt.append(pnt)
    return(lst_abs_pnt)

# Apertura de archivo de puntos en SCL.
def scl_points(file_name_scl):
    # Lista donde se guardan los puntos.
    lst_scl_pnt = []

    # Abriendo fichero de bases separado por comas y añadiendo los puntos.
    with open(file_name_scl) as raw:

        for line in raw:
            # Punto en un diccionario
            # pnt = {}
            # Extrayendo cada punto en cada línea, coord separadas por coma.
            line = line.split(",")
            # Creando puntos como diccionario.
            pnt = line[0],line[1],line[2]
            # Lista de puntos.
            lst_scl_pnt.append(pnt)
        return(lst_scl_pnt)



def main():

    lst_abs = abs_points()
    lst_scl = scl_points()

    # Se cogen los puntos que son comunes en los dos ficheros.
    """Hay que probar con ficheros que no tengan todos los puntos iguales."""
    lst_pnt_numbers = []
    for i in lst_abs:
        for k in lst_scl:
            if i[0] == k[0]:
                lst_pnt_numbers.append(i[0])

    # Creación de listas con todas las "x" y las "y" de todos los puntos
    lst_x_abs = []
    lst_y_abs = []

    lst_x_scl = []
    lst_y_scl = []

    """Esto no sirve cuando los ficheros tienen diferente número de puntos."""
    for i in lst_abs:
        lst_x_abs.append(float(i[1]))
        lst_y_abs.append(float(i[2]))
    for i in lst_scl:
        lst_x_scl.append(float(i[1]))
        lst_y_scl.append(float(i[2]))

    # Cálculo del las X absolutas del centroide.
    cent_x_abs = np.average(lst_x_abs)
    cent_y_abs = np.average(lst_y_abs)

    cent_x_scl = np.average(lst_x_scl)
    cent_y_scl = np.average(lst_y_scl)

    # Origen del centroide.
    orig_cent_abs = []
    orig_cent_scl = []
    cnt = -1
    for i in lst_pnt_numbers:
        cnt += 1
        orig_cent_abs.append((lst_x_abs[cnt]-cent_x_abs
            ,lst_y_abs[cnt]-cent_y_abs))
        orig_cent_scl.append((lst_x_scl[cnt]-cent_x_scl
            ,lst_y_scl[cnt]-cent_y_scl))

    """print(orig_cent_abs)
    print("\n")
    print(orig_cent_scl)"""

    # Listado de listas para ecuaciones I, II y III
    lst_I = []
    lst_II = []
    lst_III = []

    # Cálculo de ecuación I: x'*X'+y'*Y'
    # Cálculo de ecuación II: x'*Y'-y'*X'
    # Cálculo de ecuación III: (x'**2)+(y'**2)

    cnt = -1
    for i in orig_cent_scl:
        cnt += 1
        lst_I.append(orig_cent_scl[cnt][0]*orig_cent_abs[cnt][0]
            +orig_cent_scl[cnt][1]*orig_cent_abs[cnt][1])
        lst_II.append(orig_cent_scl[cnt][0]*orig_cent_abs[cnt][1]
            -orig_cent_scl[cnt][1]*orig_cent_abs[cnt][0])
        lst_III.append((orig_cent_scl[cnt][0])**2+(orig_cent_scl[cnt][1])**2)

    sum_lst_I = np.sum(lst_I)
    sum_lst_II = np.sum(lst_II)
    sum_lst_III = np.sum(lst_III)

    # Cálculo de parámetros "a" y "b". a = I/III, b = II/III

    a = sum_lst_I/sum_lst_III
    b = sum_lst_II/sum_lst_III

    # Cálculo de Tx y Ty.
    # Tx = (SUM(X)-SUM(ax)+SUM(by))/n; Ty = (SUM(Y)-SUM(bx)-SUM(ay))/n
    # Cambio listas por array para poder multiplicar los elementos por un número.

    tx = (np.sum(lst_x_abs)-np.sum(a*np.array(lst_x_scl))
        +np.sum(b*np.array(lst_y_scl)))/len(lst_x_abs)
    ty = (np.sum(lst_y_abs)-np.sum(b*np.array(lst_x_scl))
        -np.sum(a*np.array(lst_y_scl)))/len(lst_y_abs)

    # Cálculo del ángulo de giro. tg(alpha) = b/a
    # Cálculo de la escala. mu = b/sen(alpha)

    alpha = np.arctan2(b,a)*200/np.pi
    mu = b/np.sin(alpha*np.pi/200)

    # Escritura de los distintos parámetros en un fichero ".txt"
    # os.linesep es lo mismo que "\n"

    file = open(file_name_param, "w")
    file.write("Parámetros de transformación para sistema Helmert 2D."+os.linesep)
    file.write("a: %.15f\n" % a)    # Se escribe el número con 15 decimales.
    file.write("b: %.15f\n" % b)
    file.write("Tx: %.15f\n" % tx)
    file.write("Ty: %.15f\n" % ty)
    file.write("Alpha: %.15f\n" % alpha)
    file.write("mu: %.4f" % mu)
    file.close()

if __name__ == "__main__":
    main()

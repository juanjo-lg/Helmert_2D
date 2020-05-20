# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 14:53:57 2018

@author: juanj
"""

"""MATRIZ DE ROTACIÓN EN TORNO AL EJE Z (en sentido horario)"""

import numpy as np

punto = (30,10) # Par de coordenadas de un punto en el sistema original.
angulo_decimal = 100

#print('el ángulo en radianes es:', angulo_radianes/np.pi)

class Rotacion2D():
    """ Clase que calcula las coordenadas de un punto situado en un sistema
        original en otro girado.
        Los parámetros a introducir son:

        1. - Coordenada X del punto original.
        2. - Coordenada Y del punto original.
        3. - Ángulo de giro del nuevo sistema respecto al original.

        La rotación se lleva a cabo en sentido antihorario."""
    def __init__(self, x, y, angulo_decimal):
        self.x = x
        self.y = y
        self.incognitas = {'x_':'', 'y_':''}
        matriz_punto = np.array([[x],[y]])
        ang_rad = angulo_decimal * np.pi / 200  # Paso de ángulo a radianes.
        matriz_x_y = np.matrix([[np.cos(ang_rad),-(np.sin(ang_rad))],
                                 [np.sin(ang_rad), np.cos(ang_rad)]])
        matri_incog = matriz_x_y * matriz_punto     # Matriz de resultados.
        self.incognitas['x_'], self.incognitas['y_'] =\
        round(float(matri_incog[0]),4), round(float(matri_incog[1]),4)

    def __str__(self):
        'Imprime las coordenadas calculadas.'
        return ('x: '+ str(self.incognitas['x_']) + '\n'
                'y: '+ str(self.incognitas['y_']))

    def SetAng(self, angulo_decimal):
        'Cambia el ángulo de rotación y recalcula las coordenadas del punto.'
        self.__init__(self.x, self.y, angulo_decimal)

"""TRASLACIÓN EN EJES X E Y"""

class Traslacion2D():
    """ Clase que calcula las coordenadas de un punto situado en un sistema
        original en otro desplazado a lo largo de los ejes XY.
        Los parámetros a introducir son:

        1. - Coordenada X del punto original.
        2. - Coordenada Y del punto original.
        3. - Traslación del eje X del nuevo sistema respecto al original.
        4. - Traslación del eje Y del nuevo sistema respecto al original."""
    def __init__(self, x, y, tx, ty):
        self.x = x
        self.y = y
        self.incognitas = {'x_':'', 'y_':''}
        matriz_punto = np.array([[x],[y]])
        matriz_tras = np.array([[tx],[ty]])
        matri_incog = matriz_punto + matriz_tras
        self.incognitas['x_'], self.incognitas['y_'] =\
        round(float(matri_incog[0]),4), round(float(matri_incog[1]),4)

    def __str__(self):
        'Imprime las coordenadas calculadas.'
        return ('x: '+ str(self.incognitas['x_']) + '\n'
                'y: '+ str(self.incognitas['y_']))

class Helmert2D():
    def __init__(self, x, y, mu, tx, ty, ang):
        "No tiene la precisión necesaria, pero las fórmulas si que están bien."
        self.x = x
        self.y = y
        self.mu = mu
        "nO SE POR QUE ESTABA PUESTO EN NEGATIVO LA TRASLACION"
        self.tx = tx
        self.ty = ty
        self.ang = ang * np.pi / 200  # Paso de ángulo a radianes.
        mat_tras = np.matrix(([self.tx],[self.ty]))
        # Matriz de rotación en el eje Z.
        mat_rot = np.matrix(([np.cos(self.ang), -(np.sin(self.ang))],
                              [np.sin(self.ang), np.cos(self.ang)]))
        print("a: ",mat_rot)
        mat_pun = np.matrix(([self.x],[self.y]))
        nuevo_punto = mat_tras + mu * mat_rot * mat_pun
        #nuevo_punto = mu*(mat_rot*mat_pun)+mat_tras
        print(nuevo_punto)
        #print(mu,"*", mat_rot, "*", mat_pun, "+", mat_tras)

"""PRUEBAS"""
#a = Rotacion2D(10,10,100)
#print(a)

#b = Traslacion2D(10,10,-10,-10)
#print(b)
"Salen cambiados los signos."
#c = Helmert2D(10,10,2,5,5,100)
"No calcula bien, volver a probar."
#d = Helmert2D(353365.817,4610700.139,1,351803.375,4609326.350,-39.0014)
#e = Rotacion2D(353365.817,4610700.139,39.0014)
#f = Rotacion2D(1510.2827,1392.1894,39.0014)
"""g = Helmert2D(353313.658,4610718.540,1,351803.3753,4609326.3506,-39.014)
h = Rotacion2D(5,3,100)
i = Traslacion2D(10,5,15,-2)
print(i)"""
j = Helmert2D(1563.5367,1407.128,1,351277.4985,4610447.9868,-39.0014)
#k = Helmert2D(353313.658,4610718.540,1,-351277.68,4610488.011,39.0094)
"""print(h)
print(g)"""
"""print(j)
a = np.cos(39.0094*np.pi/200)
print(a)"""

"""FUNCIONA!!!!!!!!!!"""

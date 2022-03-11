# Microprocesadores y Microcontroladores

"""
Integrantes:
Jose Fabio Navarro Naranjo
Adrián Dittel Retana
Jimena Murillo Vargas
Francisco Aguilera Quesada
Emiliano Alfaro Chacón
"""

# importacion de librerias
import random
import time

Result = []
def crear_arreglo(cantidad):
    """Esta funcion crea un array de X elementos random"""
    arreglo = list(range(cantidad))
    random.shuffle(arreglo)
    return arreglo


def sumatoria(arreglo, Result):
    """Esta funcion calcula la sumatoria de los elementos de un arreglo"""
    suma = 0
    for i in arreglo:
        suma = suma + i
        time.sleep(0.1)
    Result.append(suma)

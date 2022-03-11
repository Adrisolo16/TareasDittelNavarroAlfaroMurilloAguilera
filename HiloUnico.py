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
import argparse
import time
from Funciones import sumatoria, crear_arreglo
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# creacion de argumentos para los hilos

parser = argparse.ArgumentParser()
parser.add_argument('-x', type=int, help='Longitud del arreglo')
args = parser.parse_args()

while True:
    Status  = GPIO.input(14)
    if Status  == False:
        start = time.time()
        Result = []

        list0 = crear_arreglo(args.x)

        sumatoria(list0, Result)

        end = time.time()

        total_time = round((end - start), 4)

        print("Lista:", list0)
        print("Sumatoria:", Result[0])
        print("Tiempo:", total_time)
        break

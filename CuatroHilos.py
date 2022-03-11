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
import threading
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

        # main 4 hilos

        start = time.time()

        list = crear_arreglo(args.x)

        list1 = []
        list2 = []
        list3 = []
        list4 = []

        Result = []

        for i in range(args.x):
            Counter = i % 4
            if Counter == 0:
                list1.append(list[i])
            elif Counter == 1:
                list2.append(list[i])
            elif Counter == 2:
                list3.append(list[i])
            elif Counter == 3:
                list4.append(list[i])

        # creacion de hilos

        hilo1 = threading.Thread(target=sumatoria, args=[list1, Result])
        hilo2 = threading.Thread(target=sumatoria, args=[list2, Result])
        hilo3 = threading.Thread(target=sumatoria, args=[list3, Result])
        hilo4 = threading.Thread(target=sumatoria, args=[list4, Result])

        # inicio del proceso de los hilos
        
        hilo1.start()
        hilo2.start()
        hilo3.start()
        hilo4.start()

        hilo1.join()
        hilo2.join()
        hilo3.join()
        hilo4.join()

        Total = sum(Result)
        
        end = time.time()

        total_time = round((end - start), 4)

        print("Lista_1:", list1)
        print("Lista_2:", list2)
        print("Lista_3:", list3)
        print("Lista_4:", list4)
        print("Sumatoria:", Total)
        print("Tiempo:", total_time)
        break

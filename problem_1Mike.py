# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:23:51 2020

@author: Lenovo
"""

#Crea un programa que dado un diccionario, regrese quien hace la accion dada,
#en este caso la accion es saltar y deberia regresar que el perro y gato lo hacen
def quien_lo_hace(accion, animales):
    lista = []
    for animal in animales:
        if accion in animales[animal]:
            lista.append(animal)
    return lista
            
        
    
s = {"perro": ["Saltar", "mover la cola", "Jugar"],
     "gato": ["Saltar", "Correr", "hacer miaw"],
     "pez": ["Nadar", "comer", "procrear"]}
print (quien_lo_hace("Saltar", s))
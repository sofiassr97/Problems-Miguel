# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:31:18 2020

@author: Lenovo
"""

#Crea un programa que dada una lista de numeros, regrese la misma lista pero
#sin los duplicados, ejemplo [1, 2, 3,3,3, 4, 4, 1] deberia regresar [1,2,3,4]
def elimina_duplicados(numeros):
    lista=[]
    for i in listaN:
        if i not in lista:
            lista.append(i)
    return lista
    
    
    
listaN = [1, 2, 3, 4, 4, 1]
print (elimina_duplicados(listaN))
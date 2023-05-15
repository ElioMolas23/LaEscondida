from principal import *
from configuracion import *
import pygame
import random
import math



def nuevaPalabra(lista):
    n=random.randint(0, len(lista)-1)
    nuevapal=lista[n]
    return nuevapal


def lectura(archivo, salida, LARGO):
    contenido = archivo.read()
    lista = contenido.split("\n")
    for j in lista:
        if len(j) == LARGO:
            salida.append(j)



def revision(palabraCorrecta, palabra, correctas, incorrectas, casi):
    if palabraCorrecta==palabra:
        return True
    else:
        for letra in range(len(palabra)):
            if palabra[letra] in palabraCorrecta:
                if palabra[letra] == palabraCorrecta[letra]:
                    correctas.append(palabra[letra])
                else:
                    casi.append(palabra[letra])
            else:
                incorrectas.append(palabra[letra])

        return False


def estaEnLista(lista, palabrasUsuario):
    for palabra in lista:
        if palabra == palabrasUsuario:
            return True
    return False








import pygame
from funcionesVACIAS import *
from pygame.locals import *
from configuracion import *

def dameLetraApretada(key,):

    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == 241:
        return("ñ")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_SLASH:
        return("-")
    elif key == K_KP_MINUS:
        return("-")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")


def dibujar(screen, listaDePalabrasUsuario, palabraUsuario, puntos, segundos,
                correctas, incorrectas, casi, palabraCorrecta):
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)


    #Linea Horizontal
    pygame.draw.line(screen, (255,255,255), (0, ALTO-70) , (ANCHO, ALTO-70), 5)

    #muestra lo que escribe el jugador
    screen.blit(defaultFont.render(palabraUsuario, 1, COLOR_FONDO), (190, 570))

    #muestra el puntaje
    screen.blit(defaultFont.render("Puntos: " + str(puntos), 1, COLOR_FONDO), (680, 10))
    #muestra los segundos y puede cambiar de color con el tiempo
    if(segundos<15):
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_FONDO)
    screen.blit(ren, (10, 10))

    #

    #muestra las palabras anteriores, las que se fueron arriesgando
    pos = 0
    for palabra in listaDePalabrasUsuario:
        x=ANCHO//3
        for let in range(len(palabra)):
            if palabra[let] in palabraCorrecta:
                if palabra[let] == palabraCorrecta[let]:
                    screen.blit(defaultFontGrande.render(palabra [let], 1, COLOR_LETRAS), (x,20 + 80 * pos))
                    x = x + TAMANNO_LETRA_GRANDE
                else:
                    screen.blit(defaultFontGrande.render(palabra[let], 1, COLOR_AZUL), (x,20 + 80 * pos))
                    x = x + TAMANNO_LETRA_GRANDE
            else:
                screen.blit(defaultFontGrande.render(palabra[let], 1, COLOR_TIEMPO_FINAL), (x,20 + 80 * pos))
                x = x + TAMANNO_LETRA_GRANDE
        pos += 1

    #muestra el abcdario
    abcdario = ["qwertyuiop", "asdfghjklñ", "zxcvbnm"]
    y=0
    for abc in abcdario:
        x = 0
        for letra in abc:

            if estaEnLista(correctas, letra):
                screen.blit(defaultFont.render(letra,1,COLOR_LETRAS), (10 + x, ALTO / 1.5+y))
                x += TAMANNO_LETRA

            elif estaEnLista(casi, letra):
                screen.blit(defaultFont.render(letra,1,COLOR_AZUL), (10 + x, ALTO / 1.5+y))
                x += TAMANNO_LETRA

            elif estaEnLista(incorrectas, letra):
                screen.blit(defaultFont.render(letra,1,COLOR_TIEMPO_FINAL), (10 + x, ALTO / 1.5+y))
                x += TAMANNO_LETRA

            else:
                screen.blit(defaultFont.render(letra,1,COLOR_FONDO), (10 + x, ALTO / 1.5+y))

                x += TAMANNO_LETRA
        y += TAMANNO_LETRA












import os, random, sys, math
import pygame
from pygame.locals import *
from configuracion import *
from extras import *
from funcionesVACIAS import *


#Funcion principal
def main():
    while True:
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()

        #Preparar la ventana
        pygame.display.set_caption("La escondida...")
        screen = pygame.display.set_mode((ANCHO, ALTO))

        #IMAGENES AGREGADAS
        images=pygame.image.load("fondoJuego.jpg").convert()#CARGA LA IMAGEN
        images=pygame.transform.scale(images, (ANCHO, ALTO))#DA LAS MEDIDAS A ESCALA DE LA VENTANA
        intro=pygame.image.load("intro.jpg").convert()
        intro=pygame.transform.scale(intro, (ANCHO, ALTO))
        imgGano=pygame.image.load("gano1.jpg").convert()
        imgGano=pygame.transform.scale(imgGano, (ANCHO, ALTO))
        imgPerdio=pygame.image.load("perdio.jpg").convert()
        imgPerdio=pygame.transform.scale(imgPerdio, (ANCHO, ALTO))



        #musica de fondo
        pygame.mixer.init()
        pygame.mixer.music.load('audio.mp3')
        pygame.mixer.music.play(-1) #parametro -1 para que este en un bucle infinito y repita la canción

        # tiempo total del juego
        gameClock = pygame.time.Clock()
        fps = FPS_inicial

        puntos =  0
        palabraUsuario = ""
        listaPalabrasDiccionario = []
        ListaDePalabrasUsuario = []
        correctas = []
        incorrectas = []
        casi = []
        gano = False
        intentos = 5

        # VARIABLES AGREGADAS
        palabraCorrecta = ""
        estaEnIntro = True
        textContinuar = pygame.font.SysFont('console', 20, True)
        textResultado = pygame.font.SysFont('console', 50, True)

        # lectura del lemario
        archivo = open("lemario.txt", "r")
        lectura(archivo, listaPalabrasDiccionario, LARGO)


        while estaEnIntro:

            #CONTROL DE VELOCIDAD DEL JUEGO
            gameClock.tick(fps)

            #CIERRE DE VENTANA
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    quit()

            screen.blit(intro,(0,0))
            pygame.display.update()
            text = textContinuar.render('Precione ENTER para comenzar...', 1, (COLOR_AZUL))
            screen.blit(text,(190,470))
            tecla = pygame.key.get_pressed()
            if tecla[pygame.K_RETURN]:
                estaEnIntro = False
            pygame.display.update()

        segundos = TIEMPO_MAX + (pygame.time.get_ticks() / 1000) #variable de control del juego
        totaltime= TIEMPO_MAX+(pygame.time.get_ticks() / 1000) #Variable de suma para saber tiempo del juego

        while True:
            final = True #Variable agregada
            while segundos > fps/1000 and intentos > 0:
            # 1 frame cada 1/fps segundos
                gameClock.tick(fps)
                while palabraCorrecta == "": #Agregado
                #elige una al azar
                    palabraCorrecta=nuevaPalabra(listaPalabrasDiccionario)
                    dibujar(screen, ListaDePalabrasUsuario, palabraUsuario, puntos,segundos, correctas, incorrectas, casi, palabraCorrecta)
                    print(palabraCorrecta)

                if not gano: #Agregado condicional para limpiar las variables
                    #Buscar la tecla apretada del modulo de eventos de pygame
                    for e in pygame.event.get():

                        #QUIT es apretar la X en la ventana
                        if e.type == QUIT:
                            pygame.quit()
                            return()

                        #Ver si fue apretada alguna tecla
                        if e.type == KEYDOWN:
                            letra = dameLetraApretada(e.key)
                            palabraUsuario += letra #es la palabra que escribe el usuario
                            if e.key == K_BACKSPACE:
                                palabraUsuario = palabraUsuario[0:len(palabraUsuario)-1]
                            if e.key == K_RETURN:
                                if estaEnLista(listaPalabrasDiccionario,palabraUsuario) and LARGO == len(palabraUsuario) and not estaEnLista(ListaDePalabrasUsuario,palabraUsuario):
                                    gano = revision(palabraCorrecta, palabraUsuario, correctas, incorrectas, casi)
                                    ListaDePalabrasUsuario.append(palabraUsuario)
                                    palabraUsuario = ""
                                    intentos -= 1

                    segundos = totaltime - pygame.time.get_ticks() / 1000

                #Limpiar pantalla anterior
                    screen.blit(images,(0,0))
                    pygame.display.update()

                #Dibujar de nuevo todo
                    dibujar(screen, ListaDePalabrasUsuario, palabraUsuario, puntos,segundos, correctas, incorrectas, casi, palabraCorrecta)
                    pygame.display.flip()

                else:     #Agregado
                    puntos += 10
                    intentos=5
                    palabraUsuario = ""
                    palabraCorrecta=""
                    ListaDePalabrasUsuario = []
                    correctas = []
                    incorrectas = []
                    casi = []
                    gano = False

        #SECCION VENTANA FINAL



            while final:
            #CONTROL DE VELOCIDAD DEL JUEGO
                gameClock.tick(fps)
             #CIERRE DE VENTANA
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        quit()

                titulo = textContinuar.render('FIN DEL JUEGO', 1, (COLOR_TEXTO))

                if  puntos>0: #NO ES NECESARIO EL NOT GANO
                    screen.blit(imgGano,(0,0))
                    pygame.display.update()
                    resultado = textResultado.render('¡HAS GANADO!', 1, (COLOR_TEXTO))
                else:
                    screen.blit(imgPerdio,(0,0))
                    pygame.display.update()
                    resultado = textResultado.render('¡HAS PERDIDO!', 1, (COLOR_TEXTO))

                pts = textContinuar.render('Puntaje total:' + str(puntos), 1, (COLOR_TEXTO))
                instrucciones = textContinuar.render('Si desea continuar presione ENTER...', 1, (COLOR_TEXTO))
                reintentar = textContinuar.render('Presione R si desea terminar...', 1, (COLOR_TEXTO))
                screen.blit(titulo,(300,5))
                screen.blit(resultado,(200,100))
                screen.blit(pts,(300,200))
                screen.blit(instrucciones,(220,300))
                screen.blit(reintentar,(220,340))
                pygame.display.update()

                tecla = pygame.key.get_pressed()
                if tecla[pygame.K_RETURN]: #Si toca la tecla enter juega de nuevo
                    final=False
                    segundos = TIEMPO_MAX
                    totaltime=(pygame.time.get_ticks() / 1000)+TIEMPO_MAX
                    puntos=0
                    intentos = 5
                    palabraUsuario = ""
                    palabraCorrecta = ""
                    ListaDePalabrasUsuario = []
                    correctas = []
                    incorrectas = []
                    casi = []

                if tecla[pygame.K_r]: #Si toca la tecla R sale del juego
                    pygame.quit()
                    return

            archivo.close()
#Programa Principal ejecuta Main
if __name__ == "__main__":
    main()

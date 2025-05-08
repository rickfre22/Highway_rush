import pygame
import sys
import time

color = (100, 200, 255)
gris = (200, 200, 200)

pygame.init()

ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("highway rush")
font = pygame.font.SysFont(None, 60)

# Carga de imágenes
carro1 = pygame.image.load("img/unnamed (2).png").convert_alpha()  
jugar = pygame.image.load("img/jugar.png").convert_alpha()

# Posiciona el botón en (100, 300) como tú querías
jugar_rect = jugar.get_rect(topleft=(100, 300))

def pantallacarga():
    ventana.fill((0, 0, 0))
    texto = font.render("cargando...", True, (255, 255, 255))
    rect = texto.get_rect(center=(400, 300))
    ventana.blit(texto, rect)
    pygame.display.flip()
    time.sleep(3)

def pantallacarga2():
    ventana.fill((0, 0, 0))
    texto = font.render("iniciando juego :)", True, (255, 255, 255))
    rect = texto.get_rect(center=(400, 300))
    ventana.blit(texto, rect)
    pygame.display.flip()
    time.sleep(2)

def pantallacarga3():
    ventana.fill((0, 0, 0))
    texto = font.render("listo", True, (255, 255, 255))
    rect = texto.get_rect(center=(400, 300))
    ventana.blit(texto, rect)
    pygame.display.flip()
    time.sleep(1)

def inicio_juego():
    esperando = True
    while esperando:
        ventana.fill(gris)
        ventana.blit(jugar, jugar_rect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if jugar_rect.collidepoint(event.pos):
                    esperando = False

def iniciar_juego():
    corriendo = True
    while corriendo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False
        ventana.fill(color)  
        ventana.blit(carro1, (300,500))  
        pygame.display.flip()  

# Flujo del programa
pantallacarga()
pantallacarga2()
pantallacarga3()
inicio_juego()
iniciar_juego()
pygame.quit()
sys.exit()

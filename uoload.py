import pygame
import sys
color =(100,200,255)
pygame.init()

ventana = pygame.display.set_mode((1050,600))
pygame.display.set_caption("juego 1")
font =pygame.font.sysfont(None,60)
def pantallacarga():
    ventana.fill((0,0,0))
    texto = font.render("cargando...",True,(255,255,255))
    rect = texto.get_rect

while True:
    for event in pygame.event.get():
        if  event.type ==pygame.QUIT:
            sys.exit()
    ventana.fill(color)
    pygame.display.flip()
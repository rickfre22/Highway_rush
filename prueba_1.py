import pygame
import time

pygame.init()

# Tamaño de la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pantalla de Carga")

# Fuente para el texto
font = pygame.font.SysFont(None, 60)

# Mostrar pantalla de carga
def mostrar_pantalla_de_carga():
    screen.fill((0, 0, 0))  # Fondo negro
    texto = font.render("Cargando...", True, (255, 255, 255))
    rect = texto.get_rect(center=(400, 300))
    screen.blit(texto, rect)
    pygame.display.flip()
    time.sleep(3)  # Simula la carga durante 3 segundos

# Juego principal
def iniciar_juego():
    corriendo = True
    while corriendo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                corriendo = False

        screen.fill((50, 100, 150))  # Fondo diferente para el juego
        texto = font.render("Juego Iniciado", True, (255, 255, 255))
        rect = texto.get_rect(center=(400, 300))
        screen.blit(texto, rect)

        pygame.display.flip()

    pygame.quit()

# Flujo del programa
mostrar_pantalla_de_carga()
iniciar_juego()




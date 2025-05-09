import pygame
import sys
import time

# Colores y dimensiones
color = (100, 200, 255)
NEGRO = (7, 7, 7)
ANCHO = 800
ALTO = 600
LIMITE_IZQUIERDO = 240
LIMITE_DERECHO = 550

pygame.init()

ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Highway Rush")
font = pygame.font.SysFont(None, 60)

# Carga de imágenes
carro1 = pygame.image.load("img/carro1.png").convert_alpha()
jugar = pygame.image.load("img/jugar.png").convert_alpha()
opciones = pygame.image.load("img/pixil-frame-0.png")
fondo = pygame.image.load("img/fondo.png").convert()
carretera = pygame.image.load("img/carretera.png").convert()
logo = pygame.image.load("img/logo1.png").convert()
# Posiciones de botones
jugar_rect = jugar.get_rect(topleft=(100, 300))
opciones_rect = opciones.get_rect(topleft=(100, 100))

# Clase jugador
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = carro1  # Usar la imagen del carro
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO // 2, ALTO - 50)

    def mover(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > LIMITE_IZQUIERDO:
            self.rect.x -= 15  # Movimientos más suaves
        if keys[pygame.K_RIGHT] and self.rect.right < LIMITE_DERECHO:
            self.rect.x += 15
        

    def reiniciar(self):
        self.rect.center = (ANCHO // 2, ALTO - 50)

# Crear jugador
jugador = Jugador()

# Pantallas de carga
def pantallacarga():
    ventana.fill((NEGRO))
    texto = font.render("Cargando...", True, (100, 255, 255))
    rect = texto.get_rect(center=(ANCHO // 2, ALTO // 2))
    ventana.blit(texto, rect)
    ventana.blit(logo,(320,150))
    pygame.display.flip()
    time.sleep(3)

def pantallacarga2():
    ventana.fill((NEGRO))
    texto = font.render("Iniciando juego :)", True, (100, 255, 255))
    rect = texto.get_rect(center=(ANCHO// 2, ALTO // 2))
    ventana.blit(texto, rect)
    ventana.blit(logo,(320,150))
    pygame.display.flip()
    time.sleep(2)

def pantallacarga3():
    ventana.fill(NEGRO)
    texto = font.render("Listo", True, (100, 255, 255))
    rect = texto.get_rect(center=(ANCHO // 2, ALTO // 2))
    ventana.blit(texto, rect)
    ventana.blit(logo,(320,150))
    pygame.display.flip()
    time.sleep(1)

# Pantalla de inicio con botones
def inicio_juego():
    esperando = True
    while esperando:
        ventana.blit(fondo, (0, 0))
        ventana.blit(jugar, jugar_rect)
        ventana.blit(opciones, opciones_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if jugar_rect.collidepoint(event.pos) or opciones_rect.collidepoint(event.pos):
                    esperando = False

        pygame.display.flip()

# Juego principal
def iniciar_juego():
    corriendo = True
    reloj = pygame.time.Clock()

    while corriendo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False

        keys = pygame.key.get_pressed()
        jugador.mover(keys)

        ventana.blit(carretera, (0, 0))  # Fondo de la carretera
        ventana.blit(jugador.image, jugador.rect)
        pygame.display.flip()

        reloj.tick(60)  # Limitar a 60 FPS

# Flujo del programa
pantallacarga()
pantallacarga2()
pantallacarga3()
inicio_juego()
iniciar_juego()
pygame.quit()
sys.exit()





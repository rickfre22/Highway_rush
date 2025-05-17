import pygame
import sys
import time
import random

# Colores y dimensiones
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
GRIS_CARRETERA = (50, 50, 50)
VERDE = (53, 104, 45)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
ANCHO = 800
ALTO = 600
LIMITE_IZQUIERDO = 150  # Expandir la carretera
LIMITE_DERECHO = 650  # Expandir la carretera

pygame.init()

ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Highway Rush")
font = pygame.font.SysFont(None, 60)

# Fuente para botones
fuente = pygame.font.Font(None, 50)

# Clase jugador
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((60, 100))
        self.image.fill(AZUL)  # Color del jugador
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO // 2, ALTO - 100)

    def mover(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > LIMITE_IZQUIERDO:
            self.rect.x -= 15  # Movimientos más suaves
        if keys[pygame.K_RIGHT] and self.rect.right < LIMITE_DERECHO:
            self.rect.x += 15

    def reiniciar(self):
        self.rect.center = (ANCHO // 2, ALTO - 100)

# Clase autos enemigos
class AutoEnemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((60, 100))
        self.image.fill(ROJO)  # Color del auto enemigo
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(LIMITE_IZQUIERDO, LIMITE_DERECHO - 60)
        self.rect.y = random.randint(-600, -100)
        self.velocidad = 4  # Velocidad moderada

    def update(self):
        self.rect.y += self.velocidad
        if self.rect.top > ALTO:
            self.rect.x = random.randint(LIMITE_IZQUIERDO, LIMITE_DERECHO - 60)
            self.rect.y = random.randint(-600, -100)
            self.velocidad = 4

# Crear jugador
jugador = Jugador()

# Crear grupo de autos enemigos
enemigos = pygame.sprite.Group()
for _ in range(5):  # Se generan varios autos enemigos
    enemigos.add(AutoEnemigo())

# Pantallas de carga
def pantallacarga():
    ventana.fill(NEGRO)
    texto = font.render("Cargando...", True, BLANCO)
    rect = texto.get_rect(center=(ANCHO // 2, ALTO // 2))
    ventana.blit(texto, rect)
    pygame.display.flip()
    time.sleep(2)

# Dibujar botón en el menú
def dibujar_boton(texto, x, y, color):
    rect = pygame.Rect(x, y, 200, 60)
    pygame.draw.rect(ventana, color, rect)
    texto_render = fuente.render(texto, True, NEGRO)
    ventana.blit(texto_render, (x + 50, y + 15))
    return rect

# Menú de inicio
def menu():
    ejecutando = True
    while ejecutando:
        ventana.fill(BLANCO)

        # Dibujar botones
        boton_jugar = dibujar_boton("Start", 300, 200, ROJO)
        boton_salir = dibujar_boton("Salir", 300, 300, VERDE)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.collidepoint(evento.pos):
                    ejecutando = False  # Salir del menú e iniciar el juego
                if boton_salir.collidepoint(evento.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

# Juego principal
def iniciar_juego():
    corriendo = True
    reloj = pygame.time.Clock()

    while corriendo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        jugador.mover(keys)
        enemigos.update()

        # Detección de colisión
        if pygame.sprite.spritecollideany(jugador, enemigos):
            print("¡Choque!")
            corriendo = False  # Termina el juego en caso de colisión

        # Dibujar carretera con límites más grandes
        ventana.fill(GRIS_CARRETERA)
        pygame.draw.rect(ventana, VERDE, (0, 0, LIMITE_IZQUIERDO, ALTO))  # Pasto izquierdo
        pygame.draw.rect(ventana, VERDE, (LIMITE_DERECHO, 0, ANCHO - LIMITE_DERECHO, ALTO))  # Pasto derecho

        # Dibujar autos
        ventana.blit(jugador.image, jugador.rect)
        enemigos.draw(ventana)

        pygame.display.flip()
        reloj.tick(60)  # Limitar a 60 FPS

# Flujo del programa
pantallacarga()
menu()
iniciar_juego()
pygame.quit()
sys.exit()
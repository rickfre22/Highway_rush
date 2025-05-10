import pygame
import sys
import time

# Colores y dimensiones
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)

NEGRO = (7, 7, 7)
ANCHO = 800
ALTO = 600
LIMITE_IZQUIERDO = 240
LIMITE_DERECHO = 550

pygame.init()

ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Highway Rush")
font = pygame.font.SysFont(None, 60)
font2 = pygame.font.SysFont(None,25)
# Carga de imágenes
carro1 = pygame.image.load("img/carro1.png").convert_alpha()
fondo = pygame.image.load("img/fondo.png").convert()
carretera = pygame.image.load("img/carretera.png").convert()

# Clase jugador
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = carro1
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO // 2, ALTO - 50)

    def mover(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > LIMITE_IZQUIERDO:
            self.rect.x -= 15
        if keys[pygame.K_RIGHT] and self.rect.right < LIMITE_DERECHO:
            self.rect.x += 15

    def reiniciar(self):
        self.rect.center = (ANCHO // 2, ALTO - 50)

# Crear jugador
jugador = Jugador()

# Función para dibujar botones
def dibujar_boton(texto, x, y, color):
    rect = pygame.Rect(x, y, 200, 60)
    pygame.draw.rect(ventana, color, rect)
    texto_render = font.render(texto, True, NEGRO)
    ventana.blit(texto_render, (x + 50, y + 15))
    return rect
def dibujar_boton2(texto,x,y,color):
    rect2 = pygame.Rect(x,y,100,30)
    pygame.draw.rect(ventana,color,rect2)
    texto_render2 = font2.render(texto,True,NEGRO)
    ventana.blit(texto_render2,(x + 2, y + 2))
    return rect2
# Pantallas de carga secuenciales al inicio
def pantallas_carga_inicial():
    ventana.fill(NEGRO)
    texto1 = font.render("Cargando...", True, (100, 255, 255))
    rect1 = texto1.get_rect(center=(ANCHO // 2, ALTO // 2))
    ventana.blit(texto1, rect1)
    pygame.display.flip()
    time.sleep(2)

    ventana.fill(NEGRO)
    texto2 = font.render("Iniciando juego :)", True, (100, 255, 255))
    rect2 = texto2.get_rect(center=(ANCHO // 2, ALTO // 2))
    ventana.blit(texto2, rect2)
    pygame.display.flip()
    time.sleep(2)

    ventana.fill(NEGRO)
    texto3 = font.render("Listo", True, (100, 255, 255))
    rect3 = texto3.get_rect(center=(ANCHO // 2, ALTO // 2))
    ventana.blit(texto3, rect3)
    pygame.display.flip()
    time.sleep(2)

# Pantalla de inicio
def inicio_juego():
    while True:
        ventana.blit(fondo, (0, 0))
        boton_jugar = dibujar_boton("iniciar", 300, 200, ROJO)
        boton_salir = dibujar_boton("Salir", 300, 300, VERDE)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.collidepoint(evento.pos):
                    return "jugar"
                if boton_salir.collidepoint(evento.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

# Juego principal
def iniciar_juego():
    corriendo = True
    reloj = pygame.time.Clock()

    while corriendo:
        ventana.blit(carretera, (0, 0))

        # Botones dentro del juego
        boton_menu = dibujar_boton2("Menu", 0, 0, ROJO)
        boton_salir = dibujar_boton2("Salir", 0, 50, ROJO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_menu.collidepoint(evento.pos):
                    return "menu"
                if boton_salir.collidepoint(evento.pos):
                    pygame.quit()
                    sys.exit()

        # Movimiento del jugador
        keys = pygame.key.get_pressed()
        jugador.mover(keys)

        # Dibujar jugador
        ventana.blit(jugador.image, jugador.rect)

        pygame.display.flip()
        reloj.tick(60)

# Función principal
def main():
    # Mostrar pantallas de carga una vez al inicio
    pantallas_carga_inicial()

    while True:
        opcion = inicio_juego()

        if opcion == "jugar":
            resultado = iniciar_juego()
            if resultado == "menu":
                jugador.reiniciar()

main()


# librerias de python
import pygame 
import sys
import time
import random
# Variables
ROJO = (255, 0, 0) 
VERDE = (0, 255, 0)
NEGRO = (7, 7, 7)
ANCHO = 800 
ALTO = 600
LIMITE_IZQUIERDO = 240 
LIMITE_DERECHO = 550
puntos  = "Puntos:"
autos_rebasados = 0
carril1 = 240
carril2 = 360
carril3 = 520
velocidad_trafico = 6
pygame.init()
# Dimensiones de pantalla.
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Highway Rush")
font = pygame.font.SysFont(None, 60)
font2 = pygame.font.SysFont(None, 25)
# Imágenes
carro1 = pygame.image.load("img/carro1.png").convert_alpha()
fondo = pygame.image.load("img/fondo.png").convert()
carretera = pygame.image.load("img/carretera.png").convert()
carretera2 =pygame.image.load("img/carretera2.png").convert()
carros2 = pygame.image.load("img/carro2.png").convert_alpha()
carros3 = pygame.image.load("img/carro3.png").convert_alpha()
niveles = [carretera,carretera2]
nivel_actual = 0
# Clase Jugador
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = carro1
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO // 2, ALTO - 50)
    def mover(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > LIMITE_IZQUIERDO:
            self.rect.x -= 10
        if keys[pygame.K_RIGHT] and self.rect.right < LIMITE_DERECHO:
            self.rect.x += 10
    def reiniciar(self):
        self.rect.center = (ANCHO // 2, ALTO - 110)
jugador = Jugador()
# Clase Tráfico
class Trafico(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        global velocidad_trafico
        self.image = random.choice([carro1, carros2, carros3])
        self.rect = self.image.get_rect()
        carriles = [carril1, carril2, carril3]
        self.rect.x = random.choice(carriles)
        self.rect.y = random.randint(-600, -100)
        self.velocidad = velocidad_trafico
    def update(self):
        self.rect.y += self.velocidad
        if self.rect.top > ALTO:
            self.rect.x = random.choice([carril1, carril2, carril3])
            self.rect.y = random.randint(-600, -100)
            self.velocidad = velocidad_trafico
            
#  botones menu 
def dibujar_boton(texto, x, y, color):
    rect = pygame.Rect(x, y, 200, 60)
    pygame.draw.rect(ventana, color, rect)
    texto_render = font.render(texto, True, NEGRO)
    ventana.blit(texto_render, (x + 50, y + 15))
    return rect

def dibujar_boton2(texto, x, y, color):
    rect2 = pygame.Rect(x, y, 100, 30)
    pygame.draw.rect(ventana, color, rect2)
    texto_render2 = font2.render(texto, True, NEGRO)
    ventana.blit(texto_render2, (x + 2, y + 2))
    return rect2
# Pantallas de carga
def pantallas_carga_inicial():
    mensajes = ["Cargando...", "Iniciando juego...", ]
    for mensaje in mensajes:
        ventana.fill(NEGRO)
        texto = font.render(mensaje, True, (100, 255, 255))
        rect = texto.get_rect(center=(ANCHO // 2, ALTO // 2))
        ventana.blit(texto, rect)
        pygame.display.flip()
        time.sleep(2)
# Pantalla de inicio
def inicio_juego():
    while True:
        ventana.blit(fondo, (0, 0))
        boton_jugar = dibujar_boton("Iniciar", 300, 200, ROJO)
        boton_salir = dibujar_boton("Salir", 300, 300, VERDE)        
        # eventos       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.collidepoint(event.pos):
                    return "jugar"
                if boton_salir.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
        pygame.display.flip()
def reiniciar():
    global  autos_rebasados,velocidad_trafico, nivel_actual
    autos_rebasados = 0
    velocidad_trafico = 6
    nivel_actual = 0
# Juego principal
def iniciar_juego():
    global nivel_actual, velocidad_trafico, autos_rebasados 
    corriendo = True
    cantidad = 2
    reloj = pygame.time.Clock()   
    # Crear grupo de tráfico
    trafico_group = pygame.sprite.Group()
    esperando = True
    for _ in range(cantidad):
        nuevo_auto = Trafico()
        while pygame.sprite.spritecollide(nuevo_auto,trafico_group,False):
            nuevo_auto.rect.y = random.randint(-600,-200)
        trafico_group.add(nuevo_auto)

    while corriendo:
        ventana.blit(niveles[nivel_actual], (0, 0))
        texto = font.render(puntos,True,(0,0,0)) 
        rect = texto.get_rect(topleft=(500,0)) 
        ventana.blit(texto, rect)        
        texto3 = font.render(str(autos_rebasados),True,(0,0,0)) 
        rect3 = texto3.get_rect(topleft=(650,0))     
        ventana.blit(texto3, rect3)
        # Botones del juego
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
        # Movimiento jugador
        keys = pygame.key.get_pressed()
        jugador.mover(keys)
        # Actualizar tráfico
        for auto in trafico_group:
            auto.rect.y += auto.velocidad
            if auto.rect.top > ALTO:
                auto.kill()
                autos_rebasados += 1
                nuevo_auto = Trafico()
                while pygame.sprite.spritecollide(nuevo_auto,trafico_group,False):
                    nuevo_auto.rect.y = random.randint(-1000,-200)
                trafico_group.add(nuevo_auto)      
        
        if autos_rebasados >= 100:         
            velocidad_trafico =8  
            nivel_actual = 1
            
            
        # Dibujar tráfico y jugador
        trafico_group.draw(ventana)
        ventana.blit(jugador.image, jugador.rect)
        # Colisiones
        if pygame.sprite.spritecollide(jugador, trafico_group, False):
            return "menu"    
        pygame.display.flip()
        reloj.tick(60)
# Función principal
def main():
    pantallas_carga_inicial()
    while True:
        opcion = inicio_juego()
        if opcion == "jugar":
            reiniciar()
            resultado = iniciar_juego()
            if resultado == "menu":
                jugador.reiniciar()
main()





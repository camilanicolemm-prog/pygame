import pygame
import random

pygame.init()
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pelota en pygame")

clock = pygame.time.Clock()
FPS = 60

tam = 50
pelota = pygame.Rect(ANCHO//2 - tam//2, ALTO//2 - tam//2, tam,tam)
vx, vy = 6,5

color_pelota = (255, 180, 200)
color_fondo = (255, 220, 235)

rebote_snd = None
try:
    pygame.mixer.init()
    rebote_snd = pygame.mixer.Sound("bounce.wav")
except Exception:
    rebote_snd = None
    
def tocar_rebote():
    if rebote_snd:
        rebote_snd.play()
        
        
def color_aleatorio_fondo():
    """genera colores claros rositas para el fondo"""
    return (random.randint(240, 255), random.randint(200, 230), random.randint(220, 250))

def color_aleatorio_pelota():
    """genera colores brillantes rositas para la pelota"""
    return (random.randint(240, 255), random.randint(150, 200), random.randint(180, 230))

ejecutando = True
while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False
            
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_UP]:
        vx *= 1.02
        vy *= 1.02
    if teclas [pygame.K_DOWN]:
        vx *= 0.98
        vy *= 0.98
    if teclas [pygame.K_SPACE]:
        color_fondo = color_aleatorio_fondo()
        
    pelota.x += int(vx)
    pelota.y += int(vy)
    
    reboto = False
    if pelota.left <= 0 or pelota.right >= ANCHO:
        vx = -vx
        reboto =True
    if pelota.top <= 0 or pelota.bottom >= ALTO:
        vy = -vy
        reboto = True
        
    if reboto:
        tocar_rebote()
        color_pelota = color_aleatorio_pelota()
        color_fondo = color_aleatorio_fondo()
        
        
    pantalla.fill(color_fondo)
    pygame.draw.ellipse(pantalla, color_pelota, pelota)
    pygame.display.update()
    clock.tick(FPS)
    
    
pygame.quit()

                
                
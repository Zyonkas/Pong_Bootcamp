import pygame as pg
from objects import Pelota ,raqueta, Pelota

pg.init()

pantalla_principal = pg.display.set_mode((800,600))
pg.display.set_caption("Pong")
cronometro = pg.time.Clock()

game_over = False
Pelota = Pelota(400, 300, color=(255,255,255))
Pelota.vx = 5
Pelota.vy = -5
raqueta1 = raqueta(20, 300, w=20, h=120, color=(255,255,255))
raqueta2 = raqueta(780, 300, w=20, h=120, color=(255,255,255))
raqueta2.vy = 5
raqueta1.vy = 5


while not game_over:
    dt = cronometro.tick(60)

    #Eventos que have el usuario y devuelve una lista de eventos
    for evento in pg.event.get():
        if evento.type == pg.quit:
            game_over = True 
    
    raqueta2.mover(pg.K_UP, pg.K_DOWN)           
    raqueta1.mover(pg.K_LSHIFT, pg.K_LCTRL)
    Pelota.mover()

    pantalla_principal.fill((0,0,0))
    Pelota.draw(pantalla_principal)
    raqueta1.draw(pantalla_principal)
    raqueta2.draw(pantalla_principal)
    
    #Le pasa la informacion a la GPU
    pg.display.flip()


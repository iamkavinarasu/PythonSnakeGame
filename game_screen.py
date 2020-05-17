import pygame as pg


red = [255,0,0]
green = [0,255,0]
black = [0,0,0]
white = [255,255,255]

screen_width = 400
screen_height = 400

pg.init()
wn = pg.display.set_mode((screen_width,screen_height))
pg.display.set_caption("Snake game")

run = True
while run:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			run = False

	wn.fill(black)

pg.quit()

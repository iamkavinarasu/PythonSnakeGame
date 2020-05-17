import pygame as pg
pg.init()
wn = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('A simple game of Snake')
fd = Food()
p = Player()
play_game(fd,p)
pg.quit()
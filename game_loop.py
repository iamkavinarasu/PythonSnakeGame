score, high_score = (0,0)
# Draw the score on the screen
def draw_score(surface):
    global high_score
    font_name = pg.font.match_font('arial')
    if score > high_score:
        high_score = score
    # writing the score
    font = pg.font.Font(font_name, 18)
    text_surface = font.render('Score: {} High Score: {}'.format(score, high_score), True, white)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (200 , 10)
    surface.blit(text_surface, text_rect)
# What to do when the game is over
def game_over():
    global score
    # writing game over
    gameOverFont = pg.font.Font('freesansbold.ttf', 24)
    gameOverSurf = gameOverFont.render('Game Over', True, white)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (200, 50)
    wn.blit(gameOverSurf, gameOverRect)
    # reset score
    score = 0
    pg.display.flip()
    time.sleep(2)
    # re-initialize game
    run = True
    fd = Food()
    p = Player()
    play_game(fd, p)
# The game
def play_game(fd, p):
    global score
    run = True
    while run:
        # FPS
        clock.tick(30)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        # draw food, snake, score
        wn.fill(black)
        fd.draw_food(wn)
        p.draw_player(wn)
        draw_score(wn)
        # user input
        pressed = pg.key.get_pressed()
        if pressed[pg.K_UP]:
            p.change_direction('up')
        if pressed[pg.K_LEFT]:
            p.change_direction('left')
        if pressed[pg.K_DOWN]:
            p.change_direction('down')
        if pressed[pg.K_RIGHT]:
            p.change_direction('right')
        # move snake
        p.move()
        # eating
        if fd.is_eaten(p.head):
            fd.new_pos()
            p.add_unit()
            score += 10
        # collision
        if p.is_collision():
            run = False
            game_over()

        pg.display.update()
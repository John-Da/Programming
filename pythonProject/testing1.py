
# import pygame

# pygame.init()
# screen = pygame.display.set_mode((1280, 720))
# clock = pygame.time.Clock()
# running = True
# dt = 0

# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# while running:

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
    
#     screen.fill("purple")

#     pygame.draw.circle(screen, 'red', player_pos, 40)

#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_w]:
#         player_pos.y -= 300 * dt
#     if keys[pygame.K_s]:
#         player_pos.y += 300 * dt
#     if keys[pygame.K_a]:
#         player_pos.x -= 300 * dt
#     if keys[pygame.K_d]:
#         player_pos.x += 300 * dt


#     pygame.display.flip()
#     dt = clock.tick(60) / 1000


# pygame.quit()














# import pygame


# pygame.init()

# screen = pygame.display.set_mode((1200, 720))
# font = pygame.font.Font(None, 40)
# blue = pygame.Color('blue')




# clock = pygame.time.Clock()
# running = True
# dd = 0
# timer = 60


# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
        
#     timer -= dd
#     if timer <= 10:
#         timer = 10
    
#     screen.fill("purple")
#     text = font.render(str(round(timer, 2)), True, blue)
#     screen.blit(text, (70, 70))

#     pygame.display.flip()
#     clock.tick(30) / 1000

# pygame.quit()









# Second Count Down
# import pygame as pg


# def main():
#     pg.init()
#     screen = pg.display.set_mode((640, 480))
#     font = pg.font.Font(None, 40)
#     gray = pg.Color('gray19')
#     blue = pg.Color('dodgerblue')
#     # The clock is used to limit the frame rate
#     # and returns the time since last tick.
#     clock = pg.time.Clock()
#     timer = 60  # Decrease this to count down.
#     dt = 0  # Delta time (time since last tick).

#     done = False
#     while not done:
#         for event in pg.event.get():
#             if event.type == pg.QUIT:
#                 done = True

#         timer -= dt
#         if timer <= 0:
#             timer = 10  # Reset it to 10 or do something else.

#         screen.fill(gray)
#         txt = font.render(str(round(timer, 2)), True, blue)
#         screen.blit(txt, (70, 70))
#         pg.display.flip()
#         dt = clock.tick(30) / 1000  # / 1000 to convert to seconds.


# if __name__ == '__main__':
#     main()
#     pg.quit()



# import pygame
# pygame.init()
# screen = pygame.display.set_mode((128, 128))
# clock = pygame.time.Clock()

# counter, text = 10, '10'.rjust(3)
# pygame.time.set_timer(pygame.USEREVENT, 1000)
# font = pygame.font.SysFont('Consolas', 30)

# run = True
# while run:
#     for e in pygame.event.get():
#         if e.type == pygame.USEREVENT: 
#             counter -= 1
#             text = str(counter).rjust(3) if counter > 0 else 'boom!'
#         if e.type == pygame.QUIT: 
#             run = False

#     screen.fill((255, 255, 255))
#     screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
#     pygame.display.flip()
#     clock.tick(60)



# import pygame as pg

# pg.init()

# screen = pg.display.set_mode((450, 600))
# timer_font = pg.font.Font('0.4B_19__.ttf', 38)
# timer_sec = 60


# def show_timer():
#     global timer_sec

#     while timer_sec > 0:
#         timer_text = timer_font.render('00:%s' % str(timer_sec), True, (255, 255, 255))
#         screen.blit(timer_text, (300, 20))

#         pg.time.wait(1000)
#         timer_sec -= 1


# running = True
# while running:
#     screen.fill((0, 0, 0))

#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             running = False

#     show_timer()
#     pg.display.update()



# import pygame
# pygame.init()

# screen = pygame.display.set_mode((450, 600))

# timer_font = pygame.font.Font("04B_19__.ttf", 38)
# timer_sec = 60
# timer_text = timer_font.render("01:00", True, (255, 255, 255))

# # USEREVENTS are just integers
# # you can only have like 31 of them or something arbitrarily low
# timer = pygame.USEREVENT + 1                                                
# pygame.time.set_timer(timer, 1000)    # sets timer with USEREVENT and delay in milliseconds

# running = True
# while running:
#     screen.fill((0, 0, 0))

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == timer:    # checks for timer event
#             if timer_sec > 0:
#                 timer_sec -= 1
#                 timer_text = timer_font.render("00:%02d" % timer_sec, True, (255, 255, 255))
#             else:
#                 pygame.time.set_timer(timer, 0)    # turns off timer event

# # add another "if timer_sec > 0" here if you want the timer to disappear after reaching 0
#     screen.blit(timer_text, (300, 20))
#     pygame.display.update()
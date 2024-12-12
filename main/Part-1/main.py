import pygame
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Platformer")
clock = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False

    pygame.display.update()
    clock.tick(120)

pygame.quit()

import pygame
pygame.init()

BACKGROUND_COLOR = (60, 60, 60)

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Platformer")
clock = pygame.time.Clock()

player_image = pygame.image.load("images/yoka.png")
player_width, player_height = 48, 60
player_image = pygame.transform.scale(player_image, (player_width, player_height))
player_x = SCREEN_WIDTH / 2 - player_width / 2
player_y = SCREEN_HEIGHT / 2 - player_height / 2
player_velocity_x = 0
player_velocity_y = 0
player_speed = 3

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False

    if keys[pygame.K_a]:
        player_velocity_x = -player_speed
    elif keys[pygame.K_d]:
        player_velocity_x = player_speed
    else:
        player_velocity_x = 0

    player_x += player_velocity_x
    player_y += player_velocity_y

    screen.fill(BACKGROUND_COLOR)

    screen.blit(player_image, (player_x, player_y))

    pygame.display.update()
    clock.tick(120)

pygame.quit()

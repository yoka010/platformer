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
player_image_right = pygame.transform.scale(player_image, (player_width, player_height))
player_image_left = pygame.transform.scale(player_image, (player_width, player_height))
player_image_left = pygame.transform.flip(player_image_left, True, False)
player_x = SCREEN_WIDTH / 2 - player_width / 2
player_y = SCREEN_HEIGHT / 2 - player_height / 2
player_velocity_x = 0
player_velocity_y = 0
player_gravity = 0.25
player_gravity_smoothing = 0.5
player_speed = 3
player_jump_speed = -6
player_on_ground = False
player_flip = False

platforms_image = pygame.image.load("images/platform.png")
platforms = [
    pygame.Rect((SCREEN_WIDTH / 2) - 200, 600, 400, 50)
]

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    new_player_x = player_x
    new_player_y = player_y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False

    if keys[pygame.K_a] and not keys[pygame.K_d]:
        player_velocity_x = -player_speed
        player_flip = True
    elif keys[pygame.K_d] and not keys[pygame.K_a]:
        player_velocity_x = player_speed
        player_flip = False
    else:
        player_velocity_x = 0

    if keys[pygame.K_SPACE] and player_on_ground:
        player_velocity_y = player_jump_speed

    new_player_x += player_velocity_x

    new_player_rect_x = pygame.Rect(new_player_x, player_y, player_width, player_height)
    player_x_collision = False
    for platform in platforms:
        if platform.colliderect(new_player_rect_x):
            player_x_collision = True

    if not player_x_collision:
        player_x = new_player_x

    player_velocity_y += player_gravity * player_gravity_smoothing
    new_player_y += player_velocity_y
    player_on_ground = False

    new_player_rect_y = pygame.Rect(player_x, new_player_y, player_width, player_height)
    player_y_collision = False
    for platform in platforms:
        if platform.colliderect(new_player_rect_y):
            if platform.y > player_y:
                player_on_ground = True
            player_velocity_y = 0
            player_y_collision = True

    if not player_y_collision:
        player_y = new_player_y

    if keys[pygame.K_r]:
        player_velocity_y = 0
        player_x = SCREEN_WIDTH / 2 - player_width / 2
        player_y = SCREEN_HEIGHT / 2 - player_height / 2

    screen.fill(BACKGROUND_COLOR)

    for platform in platforms:
        platform_scale_image = pygame.transform.scale(platforms_image, (platform.width, platform.height))
        screen.blit(platform_scale_image, (platform.x, platform.y))

    if not player_flip:
        screen.blit(player_image_right, (player_x, player_y))
    if player_flip:
        screen.blit(player_image_left, (player_x, player_y))

    pygame.display.update()
    clock.tick(120)

pygame.quit()
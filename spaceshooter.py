import math
import pygame
import random
screen_width = 800
screen_height = 500
player_start_x = 370
player_start_y = 380
enemy_start_x_min = 50
enemy_start_x_max = 150
enemy_speed_x = 4
enemy_speed_y = 40
bullet_speed = 10
collision_distance = 27
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load('bg.jpg')
pygame.display.set_caption("Space Shooter")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
playerImg = pygame.image.load('player.png')
playerX = player_start_x
playerY = player_start_y
playerX_change = 0
playerImg = pygame.transform.scale(pygame.image.load('player.png'), (64, 64))
enemyImg = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    playerImg = pygame.transform.scale(pygame.image.load('enemy.png'), (64, 64))
    enemyx.append(random.randint(0, screen_width - 64))
    enemyy.append(random.randint(enemy_start_x_min, enemy_start_x_max))
    enemyx_change.append(enemy_speed_x)
    enemyy_change.append(enemy_speed_y)
bulletImg = pygame.image.load('bullet.png')
bulletx = 0
bullety = playerY
bulletx_change = 0
bullety_change = bullet_speed
bullet_state = "ready"
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 64)
textX = 10
textY = 10
over_font = pygame.font.Font('freesansbold.ttf', 64)
def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (screen_width // 2 - over_text.get_width() // 2, screen_height // 2 - over_text.get_height() // 2))
def player(x, y):
    screen.blit(playerImg, (x, y))
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((math.pow(enemy_x - bullet_x, 2)) + (math.pow(enemy_y - bullet_y, 2)))
    return distance < collision_distance
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletx = playerX
                    fire_bullet(bulletx, bullety)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    playerX += playerX_change
    playerX = max(0, min(playerX, screen_width - 64))
    for i in range(num_of_enemies):
        if enemyy[i] > screen_height:
            for j in range(num_of_enemies):
                enemyy[j] = 2000
            game_over_text()
            break
        enemyx[i] += enemyx_change[i]
        if enemyx[i] <= 0:
            enemyx_change[i] = enemy_speed_x
            enemyy[i] += enemyy_change[i]
        elif enemyx[i] >= screen_width - 64:
            enemyx_change[i] = -enemy_speed_x
            enemyy[i] += enemyy_change[i]
        collision = is_collision(enemyx[i], enemyy[i], bulletx, bullety)
        if collision:
            bullety = playerY
            bullet_state = "ready"
            score_value += 1
            enemyx[i] = random.randint(0, screen_width - 64)
            enemyy[i] = random.randint(enemy_start_x_min, enemy_start_x_max)
        enemy(enemyx[i], enemyy[i], i)
    if bullety == 0:
        bullety = playerY
        bullet_state = "ready"
    elif bullet_state == "fire":
        fire_bullet(bulletx, bullety)
        bullety -= bullety_change
    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
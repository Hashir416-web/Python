import pygame
import random
screen_width, screen_height = 500, 400
movement_speed = 5
font_size = 72
pygame.init()
backgroundimage = pygame.transform.scale(pygame.image.load("bg.jpg"), (screen_width, screen_height))
font = pygame.font.Font("Times New Roman", font_size)
class Sprite(pygame.sprite.Sprite):
    def __init__(self, colour, height, width):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(pygame.Color('Dodgerblue'))
        pygame.draw.rect(self.image, colour, (0, 0, width, height), 0)
        self.rect = self.image.get_rect()
    def move (self, x_change, y_change):
        self.rect.x = max(min(self.rect.x + x_change, screen_width - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, screen_height - self.rect.height), 0)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Collision")
all_sprites = pygame.sprite.Group()
sprites_1 = Sprite(pygame.Color('Yellow'), 20, 30)
sprites_1.rect.x, sprites_1.rect.y = random.randint(0, screen_width - sprites_1.rect.width), random.randint(0, screen_height - sprites_1.rect.height)
all_sprites.add(sprites_1)
sprites_2 = Sprite(pygame.Color('Purple'), 20, 30)
sprites_2.rect.x, sprites_2.rect.y = random.randint(0, screen_width - sprites_2.rect.width), random.randint(0, screen_height - sprites_2.rect.height)
all_sprites.add(sprites_2)
running,won = True, False
clock = pygame.time.Clock()
while running:
    for event in pygame.get():
        if event.type == pygame.QUIT:
            running = False
        if not won:
            keys = pygame.key.get_pressed()
            x_change, = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT] * movement_speed
            y_change = keys[pygame.K_DOWN] - keys[pygame.K_UP] * movement_speed
            sprites_1.move(x_change, y_change)
            if sprites_1.rect.colliderect(sprites_2.rect):
                won = True
                win_text = font.render("You Win!", True, pygame.Color('White'))
                screen.blit(win_text, (screen_width // 2 - win_text.get_width() // 2, screen_height // 2 - win_text.get_height() // 2))
            pygame.display.flip()
            clock.tick(90)
pygame.quit()
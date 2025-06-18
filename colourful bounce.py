import pygame
import random
pygame.init()
sprite_color_change_event = pygame.USEREVENT + 1
background_color_change_event = pygame.USEREVENT + 2
blue = pygame.Color("blue")
light_blue = pygame.Color("lightblue")
dark_blue = pygame.Color("darkblue")
yellow = pygame.Color("yellow")
purple = pygame.Color("purple")
orange = pygame.Color("orange")
white = pygame.Color("white")
class Sprite(pygame.sprite.Sprite):
    def __init__(self, colour, height, width):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        if self.rect.left < 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        if self.rect.top < 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True
        if boundary_hit:
            pygame.event.post(pygame.event.Event(sprite_color_change_event))
            pygame.event.post(pygame.event.Event(background_color_change_event))

    def change_color(self):
        self.image.fill(random.choice([yellow, purple, orange, white]))

def change_background_color():
    global bg_color
    bg_color = random.choice([blue, light_blue, dark_blue])

all_spirtes_list = pygame.sprite.Group()
sp1 = Sprite(white, 20, 20)
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 380)
all_spirtes_list.add(sp1)
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Colourful Bounce")
bg_color = blue
screen.fill(bg_color)
exit_game = False
clock = pygame.time.Clock()
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        elif event.type == sprite_color_change_event:
            sp1.change_color()
        elif event.type == background_color_change_event:
            change_background_color()
    all_spirtes_list.update()
    screen.fill(bg_color)
    all_spirtes_list.draw(screen)
    pygame.display.flip()
    clock.tick(240)
pygame.quit()
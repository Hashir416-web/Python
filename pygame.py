import pygame
pygame.init()
screen_width, screen_height = 800, 600
display_surface = pygame.display.set_mode ((screen_width,screen_height))
pygame.display.set_caption("Adding image tot he background")
background_image = pygame.image.load("background.jpg").convert()
(screen_width, screen_height)
penguin_image = pygame.transform.scale(pygame.image.load("penguin.png").convert_alpha(), (200, 200))
penguin_rect = penguin_image.get_rect(center=(screen_width // 2, screen_height // 2-30))
text = pygame.font.Font(None, 36).render("Hello, Pygame!", True, pygame.Color('black'))
text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2 + 110))
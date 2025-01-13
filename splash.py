import pygame
import sys
import time

import menu

# Starts pygame
pygame.init()

# Screen Configuration
WIDTH, HEIGHT = 1800, 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monkey Kong")

# Clock
clock = pygame.time.Clock()

# Colors
Brown = (92, 64, 51)
Tan = (222, 184, 135)

# Fonts
font_title = pygame.font.SysFont("fonts/donkey.ttf", 150)

# Load image
palm_image = pygame.image.load("imagenes/palmeras.png").convert_alpha()

# Resize image proportionally
palm_image = pygame.transform.scale(palm_image, (WIDTH, HEIGHT))

# Function splash
def main():
    # Text
    text_title = font_title.render("Monkey Kong", True, Tan)
    text_rect = text_title.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    text_surface = pygame.Surface(text_title.get_size(), pygame.SRCALPHA)
    text_surface.blit(text_title, (0, 0))

    # Animation fases
    duration_fade = 60  # frames to appear aparecer
    duration_visible = 90  # frames visibles without change
    duration_fade_out = 60  # frames to disappear

    total_frames = duration_fade + duration_visible + duration_fade_out
    frame, t = 0, 0
    running = True
    while running:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.fill(Brown)
        SCREEN.blit(palm_image, (0, 0))

        # Calculte opacity based on frame
        if frame < duration_fade:
            alpha = int((frame / duration_fade) * 255)  # Appear
        elif frame < duration_fade + duration_visible:
            alpha = 255  # Visible
        elif frame < total_frames:
            alpha = int(((total_frames - frame) / duration_fade_out) * 255)  # Dissapear
        elif t == 0:
            frame = 0
            t = 1
            text_title = font_title.render("By Nicole Valverde", True, Tan)
            text_rect = text_title.get_rect(center=(WIDTH // 2, HEIGHT // 2)) # Show Credits

            text_surface = pygame.Surface(text_title.get_size(), pygame.SRCALPHA)
            text_surface.blit(text_title, (0, 0))
        else:
            running = False
            menu.mostrar_menu() # Start Menu

        # Draw text
        text_surface.set_alpha(alpha)
        SCREEN.blit(text_surface, text_rect)

        pygame.display.flip()
        clock.tick(60)
        frame += 1


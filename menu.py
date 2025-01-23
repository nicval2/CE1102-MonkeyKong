import pygame
import sys
import scoreboard
import first_level
import second_level

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
ButtonHover = (200, 170, 120)

# Fonts
font_title = pygame.font.SysFont("fonts/donkey.ttf", 150)
font_menu = pygame.font.SysFont("fonts/donkey.ttf", 100)

# Load image
palm_image = pygame.image.load("imagenes/palmeras.png").convert_alpha()
palm_image = pygame.transform.scale(palm_image, (WIDTH, HEIGHT))

# Buttons
buttons = [
    {"text": "Nivel Uno", "pos": (WIDTH//2, 300)},
    {"text": "Nivel Dos", "pos": (WIDTH//2, 430)},
    {"text": "Salón de la fama", "pos": (WIDTH//2, 560)},
    {"text": "Salir", "pos": (WIDTH//2, 690)}
]

# Function to draw button
def draw_button(button):
    mouse_pos = pygame.mouse.get_pos()
    text_color = Tan
    text_surface = font_menu.render(button["text"], True, text_color)
    rect = text_surface.get_rect(center=button["pos"])
    # Change color when pressed
    if rect.collidepoint(mouse_pos):
        text_surface = font_menu.render(button["text"], True, ButtonHover)
    SCREEN.blit(text_surface, rect.topleft)
    return rect  # Detect Clicks

# Show menu
def menu():
    running = True
    while running:
        SCREEN.fill(Brown)
        SCREEN.blit(palm_image, (0, 0))

        # Draw title
        title = font_title.render("MENÚ PRINCIPAL", True, Tan)
        SCREEN.blit(title, (WIDTH//2 - title.get_width()//2, 100))

        # Draw buttons
        button_rects = [draw_button(b) for b in buttons]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Click buttons
                for i, rect in enumerate(button_rects):
                    if rect.collidepoint(event.pos):
                        if i == 0:
                            first_level.first_level()
                            print("Nivel Uno seleccionado")
                        elif i == 1:
                            second_level.second_level()
                            print("Nivel Dos seleccionado")
                        elif i == 2:
                            print("Salón de la fama seleccionado")
                            running = False
                            scoreboard.scoreboard()
                        elif i == 3:
                            pygame.quit()
                            sys.exit()

        pygame.display.flip()
        clock.tick(60)



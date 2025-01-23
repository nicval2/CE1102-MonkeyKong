import pygame
import sys
import menu
import first_level
import scoreboard

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
Green = (0, 255, 0)

# Fonts
font_title = pygame.font.SysFont("fonts/donkey.ttf", 150)
font_menu = pygame.font.SysFont("fonts/donkey.ttf", 50)

# Load image
palm_image = pygame.image.load("imagenes/palmeras.png").convert_alpha()
palm_image = pygame.transform.scale(palm_image, (WIDTH, HEIGHT))

# Buttons
menu_button = {"text": "Menú", "pos": (WIDTH//2 + 300, 700)}
next_button = {"text": "Siguiente", "pos": (WIDTH//2 + 300, 500)}
replay_button = {"text": "Repetir", "pos": (WIDTH//2 - 300, 500)}
scoreboard_button = {"text": "Salón de fama", "pos": (WIDTH//2 - 300, 700)}



# Scoreboard
def losing(level):
    running = True
    # Buttons
    if level == 1:
        next_button = {"text": "Siguiente", "pos": (WIDTH//2 + 300, 500)}
        replay_button = {"text": "Repetir", "pos": (WIDTH//2 - 300, 500)}
    else: 
        next_button = {"text": "Repetir", "pos": (WIDTH//2 + 300, 500)}
        replay_button = {"text": "Anterior", "pos": (WIDTH//2 - 300, 500)}
    menu_button = {"text": "Menú", "pos": (WIDTH//2 + 300, 700)}
    scoreboard_button = {"text": "Salón de fama", "pos": (WIDTH//2 - 300, 700)}

    while running:
        SCREEN.fill(Brown)
        SCREEN.blit(palm_image, (0, 0))

        # Draw title
        title = font_title.render("Perdiste :(", True, Tan)
        SCREEN.blit(title, (WIDTH//2 - title.get_width()//2, 200))

        # Draw return button
        button_menu = menu.draw_button(menu_button)
        button_next = menu.draw_button(next_button)
        button_replay = menu.draw_button(replay_button)
        button_scoreboard = menu.draw_button(scoreboard_button)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if button_menu.collidepoint(event.pos):
                        running = False
                        menu.menu()  # Return to menu
                    if button_replay.collidepoint(event.pos):
                        running = False
                        first_level.first_level()  
                    if button_scoreboard.collidepoint(event.pos):
                        running = False
                        scoreboard.scoreboard()
                    

        pygame.display.flip()
        clock.tick(60)

import pygame
import sys
import menu
import first_level
import scoreboard
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
Black = (0, 0, 0)
Green = (0, 255, 0)

# Fonts
font_title = pygame.font.SysFont("fonts/donkey.ttf", 150)
font_menu = pygame.font.SysFont("fonts/donkey.ttf", 50)

# Load image
palm_image = pygame.image.load("imagenes/palmeras.png").convert_alpha()
palm_image = pygame.transform.scale(palm_image, (WIDTH, HEIGHT))


def save_score(path, name, score):
    scores = []

    # Read file if it exists
    try:
        with open(path, "r") as file:
            data = file.read().strip()
            if data:
                data = data.split(";")
                for i in range(0, len(data) - 1, 2):
                    player_name = data[i]
                    player_score = int(data[i + 1])
                    scores.append((player_name, player_score))
    except FileNotFoundError:
        pass  # File does not exist yet

    # Add new score
    scores.append((name, score))

    # Sort scores from highest to lowest
    scores.sort(key=lambda x: x[1], reverse=True)

    # Write back to file
    with open(path, "w") as file:
        file.write(";".join(f"{name};{score}" for name, score in scores))





# Scoreboard
def winning(score, level):
    running = True
    path = "scores/highscores.txt"
    # Input box
    input_rect = pygame.Rect(750, 280, 300, 40)
    input_color_active = Tan
    input_color_inactive = Green
    input_color = input_color_inactive
    active = False
    name = ""
    label_name = ""
    saved = False

    # Buttons
    if level == 1:
        next_button = {"text": "Siguiente", "pos": (WIDTH//2 + 300, 600)}
        replay_button = {"text": "Repetir", "pos": (WIDTH//2 - 300, 600)}
    else: 
        next_button = {"text": "Repetir", "pos": (WIDTH//2 + 300, 600)}
        replay_button = {"text": "Anterior", "pos": (WIDTH//2 - 300, 600)}
    menu_button = {"text": "Menú", "pos": (WIDTH//2 + 300, 700)}
    scoreboard_button = {"text": "Salón de fama", "pos": (WIDTH//2 - 300, 700)}
    save_button = {"text": "Guardar nombre", "pos": (WIDTH//2, 450)}

    while running:
        SCREEN.fill(Brown)
        SCREEN.blit(palm_image, (0, 0))

        # Draw title
        title = font_title.render("Ganaste!!!!", True, Tan)
        SCREEN.blit(title, (WIDTH//2 - title.get_width()//2, 100))

        # Draw return button
        button_menu = menu.draw_button(menu_button)
        button_next = menu.draw_button(next_button)
        button_replay = menu.draw_button(replay_button)
        button_scoreboard = menu.draw_button(scoreboard_button)
        button_save_name = menu.draw_button(save_button)

        # Input
        pygame.draw.rect(SCREEN, input_color, input_rect, 2)
        input_surface = font_menu.render(name, True, Black)
        SCREEN.blit(input_surface, (WIDTH//2 - input_surface.get_width()//2, 280))

        label_surface = font_menu.render("Ingresa tu nombre", True, Tan)
        SCREEN.blit(label_surface, (WIDTH//2 - label_surface.get_width()//2, 200))

        label_surface = font_menu.render(label_name, True, Tan)
        SCREEN.blit(label_surface, (WIDTH//2 - label_surface.get_width()//2, 350))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False 
                if event.button == 1:
                    if button_menu.collidepoint(event.pos):
                        running = False
                        menu.menu()  # Return to menu
                    if button_replay.collidepoint(event.pos):
                        running = False
                        first_level.first_level()  
                    if button_next.collidepoint(event.pos):
                        running = False
                        second_level.second_level() 
                    if button_scoreboard.collidepoint(event.pos):
                        running = False
                        scoreboard.scoreboard()
                    if button_save_name.collidepoint(event.pos):
                        if name == "":
                            label_name = "Debes de ingresar un nombre"
                        else:
                            label_name = "Se guardó el puntaje de: " + name
                            if saved == False:
                                save_score(path, name, score)
                                saved = True
                            else:
                                label_name = "Ya se guardó este puntaje"
                            name = ""


            # Writing
            if event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode
                    
        input_color = input_color_active if active else input_color_inactive

        pygame.display.flip()
        clock.tick(60)

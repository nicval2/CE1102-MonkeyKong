import pygame
import sys
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
ButtonHover = (200, 170, 120)

# Fonts
font_title = pygame.font.SysFont("fonts/donkey.ttf", 150)
font_menu = pygame.font.SysFont("fonts/donkey.ttf", 100)

# Load images
palm_image = pygame.image.load("imagenes/palmeras.png").convert_alpha()
palm_image = pygame.transform.scale(palm_image, (WIDTH, HEIGHT))
platform_image = pygame.image.load("imagenes/platform.png").convert_alpha()
platform_image = pygame.transform.scale(platform_image, (100, 50))
player_image = pygame.image.load("imagenes/Player_1.png").convert_alpha()
player_image = pygame.transform.scale(player_image, (50, 50))


# Button
return_button = {"text": "Regresar", "pos": (WIDTH//2, 860)}

# Function to read scores
def read_scores(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().strip().split(",")
            # Convertir a tuplas (nombre, puntuación)
            scores = [(content[i], content[i+1]) for i in range(0, len(content), 2)]
            return scores[:3]  # Solo los primeros 3 lugares
    except Exception as e:
        print("Error leyendo archivo:", e)
        return []


def draw_platforms(x, y):
    if y == 730 and x < 900:
        SCREEN.blit(platform_image, (x, y))
        return draw_platforms(x + 100, y)
    elif y > 620 and 900 <= x < 1300:
        SCREEN.blit(platform_image, (x, y))
        return draw_platforms(x + 100, y - 20)
    elif y > 620 and 1300 <= x < 1400:
        SCREEN.blit(platform_image, (x, y))
        return draw_platforms(x - 100, 540)
    elif y == 540 and 900 <= x < 1300:
        SCREEN.blit(platform_image, (x, y))
        return draw_platforms(x - 100, y)
    elif y > 460 and x < 900:
        SCREEN.blit(platform_image, (x, y))
        return draw_platforms(x - 100, y - 20)
    elif y == 460 and 400 == x:
        SCREEN.blit(platform_image, (x, y))
        return draw_platforms(x + 100, 350)
    elif 260 < y < 360 and 400 < x < 1300:
        SCREEN.blit(platform_image, (x, y))
        return draw_platforms(x + 100, y)
    elif 230 < y < 360 and x == 1300:
        SCREEN.blit(platform_image, (x, y))
        return draw_platforms(900, 230)
    elif y == 230 and x < 1300:
        SCREEN.blit(platform_image, (x, y))
        return draw_platforms(x + 100, y)
    else:
        SCREEN.blit(platform_image, (x, y))
        return 0

# Player movement
def movement(x, y):
    if (974 == x and y == 680) or (1072 == x and y == 660) or (1176 == x and y == 640) or (1268 == x and y == 620) or (x == 484 and y == 430) or (x == 580 and y == 450) or (x == 680 and y == 470) or (x == 770 and y == 490):
        y -= 20
    if (972 == x  and y == 660) or (1070 == x  and y == 640) or (1162 == x  and y == 620) or (1256 == x  and y == 600) or (x == 504 and y == 410) or (x == 598 and y == 430) or (x == 700 and y == 450) or (x == 794 and y == 470):
        y += 20  
    return y


# First Level
def first_level():
    scores = read_scores("scores/highscores.txt")
    running = True
    x = 450
    #y = 680
    y = 410
    velocity = 2
    while running:
        SCREEN.fill(Brown)
        SCREEN.blit(palm_image, (0, 0))
        SCREEN.blit(player_image, (x, y))

        # Check movement in keyboard
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and x >= 430:
            x -= velocity
            print(x)
        if key[pygame.K_RIGHT] and x <= 1350:
            x += velocity
            print(x)

        y = movement(x, y)

        # Draw platforms
        draw_platforms(400, 730) # Initial position

        # Draw title
        title = font_title.render("Primer Nivel", True, Tan)
        SCREEN.blit(title, (WIDTH//2 - title.get_width()//2, 20))

        # Draw return button
        button_rect = menu.draw_button(return_button)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_rect.collidepoint(event.pos):
                    running = False
                    menu.menu()  # Return to menu

        pygame.display.flip()
        clock.tick(60)

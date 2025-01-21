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
ladder_image = pygame.image.load("imagenes/Ladder.png").convert_alpha()
ladder_image = pygame.transform.scale(ladder_image, (25,25))
player_image_1 = pygame.image.load("imagenes/Mario_Run1.png").convert_alpha()
player_image_1 = pygame.transform.scale(player_image_1, (50, 50))
player_image_1_flip = pygame.transform.flip(player_image_1, True, False)
player_image_2 = pygame.image.load("imagenes/Mario_Run2.png").convert_alpha()
player_image_2 = pygame.transform.scale(player_image_2, (50, 50))
player_image_2_flip = pygame.transform.flip(player_image_2, True, False)
player_image_3 = pygame.image.load("imagenes/Mario_Run3.png").convert_alpha()
player_image_3 = pygame.transform.scale(player_image_3, (50, 50))
player_image_3_flip = pygame.transform.flip(player_image_3, True, False)
player_image_climb = pygame.image.load("imagenes/Mario_Climb.png").convert_alpha()
player_image_climb = pygame.transform.scale(player_image_climb, (50, 50))


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

def draw_ladders(): 
    ladders = [(1000, 685), (1000, 660), (1000, 635), (1000, 610), (1000, 585), (1000, 560), (1000, 535), (1230, 645), (1230, 620), 
    (1230, 595), (1230, 570), (1230, 545), (1230, 535), (510, 455), (510, 430), (510, 405), (510, 380), (510, 355), (510, 343), (1120, 225), 
    (1120, 250), (1120, 275), (1120, 300), (1120, 325)]

    for x,y in ladders:
        SCREEN.blit(ladder_image, (x, y))
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
    y = 680
    velocity = 2
    direction = 0

    # Jump varieties
    velocity_jump = 12
    velocity_y = 0
    gravity = 1
    on_ground = True
    y_initial = 100
    player_image = 0

    going_up = False
    going_down = False

    while running:
        SCREEN.fill(Brown)
        SCREEN.blit(palm_image, (0, 0))
        
        # Draw platforms
        draw_platforms(400, 730) # Initial position
        draw_ladders()


        # Check movement in keyboard
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and x >= 430:
            x -= velocity
            direction = 1
            print("x =", x, "y =", y)
            if player_image == 5:
                player_image = 0
            else:
                player_image += 1


        if key[pygame.K_RIGHT] and x <= 1350:
            x += velocity
            direction = 0
            print("x =", x, "y =", y)
            if player_image == 5:
                player_image = 0
            else:
                player_image += 1
        

        # Climbing up
        if key[pygame.K_UP] and ((975 <= x <= 1010 and y == 660) or (1186 <= x <= 1248 and y == 620) or (476 <= x <= 524 and y == 430) or (1084 <= x <= 1136 and y == 300)):
            going_up = True
            player_image = 20


        if going_up == True:
            if ((975 <= x <= 1010 or 1186 <= x <= 1248) and y >= 492):
                y -= 2
            elif (476 <= x <= 524 and y >= 302) or (1084 <= x <= 1136 and y >= 182):
                y -= 2
            else: 
                going_up = False
                player_image = 1
        
        # Climbing down
        if key[pygame.K_DOWN] and ((975 <= x <= 1010 and y == 490) or (1186 <= x <= 1248 and y == 490) or (476 <= x <= 524 and y == 300) or (1084 <= x <= 1136 and y == 180)):
            going_down = True
            player_image = 20


        if going_down == True:
            if (975 <= x <= 1010 and y <= 658) or (1186 <= x <= 1248 and y <= 618):
                y += 2
            elif (476 <= x <= 524 and y <= 428) or (1084 <= x <= 1136 and y <= 298):
                y += 2
            else: 
                going_down = False
                player_image = 1


        y = movement(x, y)

        if player_image == 0 or player_image == 1:
            if direction == 0:
                SCREEN.blit(player_image_1, (x, y))
            else:
                SCREEN.blit(player_image_1_flip, (x, y))
        if player_image == 2 or player_image == 3:
            if direction == 0:
                SCREEN.blit(player_image_2, (x, y))
            else:
                SCREEN.blit(player_image_2_flip, (x, y))
        if player_image == 4 or player_image == 5:
            if direction == 0:
                SCREEN.blit(player_image_3, (x, y))
            else:
                SCREEN.blit(player_image_3_flip, (x, y))
        if player_image == 20:
            SCREEN.blit(player_image_climb, (x, y))

        # Jump
        if key[pygame.K_SPACE] and on_ground:
            y_initial = y
            velocity_y = -velocity_jump
            on_ground = False

        if on_ground == False:
            velocity_y += gravity
            y += velocity_y
            if y == y_initial:
                y_initial = 0
                velocity_y = 0
                on_ground = True

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

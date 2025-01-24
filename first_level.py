import pygame
import sys
import menu
import winning
import losing

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
font_score = pygame.font.SysFont("fonts/donkey.ttf", 50)
font_points = pygame.font.SysFont("fonts/donkey.ttf", 30)

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
princess_image = pygame.image.load("imagenes/Princess.png").convert_alpha()
princess_image = pygame.transform.scale(princess_image, (50, 50))
princess_image = pygame.transform.flip(princess_image, True, False)
barrel_image = pygame.image.load("imagenes/Barrel.png").convert_alpha()
barrel_image = pygame.transform.scale(barrel_image, (25,25))
barrel_images = []
for i in range(0, 72):
    x = 5*i
    barrel_images += [pygame.transform.rotate(barrel_image, x)]

print(len(barrel_images))
monkey_image_1 = pygame.image.load("imagenes/Monkey_1.png").convert_alpha()
monkey_image_1 = pygame.transform.scale(monkey_image_1, (70, 70))
monkey_image_2 = pygame.image.load("imagenes/Monkey_2.png").convert_alpha()
monkey_image_2 = pygame.transform.scale(monkey_image_2, (70, 70))
monkey_image_2 = pygame.transform.flip(monkey_image_2, True, False)

# Button
return_button = {"text": "Regresar", "pos": (WIDTH//2, 860)}

def draw_platforms():
    platforms = [(900, 230), (1000, 230), (1100, 230), (1200, 230), (1300, 230),
    (500, 350), (600, 350), (700, 350), (800, 350), (900, 350), (1000, 350), (1100, 350), (1200, 350), (1300, 350), 
    (400, 460), (500, 480), (600, 500), (700, 520), (800, 540), (900, 540), (1000, 540), (1100, 540), (1200, 540), 
    (1300, 650), (1200, 670), (1100, 690), (1000, 710), (900, 730), (800, 730), (700, 730), (600, 730), (500, 730), (400, 730)]

    for x,y in platforms:
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
    if (963 == x and y == 680) or (1065 == x and y == 660) or (1164 == x and y == 640) or (1257 == x and y == 620) or (x == 492 and y == 430) or (x == 585 and y == 450) or (x == 681 and y == 470) or (x == 777 and y == 490):
        y -= 20
    if (960 == x  and y == 660) or (1062 == x  and y == 640) or (1161 == x  and y == 620) or (1254 == x  and y == 600) or (x == 504 and y == 410) or (x == 591 and y == 430) or (x == 687 and y == 450) or (x == 792 and y == 470):
        y += 20  
    return y

def draw_barrels(barrels):
    new_barrels = []
    adding = True

    for x,y,z in barrels:
        if x != 470 and y == 325:
            x -= 1
            z += 1
            if z == 72:
                z = 0
        elif (x == 470 and 325 <= y < 435) or (625 > y >= 515 and x == 1302):
            y += 1
        elif 515 >= y >= 435 and x != 1302:
            if (x == 500 and 454 >= y >= 435) or (x == 600 and 474 >= y >= 455) or (x == 700 and 494 >= y >= 475) or (x == 800 and 514 >= y >= 495):
                y += 1
            else: 
                x += 1
                z -= 1
                if z == -1:
                    z = 71
        elif 705 >= y >= 435 and x != 400:
            if (x == 975 and 705 > y >= 685) or (x == 1075 and 685 >= y >= 665) or (x == 1175 and 665 >= y >= 645) or (x == 1275 and 645 >= y >= 625):
                y += 1
            else: 
                x -= 1
                z += 1
                if z == 72:
                    z = 0
        if adding == True:
            new_barrels += [(x,y,z)]
            SCREEN.blit(barrel_images[z], (x, y))
        else:
            adding = True

    return new_barrels


# First Level
def first_level():
    running = True
    x = 450
    y = 680
    velocity = 3
    direction = 0

    # Jump varieties
    velocity_jump = 17
    velocity_y = 0
    gravity = 1
    on_ground = True
    y_initial = 100
    player_image = 0

    going_up = False
    going_down = False

    # Score varietis
    score = 0
    current_platform = 0
    next_highest_platform = 1
    n = 40
    scored_jump = False

    # Barrel varieties
    new_barrel = pygame.USEREVENT + 1
    pygame.time.set_timer(new_barrel, 10000) 
    barrels = [(1230, 325, 0)]
    monkey_change = 50

    while running:
        SCREEN.fill(Brown)
        SCREEN.blit(palm_image, (0, 0))
        SCREEN.blit(princess_image, (1200, 180))

        if monkey_change < 50:
            SCREEN.blit(monkey_image_2, (1250, 284))
            monkey_change += 1
        if monkey_change == 50:
            SCREEN.blit(monkey_image_1, (1250, 284))

        # Draw platforms, barrels and ladders
        draw_platforms()
        draw_ladders()
        barrels =  draw_barrels(barrels)

        # Check movement in keyboard
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and x >= 430:
            if x == 474 and y == 300:
                x += 0
            else:
                x -= velocity
            direction = 1
            print("x =", x, "y =", y)
            if player_image == 5:
                player_image = 0
            else:
                player_image += 1


        if key[pygame.K_RIGHT] and x <= 1350:
            if x == 1275 and y == 490:
                x += 0
            else:
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
            current_platform += 1

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
            current_platform -= 1

        if going_down == True:
            if (975 <= x <= 1010 and y <= 658) or (1186 <= x <= 1248 and y <= 618):
                y += 2
            elif (476 <= x <= 524 and y <= 428) or (1084 <= x <= 1136 and y <= 298):
                y += 2
            else: 
                going_down = False
                player_image = 1


        # Player movement
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

        # Draw score
        score_label = font_score.render(f"Puntuación: {score}", True, Tan)
        SCREEN.blit(score_label, (WIDTH//2 - score_label.get_width()//2, 130))

        # Earn points
        if next_highest_platform == current_platform:
            next_highest_platform += 1
            score += 100
            n = 0
        if n < 40:
            if scored_jump == True:
                points = font_points.render("25", True, Tan)
            else:
                points = font_points.render("100", True, Tan)    

            SCREEN.blit(points, (x + 50, y - 50))
            n += 1
        if n == 40:
            scored_jump = False

        # Winning screen
        if x == 1167 and y == 180:
            running = False
            winning.winning(score, 1)

        # Draw return button
        button_rect = menu.draw_button(return_button)

        player_rect = pygame.Rect(x, y, 50, 50)

        for bx, by, bz in barrels:
            barrel_rect = pygame.Rect(bx, by, 25, 25)

            # Colition
            if player_rect.colliderect(barrel_rect):
                running = False
                losing.losing(1)

            # Earn points
            if not on_ground and not scored_jump:
                if abs((x + 25) - (bx + 12)) < 20:
                    if by > y + 80:
                        score += 25
                        scored_jump = True
                        n = 0

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
            if event.type == new_barrel:
                barrels += [(1230, 325, 0)]
                print(barrels)
                monkey_change = 0
                

        pygame.display.flip()
        clock.tick(60)

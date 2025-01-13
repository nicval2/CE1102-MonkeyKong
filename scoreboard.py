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

# Load image
palm_image = pygame.image.load("imagenes/palmeras.png").convert_alpha()
palm_image = pygame.transform.scale(palm_image, (WIDTH, HEIGHT))

# Button
return_button = {"text": "Regresar", "pos": (WIDTH//2, 720)}

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

# Scoreboard
def scoreboard():
    scores = read_scores("scores/highscores.txt")
    running = True
    while running:
        SCREEN.fill(Brown)
        SCREEN.blit(palm_image, (0, 0))

        # Draw title
        title = font_title.render("Salón de la fama", True, Tan)
        SCREEN.blit(title, (WIDTH//2 - title.get_width()//2, 100))

        # Show names
        y_start = 300
        for i, (name, score) in enumerate(scores):
            text = f"{i+1}. {name} - {score}"
            line = font_menu.render(text, True, Tan)
            SCREEN.blit(line, (WIDTH//2 - line.get_width()//2, y_start + i*100))

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

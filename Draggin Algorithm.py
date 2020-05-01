#UMERAHMAD2020

import pygame

# --- constants --- (UPPER_CASE names)

SCREEN_WIDTH = 430
SCREEN_HEIGHT = 410
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
FPS = 30

# --- main ---

# - init -

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# - objects -

circle = pygame.draw.ellipse(screen, (RED), (176, 134, 30, 30))
circle_dragging = False

# - mainloop -

clock = pygame.time.Clock()

running = True

while running:

    # - events -

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:            
                if circle.collidepoint(event.pos):
                    circle_dragging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = circle.x - mouse_x
                    offset_y = circle.y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:            
                circle_dragging = False

        elif event.type == pygame.MOUSEMOTION:
            if circle_dragging:
                mouse_x, mouse_y = event.pos
                circle.x = mouse_x + offset_x
                circle.y = mouse_y + offset_y

    # - draws (without updates) -

    screen.fill(WHITE)
    pygame.draw.ellipse(screen, RED, circle)
    pygame.display.flip()

    # - constant game speed / FPS -

    clock.tick(FPS)

# - end -

pygame.quit()

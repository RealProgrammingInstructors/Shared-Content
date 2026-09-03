# -- If using old pygame you must also use Python version 3.13 or older --
# -- pygame-ce works for newer versions of Python only difference is in package install (pip) --
# Imports
import pygame
from game import *

# Variables
global running
clock = pygame.time.Clock()


# ---- Setup
def init():
    global running
    running = True
    set_size(100, 100)
    setup()


# ---- Start
if __name__ == '__main__':
    pygame.init()
    set_defaults()
    init()


# ---- Main Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            key_pressed(event)
        if event.type == pygame.KEYUP:
            key_released(event)

    draw()
    pygame.display.flip()

    # -- Frame Rate
    clock.tick(60)

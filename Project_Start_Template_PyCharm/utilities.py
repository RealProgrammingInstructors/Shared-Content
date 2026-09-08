# -- This page contains helpful functions that make starting a beginner project easier
import math
import random
import pygame

global window_width, window_height, screen, font, font_colour


# ---- Settings Functions
def set_defaults():
    global window_width, window_height, screen, font, font_colour
    window_width = 500
    window_height = 500
    font = pygame.font.SysFont('Arial', 24)
    font_colour = (255, 255, 255)


def set_size(width: int, height: int):
    global window_width, window_height, screen
    window_width = width
    window_height = height
    screen = pygame.display.set_mode((window_width, window_height))


def get_window_width():
    return screen.get_width()


def get_window_height():
    return screen.get_height()


def background(bg_colour: tuple[int, int, int]):
    screen.fill(bg_colour)


# ---- Image Functions
def draw_image(image: pygame.Surface, x: float, y: float):
    screen.blit(image, (x, y))


def load_image(image_path: str):
    image = pygame.image.load(image_path)
    return image


def resize_image(image: pygame.Surface, width: int, height: int):
    image = pygame.transform.scale(image, (width, height))
    return image


def rotate_image(image: pygame.Surface, pos: tuple[int, int], angle: float):
    origin_pos = (0, 0)  # Origin position should be top left of the screen
    image_rect = image.get_rect(topleft=(pos[0] - origin_pos[0], pos[1] - origin_pos[1]))
    offset = pygame.math.Vector2(pos) - image_rect.topleft

    # Pygame's rotate function spins counter-clockwise, so we invert the angle for the math vector
    rotated_offset = offset.rotate_rad(-angle)

    angle_in_degrees = math.degrees(angle)  # converting our Radians Angle to Degrees Angle for image rotation
    rotated_image = pygame.transform.rotate(image, -angle_in_degrees)

    new_top_left = pygame.math.Vector2(pos) - rotated_offset

    rotated_rect = rotated_image.get_rect(topleft=new_top_left)
    screen.blit(rotated_image, rotated_rect)


# ---- Text Functions
def draw_text(text: str, x: int, y: int):
    text_to_draw = font.render(text, True, font_colour)
    screen.blit(text_to_draw, (x, y))


def set_font_size(size: int):
    global font
    font = pygame.font.SysFont('Arial', size)


def set_font_colour(colour: tuple[int, int, int]):
    global font_colour
    font_colour = colour


# ---- Math Functions
def dist(x1: float, y1: float, x2: float, y2: float):
    a = abs(x1 - x2)
    b = abs(y1 - y2)
    c = math.sqrt(a * a + b * b)
    return c


def random_number(min_num: float, max_num: float):
    return random.uniform(min_num, max_num)


# ---- Common Shapes
def rect(x: int, y: int, w: int, h: int, colour: tuple[int, int, int]):
    pygame.draw.rect(screen, colour, (x, y, w, h))


def circle(x: float, y: float, radius: float, colour: tuple[int, int, int]):
    pygame.draw.circle(screen, colour, (x, y), radius)


def ellipse(x: float, y: float, w: int, h: int, colour: tuple[int, int, int]):
    pygame.draw.ellipse(screen, colour, (x, y, w, h))



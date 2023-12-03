# Filename: laser.py

# Function: Model file that contains various laser related functions that essentially implement the weapon system.

# Importing all modules required for proper functioning of the code in this file.

import pygame

# Importing the required code from other modules of the game.

from config import config
from utils.collide import collide
from utils.assets import Assets


class Laser:

    # Initializes the laser system. Inputs such as laser image (for player / enemy) and coorindates can be provided.

    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    # Draws the laser on the screen.

    def draw(self):

        # Makes laser's coordinates centered in the sprite.

        Assets.image.draw(
            self.img, (config.starting_x + self.x, self.y), True, True)

    # Propagates the laser across the screen with the specified velocity.

    def move(self, vel):
        self.y += vel

    # Defines what happens to the laser when it goes off-screen. 

    def off_screen(self, height):
        return not(height >= self.y >= 0)

    # Defines what happens to the laser when it collides with the player. Essentially, it reduces the player health acc. to laser type.

    def collision(self, obj):
        return collide(self, obj)

    # Defines the height and width of the laser beam.

    def get_width(self):
        return self.img.get_width()

    def get_height(self):
        return self.img.get_height()

# Filename: config.py

# Function: Configuration file that contains parameters for various settings that the game uses.

# Importing all modules required for proper functioning of the code in this file.

import pygame
import os
import ctypes

# Importing the required code from other modules of the game.

from utils.resource_path import resource_path

# Configuration parameters are defined below. 

# First one sets the title of the game window and a default resolution in-case automatic resolution detection by pygame fails.

class Config:
    def __init__(self):
        
        self.TITLE = 'Space Impact'
        self.WIDTH = 750
        self.HEIGHT = 750

        # Loads the background image (i.e. image of space) from /assets/graphics.

        self.backgroundImage = pygame.image.load(resource_path(
            os.path.join('assets', 'graphics', 'background-black-wide.png')))

        # Function that returns the width and height of the screen pixels as a two-integer tuple.

        windows_user = ctypes.windll.user32
        self.monitor_size = (windows_user.GetSystemMetrics(0),
                             windows_user.GetSystemMetrics(1))

        # Sets the dimension for the background image based on the resolution retrieved by previous function.

        self.BG = pygame.transform.scale(
            self.backgroundImage, self.monitor_size)

        # Sets the default framerate to 60 FPS for a smooth gameplay experience.

        self.FPS = 60
        self.clock = pygame.time.Clock()

        # Initializes a window / screen that is resizable with 750 x 750 resolution by default. 

        self.CANVAS = pygame.display.set_mode(
            (self.WIDTH, self.HEIGHT), pygame.RESIZABLE)

        # Gets the width & height of the window in case it is resized. Achieved by calculating the rectangular area of the surface.

        self.screen_rect = self.CANVAS.get_rect()
        self.center_x = self.screen_rect.centerx
        self.starting_x = 0
        self.ending_x = self.WIDTH

        self.center_y = self.screen_rect.centery
        self.starting_y = 0
        self.ending_y = self.HEIGHT
        

    # Updates the width and height of the window such that it can scale dynamically (windowed -> full screen, for example).
    # Also responsible for resizing the background image used from 16:9 to 1:1 in case the window is resized. 
    # This is a fast scale operation that does not sample the results.

    def update(self, width, height):
        self.CANVAS = pygame.display.set_mode(
            (width, height), pygame.RESIZABLE)
        self.WIDTH = width
        self.HEIGHT = height
        self.center_x = width//2
        self.center_y = height//2
        self.ending_x = width
        self.ending_y = height
        self.BG = pygame.transform.scale(
            self.backgroundImage, (self.WIDTH, self.HEIGHT))


config = Config()

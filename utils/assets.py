# Filename: assets.py

# Function: Utility file that defines various functions used by asset files, including rendering, drawing and scaling..

# Importing all modules required for proper functioning of the code in this file.

import pygame
import os

# Importing the required code from other modules of the game.

from utils.resource_path import resource_path
from config import config

# Defines various functions used by graphic/audio assets.

class Assets:
    class text:
        
        # The below function is used to render text on the screen. Inputs to be provided are the text, font name and color.
        
        def render(text, font, color):
            return font.render(text, 1, color)

        # The below function is used to draw text on screen with position. Inputs to be provided are the text, font name and color.
        # Position can be specified using coorindates or set (x,y) values from the center using isCenterX and isCenterY.

        def draw(text, font, color, pos, isCenterX=False, isCenterY=False, underline=False):
            text_label = font.render(text, 1, color)

            # Defines how to calculate position if isCenterX and isCenterY is provided as input.
            
            if isCenterX:
                pos = (pos[0] - text_label.get_width()//2, pos[1])
            if isCenterY:
                pos = (pos[0], pos[1] - text_label.get_height()//2)

            if underline:

                # Draws a straight line
            
                pygame.draw.line(config.CANVAS, color,
                                 (pos[0], pos[1]+45), (pos[0]+text_label.get_width()-4, pos[1]+45), 7)

            config.CANVAS.blit(text_label, pos)

        # Used to draw a surface with a given label at a given position.

        def drawSurface(label, pos):
            config.CANVAS.blit(label, pos)

    # Various image related functions are defined below.

    class image:

        # Used to load an image file. The root folder containing the file can be specified followed by the complete image path.
        # Returns the resource path to the image

        def load(root_path, image_path):
            return pygame.image.load(resource_path(os.path.join(root_path, image_path)))

        # Used to load an image file and then scale it on the fly (dynamically). 
        # The root folder containing the file can be specified followed by the complete image path and the scale factor.
        # Returns the scaled image.

        def scale(root_path, image_path, factor):
            image = pygame.image.load(resource_path(
                os.path.join(root_path, image_path)))

            return pygame.transform.scale(image, (image.get_width()*factor, image.get_height()*factor))

        # Used to draw image on the screen at a given position. 
        # Position can be specified using coorindates or set (x,y) values from the center using isCenterX and isCenterY.

        def draw(image, pos, isCenterX=False, isCenterY=False):
            if isCenterX:
                pos = (pos[0] - image.get_width()//2, pos[1])
            if isCenterY:
                pos = (pos[0], pos[1] - image.get_height()//2)

            config.CANVAS.blit(image, pos)

    class sound:

        # Used to load audio files required by the game. The root folder containing the audio can be specified followed by the complete path.
        # Returns the audio file. We use mixer, a component provided by pygame to manage audio I/O.

        def load(root_path, sound_path):
            return pygame.mixer.Sound(resource_path(os.path.join(root_path, sound_path)))

    class font:

        # Used to load fonts required by the game. The root folder containing the font can be specified followed by the complete path.

        def load(root_path, font_path):
            return resource_path(os.path.join(root_path, font_path))

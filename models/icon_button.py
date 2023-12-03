# Filename: icon_button.py

# Function: Model file that contains various functions that are used by icon type buttons in-game. This include draw and initialization.

# Importing all modules required for proper functioning of the code in this file.

import pygame

# Importing the required code from other modules of the game.

from constants import Colors, Font
from utils.outlineImage import outlineImage
from utils.assets import Assets

class IconButton:

    # Initializes various button parameters. Input parameters include the image file and text to be included, if any.

    def __init__(self, image, subtitle=''):
        self.image = image
        self.outline = False
        self.subtitle = subtitle
        self.rect = pygame.Rect(
            0, 0, self.image.get_width(), self.image.get_height())

    # Function that draws the button in question. Input include position and size of the button. 
    # Once the parameters are passed, the coordinates to draw are calculated and if outline is required or not.
    # Note: isCenterX and isCenterY can also be used to specify coordinates.
    

    def draw(self, pos, isCenterX=False, isCenterY=False):
        new_pos = pos
        if isCenterX == True:
            new_pos = (new_pos[0] - self.image.get_width()//2, new_pos[1])
        if isCenterY == True:
            new_pos = (new_pos[0], new_pos[1] - self.image.get_height()//2)

        # If an outline is required for the icon, then values can be passed accordingly.

        if self.outline == True:
            outlineImage(self.image, new_pos)

        self.rect = pygame.Rect(
            new_pos[0], new_pos[1], self.image.get_width(), self.image.get_height())

        # Finally, the button is drawn using image.draw()

        Assets.image.draw(self.image, self.rect)

        # Specifices the subtitle font to be used, if there is text present.

        subtitle_font = pygame.font.Font(Font.neue_font, 20)

        # Draws the subtitle text in white color.

        if self.subtitle != '':
            Assets.text.draw(self.subtitle, subtitle_font, Colors.WHITE,
                             (pos[0], pos[1] + 35), True)

    # Returns 'true' if that point is within the bounds of the rectangle. Usually used to implement highlighting of textbox.

    def isOver(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

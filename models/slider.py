# Filename: slider.py

# Function: Model file that implements the slider system found on the settings page.

# Importing the required code from other modules of the game.

from config import config
from constants import Colors

# Importing all modules required for proper functioning of the code in this file.

import pygame

# Initializes all imported pygame modules in a convenient way to get everything started.

pygame.init()

# Loads & initializes font to be used (Verdana of size 12 in this case).

font = pygame.font.SysFont("Verdana", 12)


class Slider():

    # Initializes the slider component. Inputs include start value, position on screen, max. or min. at slider positions left/right.
    def __init__(self, name, val, maxi, mini, pos):
        self.val = val   # Starting value.
        self.maxi = maxi # Maximum value is at slider position right.
        self.mini = mini # Minimum value is at slider position left.
        self.xpos = pos  # At x-coordinate on screen.
        self.ypos = 250  # Specifies the y-coordinate.
        self.surf = pygame.surface.Surface((200, 50))
        self.hit = False  # Hit attribute indicates slider movement due to mouse interaction.

        # Static graphics, which is essentially the slider background.
        pygame.draw.rect(self.surf, Colors.WHITE, [10, 30, 160, 5], 0)

        # Dynamic graphics, which is essentially the button surface.
        self.button_surf = pygame.surface.Surface((20, 20))
        self.button_surf.fill(Colors.TRANS)
        self.button_surf.set_colorkey(Colors.TRANS)
        pygame.draw.circle(self.button_surf, Colors.BLACK, (10, 10), 6, 0)
        pygame.draw.circle(self.button_surf, Colors.WHITE, (10, 10), 4, 0)

    def draw(self):
        
        # Combination of static and dynamic graphics in a copy of the basic slide surface.
        
        # Static
        surf = self.surf.copy()

        # Dynamic
        pos = (10+int((self.val-self.mini)/(self.maxi-self.mini)*100), 33)
        self.button_rect = self.button_surf.get_rect(center=pos)
        surf.blit(self.button_surf, self.button_rect)

        # Moving button box to correct screen position.
        self.button_rect.move_ip(self.xpos, self.ypos)

        # Screen
        config.CANVAS.blit(surf, (self.xpos, self.ypos))

    def move(self):

    # The dynamic part; reacts to movement of the slider button.

        self.val = (pygame.mouse.get_pos()[
                    0] - self.xpos - 10) / 80 * (self.maxi - self.mini) + self.mini
        if self.val < self.mini:
            self.val = self.mini
        if self.val > self.maxi:
            self.val = self.maxi

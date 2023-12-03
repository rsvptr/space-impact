# Filename: outlineImage.py

# Function: Utility file that contains the code to create the while outlines on any interactive object the mouse hovers on.

# Importing all modules required for proper functioning of the code in this file.

import pygame

# Importing the required code from other modules of the game.

from constants import Colors
from utils.assets import Assets

# Outline definition given below.
# Essentially, the code works by providing an input image along with it's position.
# A mask is then generated for the image/button in question.
# We want our outline to be white in color, hence we specify the argument accordingly.
# Finally, we use the draw function to draw the outline at the border of this mask.
# This shows up as the outline on interactive objects like buttons.

def outlineImage(image, pos):
    mask = pygame.mask.from_surface(image)
    mask_outline = mask.outline()
    mask_surf = pygame.Surface(image.get_size())
    for pixel in mask_outline:
        mask_surf.set_at(pixel, Colors.WHITE)
    mask_surf.set_colorkey((0, 0, 0))

    Assets.image.draw(mask_surf, (pos[0], pos[1]+2))
    Assets.image.draw(mask_surf, (pos[0], pos[1]+1))
    Assets.image.draw(mask_surf, (pos[0], pos[1]-1))
    Assets.image.draw(mask_surf, (pos[0], pos[1]-2))
    Assets.image.draw(mask_surf, (pos[0]+2, pos[1]))
    Assets.image.draw(mask_surf, (pos[0]+1, pos[1]))
    Assets.image.draw(mask_surf, (pos[0]-1, pos[1]))
    Assets.image.draw(mask_surf, (pos[0]-2, pos[1]))
    Assets.image.draw(mask_surf, (pos[0]+1, pos[1]+1))
    Assets.image.draw(mask_surf, (pos[0]+1, pos[1]-1))
    Assets.image.draw(mask_surf, (pos[0]-1, pos[1]+1))
    Assets.image.draw(mask_surf, (pos[0]-1, pos[1]-1))

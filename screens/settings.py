# Filename: settings.py

# Function: This file contains the code required to display the 'Settings' page in the game.

# In the settings page, we only have one option to be modified, which is the volume of the game.

# Importing all modules required for proper functioning of the code in this file.

import pygame
import sys

# Importing the required code from other modules of the game.

from .background import slow_bg_obj
from models.icon_button import IconButton
from models.controls import audio_cfg, display_cfg
from utils.assets import Assets
from config import config
from constants import Image, Font, Colors, Text

# Settings page configuration data begins below. 
# First one specifices & loads the fonts to be used (which is Edit Undo).

def settings():
    settings_title_font = pygame.font.Font(Font.edit_undo_font, 50)
    settings_right_font = pygame.font.Font(Font.edit_undo_font, 50)
    settings_left_font = pygame.font.Font(Font.edit_undo_font, 46)

    # Loads the image for the back button shown on the page.

    go_back_btn = IconButton(Image.GO_BACK_IMAGE)

    # Loads the images for the plus and minus button used to increase / decrease volume.

    plus_btn = IconButton(Image.PLUS_IMAGE)
    minus_btn = IconButton(Image.MINUS_IMAGE)

    # Loop that runs the current screen. Value of run changes to false when game begins, another screen is called or if user quits the game.
    # First command updates the background image (i.e. space) and renders it dynamically.

    run = True
    while run:
        slow_bg_obj.update()
        slow_bg_obj.render()

        # Draws the text 'SETTINGS' in yellow color on top of the screen.
        # Also draws spanner & toolbox icons on the left & right of text respectively.

        Assets.text.draw(Text.SETTINGS, settings_title_font, Colors.YELLOW,
                         (config.center_x, 130), True, False, True)
        Assets.image.draw(Image.TOOLS_IMAGE,
                          (config.center_x - 150, 120), True)
        Assets.image.draw(Image.TOOLBOX_IMAGE,
                          (config.center_x + 150, 129), True)

        # Draws the text 'VOLUME' with green color at (x-160, 240).
        # Also draws the volume value as numbers in white color at (x+155, 240).

        Assets.text.draw('VOLUME', settings_left_font, Colors.GREEN,
                         (config.center_x - 160, 240), True)
        Assets.text.draw(f'{audio_cfg.volume}', settings_right_font, Colors.WHITE,
                         (config.center_x + 155, 240), True)

        # Draws the back button used to go back to the main menu at (x+65, 50).

        go_back_btn.draw((config.starting_x + 65, 50), True, True)

        # Draws the plus and minus buttons used to increase & decrease volumes at (x+235, 230) & (x+70, 260) respectively.

        plus_btn.draw((config.center_x + 235, 260), True, True)
        minus_btn.draw((config.center_x + 70, 260), True, True)

        # The following code given below are present on every screen component to ensure smooth functioning of the game. 

        # They include:

        # (a) Code to set the framerate to 60 FPS.
        # (b) Code to quit the game in case the user presses the 'X' button on window.
        # (c) Code to update the window size and dimensions of the background image in the event user resizes the window.
        # (d) Code to implement various keyboard button functions like modifying volume, quit game, mute, toggling full screen.
        # (e) Code to respond to mouse click events on buttons, set 'run' to false and return to main menu.
        # (f) Code to respond to mouse hover events, set the white outline over interactive objects.

        # Each code block will be highlighted with their corresponding alphabets.

        # Note: Volume is not being displayed at the bottom left corner as in other pages since we're modifying the volume here!

        # (a)
        config.clock.tick(config.FPS)
        pygame.display.flip()

        
        for event in pygame.event.get():

            # (b)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            # (c)
            if event.type == pygame.VIDEORESIZE:
                if not display_cfg.fullscreen:
                    config.update(event.w, event.h)
            
            # (d)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_f:
                    config.update(
                        config.monitor_size[0], config.monitor_size[1])
                    display_cfg.toggle_full_screen()
                if event.key == pygame.K_BACKSPACE:
                    run = False

            # (e)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if go_back_btn.isOver():
                        run = False
                    if plus_btn.isOver():
                        audio_cfg.inc_volume(5)
                    if minus_btn.isOver():
                        audio_cfg.dec_volume(5)

            # (f)
            if event.type == pygame.MOUSEMOTION:
                if go_back_btn.isOver():
                    go_back_btn.outline = True
                else:
                    go_back_btn.outline = False


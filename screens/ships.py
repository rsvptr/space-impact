# Filename: ships.py

# Function: This file contains the code required to display the 'Ships' page in the game.

###########################################################################################

#There are 4 different enemy spaceships in the game. They are:

# 1. Lanius Outrider (Easy)
# Health: 100, Weapon Damage: 10

# 2. Zoltan Interceptor (Medium)
# Health: 100, Weapon Damage: 18

# 3. Slug Instigator (Hard)
# Health: 100, Weapon Damage: 25

# 4. Mantis Battlecruiser (Boss)
# Health: 1980, Weapon Damage: 100

# The user's spacecraft has the following attributes:
# Health: 100, Lives: 5, Weapon Damage: 100

###########################################################################################

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

# Ship page configuration data begins below. 
# First one specifices & loads the fonts to be used (which is Edit Undo and Neue Sans).

def ships():
    ships_title_font = pygame.font.Font(Font.edit_undo_font, 50)
    ships_info_font = pygame.font.Font(Font.neue_font, 22)

    # Loads the image for the back button shown on the page.

    go_back_btn = IconButton(Image.GO_BACK_IMAGE)

    # Loads the image for the heart, which depicts the number of the lives the player's ship has.

    NEW_HEART_IMAGE = pygame.transform.scale(
        Image.HEART_IMAGE, (Image.HEART_IMAGE.get_width()*3/4, Image.HEART_IMAGE.get_height()*3/4))

    # Loop that runs the current screen. Value of run changes to false when game begins, another screen is called or if user quits the game.
    # First command updates the background image (i.e. space) and renders it dynamically
    run = True
    while run:
        slow_bg_obj.update()
        slow_bg_obj.render()

        # Draws the text 'SHIPS' in cyan color on top of the screen with two spaceship icons on either side (L & R) of the text.

        Assets.text.draw(Text.SHIPS, ships_title_font, Colors.CYAN,
                         (config.center_x, 100), True, False, True)
        Assets.image.draw(Image.SHIPS_IMAGE,
                          (config.center_x - 110, 90), True)
        Assets.image.draw(Image.SHIPS_IMAGE_2,
                          (config.center_x + 110, 99), True)

        # Codes given below draws the images of spaceships with their information such as health, weapon damage & name.

        # Name: Lanius Outrider; Health: 100; Damage: 10;

        Assets.image.draw(Image.EASY_SPACE_SHIP,
                          (config.center_x - 270, 210), True)
        Assets.text.draw('Lanius Outrider', ships_info_font, Colors.WHITE,
                         (config.center_x - 210, 195))
        Assets.text.draw('Health: 100', ships_info_font,
                         Colors.GREEN, (config.center_x - 210, 222))
        Assets.text.draw('Damage: 10', ships_info_font,
                         Colors.RED, (config.center_x - 210, 249))

        # Name: Zoltan Interceptor; Health: 100; Damage: 18;

        Assets.image.draw(Image.MEDIUM_SPACE_SHIP,
                          (config.center_x - 270, 295), True)
        Assets.text.draw('Zoltan Interceptor', ships_info_font, Colors.WHITE,
                         (config.center_x - 210, 290))
        Assets.text.draw('Health: 100', ships_info_font,
                         Colors.GREEN, (config.center_x - 210, 317))
        Assets.text.draw('Damage: 18', ships_info_font,
                         Colors.RED, (config.center_x - 210, 344))

        # Name: Slug Instigator; Health: 100; Damage: 25;

        Assets.image.draw(Image.HARD_SPACE_SHIP,
                          (config.center_x - 270, 420), True)
        Assets.text.draw('Slug Instigator', ships_info_font, Colors.WHITE,
                         (config.center_x - 210, 400))
        Assets.text.draw('Health: 100', ships_info_font,
                         Colors.GREEN, (config.center_x - 210, 427))
        Assets.text.draw('Damage: 25', ships_info_font,
                         Colors.RED, (config.center_x - 210, 454))

        # Name: Your Spaceship; Lives: 5; Health: 100; Damage: 100

        Assets.image.draw(Image.PLAYER_SPACE_SHIP,
                          (config.center_x + 260, 270), True)
        Assets.text.draw('Your Spaceship', ships_info_font, Colors.WHITE,
                         (config.center_x + 70, 265))
        for index in range(1, 6):
            Assets.image.draw(
                NEW_HEART_IMAGE, (config.center_x + 45 + 25 * index, 292))
        Assets.text.draw('Health: 100', ships_info_font,
                         Colors.GREEN, (config.center_x + 70, 319))
        Assets.text.draw('Damage: 100', ships_info_font,
                         Colors.RED, (config.center_x + 70, 346))

        # Name: Mantis Battlecruiser; Health: 1980; Damage: 100;

        Assets.image.draw(Image.BOSS_SHIP, (config.center_x, 450), True)
        Assets.text.draw('Mantis Battlecruiser', ships_info_font, Colors.WHITE,
                         (config.center_x + 150, 505))
        Assets.text.draw('Health: 1980', ships_info_font,
                         Colors.GREEN, (config.center_x + 150, 532))
        Assets.text.draw('Damage: 100', ships_info_font,
                         Colors.RED, (config.center_x + 150, 559))

        # Draws the back button used to go back to the main menu at (x+65, 50).

        go_back_btn.draw((config.starting_x + 65, 50), True, True)

        # The following code given below are present on every screen component to ensure smooth functioning of the game. 

        # They include:

        # (a) Code to display the volume information
        # (b) Code to set the framerate to 60 FPS.
        # (c) Code to quit the game in case the user presses the 'X' button on window.
        # (d) Code to update the window size and dimensions of the background image in the event user resizes the window.
        # (e) Code to implement various keyboard button functions like modifying volume, quit game, mute, toggling full screen.
        # (f) Code to respond to mouse click events on buttons, set 'run' to false and return to main menu.
        # (g) Code to respond to mouse hover events, set the white outline over interactive objects.

        # Each code block will be highlighted with their corresponding alphabets.

        # (a)
        audio_cfg.display_volume()

        # (b)
        config.clock.tick(config.FPS)
        pygame.display.flip()

        
        for event in pygame.event.get():

            # (c)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            # (d)
            if event.type == pygame.VIDEORESIZE:
                if not display_cfg.fullscreen:
                    config.update(event.w, event.h)

            # (e)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_m:
                    audio_cfg.toggle_mute()
                if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                    audio_cfg.inc_volume(5)
                if event.key == pygame.K_MINUS:
                    audio_cfg.dec_volume(5)
                if event.key == pygame.K_f:
                    config.update(
                        config.monitor_size[0], config.monitor_size[1])
                    display_cfg.toggle_full_screen()
                if event.key == pygame.K_BACKSPACE:
                    run = False

            # (f)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if go_back_btn.isOver():
                        run = False

            # (g)
            if event.type == pygame.MOUSEMOTION:
                if go_back_btn.isOver():
                    go_back_btn.outline = True
                else:
                    go_back_btn.outline = False

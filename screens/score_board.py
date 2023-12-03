# Filename: score_board.py

# Function: This file contains the code required to display the 'Scoreboard' page in the game.

# The scoreboard contains the scores of every turns played in the game with the number of kills & levels completed.

# Importing all modules required for proper functioning of the code in this file.

import pygame
import sys

# Importing the required code from other modules of the game.

from .background import slow_bg_obj
from models.icon_button import IconButton
from models.controls import audio_cfg, display_cfg
from models.scores import scores
from utils.assets import Assets
from config import config
from constants import Image, Font, Text, Colors

# Scoreboard page configuration data begins below. 
# First one specifices & loads the fonts to be used (which are Edit Undo & Neue Sans).

def score_board():
    score_title_font = pygame.font.Font(Font.edit_undo_font, 50)
    score_font = pygame.font.Font(Font.neue_font, 35)

    # Loads the image for the back button shown on the page.

    go_back_btn = IconButton(Image.GO_BACK_IMAGE)

    # Loop that runs the current screen. Value of run changes to false when game begins, another screen is called or if user quits the game.
    # First command updates the background image (i.e. space) and renders it dynamically.

    run = True
    while run:
        slow_bg_obj.update()
        slow_bg_obj.render()

        # Draws the text 'SCOREBOARD' in green color on top of the screen.
        # Also draws a trophy cup on the right side of text.

        Assets.text.draw(Text.SCOREBOARD, score_title_font, Colors.GREEN,
                         (config.center_x, 90), True, False, True)
        Assets.image.draw(Image.TROPHY_IMAGE, (config.center_x + 160, 90))

        # Draws the text 'You haven't played yet!' in white color at (y=180) if the game is run afresh with no games played so far.

        if len(scores.get_scores()) == 0:
            Assets.text.draw('You haven\'t played yet!', score_font, Colors.CYAN,
                             (config.center_x, 180), True)

        else:

            # Draws the image for the levels, kills and score buttons using files from the assets folder.

            Assets.image.draw(Image.LEVELS_IMAGE,
                              (config.center_x-105, 160), True)
            Assets.image.draw(Image.KILLS_IMAGE,
                              (config.center_x+52, 160), True)
            Assets.image.draw(Image.SCORE_IMAGE,
                              (config.center_x+222, 160), True)

            # If the user has completed all 10 levels and defeated the boss, the trophy cup image is drawn. If not, a skull is drawn.

            for i, item in enumerate(scores.get_top_5()):
                if item['status']:
                    Assets.image.draw(
                        Image.WON_IMAGE, (config.center_x-245, 240 + i*100), True, True)
                else:
                    Assets.image.draw(Image.SKULL_IMAGE_2,
                                      (config.center_x-245, 240 + i*100), True, True)

                # Draws the values of levels, kills & score for each turn in cyan, red and yellow respectively.

                Assets.text.draw(str(item['level']), score_font, Colors.CYAN,
                                 (config.center_x-105, 220 + i*100), True)
                Assets.text.draw(str(item['kills']), score_font, Colors.RED,
                                 (config.center_x+52, 220 + i*100), True)
                Assets.text.draw(str(item['score']), score_font, Colors.YELLOW,
                                 (config.center_x+222, 220 + i*100), True)

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

            

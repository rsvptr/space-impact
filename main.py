# Filename: main.py

# Function: Main program file that is used to launch the game.

# Importing all modules required for proper functioning of the code in this file.

import sys
import pygame
import argparse

# Importing the required code from other modules of the game.

from utils.assets import Assets
from screens.game import game
from screens.controls import controls
from screens.score_board import score_board
from screens.ships import ships
from screens.settings import settings
from screens.background import slow_bg_obj
from models.button import Button
from models.icon_button import IconButton
from models.controls import audio_cfg, display_cfg
from config import config
from constants import Path, Image, Font, Colors, Text

# Parses command line arguments, if any. In this case, it is disabling all audio.

ag = argparse.ArgumentParser()
ag.add_argument('--mute', help='disable all sounds', action='store_true' )
args = vars(ag.parse_args())

# Toggle mute (disable all audio) if the mute argument is passed via command line.

if args['mute']:
    audio_cfg.toggle_mute()

# Used to initializes the font module. This must be initialized before any font related functions can be used.

pygame.font.init()

# If the display has a window title, this function will change the name on the window.

pygame.display.set_caption(config.TITLE)

# Sets the runtime icon the system will use to represent the display window. In this case, we use a 32x32 crop of the player's ship.

pygame.display.set_icon(Image.PLAYER_SPACE_SHIP)


# Execution of program begins here.

def main():

    # Sets various parameters for the two fonts being loaded (such as the font size).

    title_font = pygame.font.Font(Font.edit_undo_font, 60)  # Title font (used to show 'Start Game')
    grp_font = pygame.font.Font(Font.edit_undo_font, 30)  # Group font (used to show 'Designed by RERH - MS Group 4').

    # Plays the menu music.

    audio_cfg.play_music(Path.MENU_MUSIC_PATH)

    # Loads the button images from the assets folder for buttons using images or button color for primitive buttons.
    # In the below list, the 'MOUSE' and 'KEYBOARD' buttons are just white bordered rectangles with text in them.
    # Rest are buttons that loads as images from assets folder.

    mouse_btn = Button(Colors.BACKGROUND_BLACK, Colors.WHITE, 'MOUSE')
    keyboard_btn = Button(Colors.BACKGROUND_BLACK, Colors.WHITE, 'KEYBOARD')
    control_btn = IconButton(Image.CONTROL_IMAGE, Text.CONTROLS)
    ships_btn = IconButton(Image.SHIPS_IMAGE, Text.SHIPS)
    trophy_btn = IconButton(Image.TROPHY_IMAGE, Text.SCOREBOARD)
    settings_btn = IconButton(Image.TOOLBOX_IMAGE, Text.SETTINGS)
    exit_btn = IconButton(Image.EXIT_IMAGE)

    # Loop that runs the current screen. Value of run changes to false when game begins, another screen is called or if user quits the game.

    run = True
    while run:

        # Shows the mouse cursor

        pygame.mouse.set_visible(True)

        # Updates the background image (i.e. space) and renders it dynamically (i.e. screen size changes for example).

        slow_bg_obj.update()
        slow_bg_obj.render()

        # Draws the text 'Designed by RERH - MS Group 4' at (y+250) from the center (x).

        Assets.text.draw(
            'Designed by RERH - MS Group 4',
            grp_font,
            Colors.WHITE,
            (config.center_x, config.center_y + 250),
            True,
            True,
            )

        # Draws the mouse and keyboard buttons at (x-210, y+42) from center of screen.

        mouse_btn.draw((config.center_x - 210, config.center_y + 42), (195, 66))
        keyboard_btn.draw((config.center_x + 15, config.center_y + 42), (195, 66))

        # Draws the text 'Start Game' at (y-10) from the center (x).

        Assets.text.draw(
            'Start Game',
            title_font,
            Colors.WHITE,
            (config.center_x, config.center_y - 10),
            True,
            True,
            )

        # Draws the control page button at (x+10, 53).

        control_btn.draw((config.starting_x + 65, 53), True, True)

        # Draws the scoreboard page button at (x-65, 55).

        trophy_btn.draw((config.ending_x - 65, 55), True, True)

        # Draws the settings page button at (x-65, 165).

        settings_btn.draw((config.ending_x - 65, 165), True, True)

        # Draws the ships page button at (x+65, 165).

        ships_btn.draw((config.starting_x + 65, 165), True, True)

        # Displays the volume at the bottom left of the screen.

        audio_cfg.display_volume()

        # Draws the exit button at (x-65, 165).

        exit_btn.draw((config.ending_x - 75, config.ending_y - 40), True, True)

        # Draws the logo of the game on the top at y=50 from center (x).

        Assets.image.draw(Image.TITLE_LOGO, (config.center_x, 50), True)

        # Updates the content on the entire screen.

        pygame.display.flip()

        # Caps the framerate to 60 for a smooth experience.

        config.clock.tick(config.FPS)

        # Used to quit the game in case user clicks on the 'X' button on the window.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Used to dynamically scale the window if the user uses the maximize button on the window.

            if event.type == pygame.VIDEORESIZE:
                if not display_cfg.fullscreen:
                    config.update(event.w, event.h)

            # Responds to keyboard input events, such as reducing / increasing volume, disabing audio, or toggling full screen.

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    audio_cfg.toggle_mute()
                if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                    audio_cfg.inc_volume(5)
                if event.key == pygame.K_MINUS:
                    audio_cfg.dec_volume(5)
                if event.key == pygame.K_f:
                    config.update(config.monitor_size[0],
                                  config.monitor_size[1])
                    display_cfg.toggle_full_screen()

            # Responds to mouse click events and redirects to different screens depending on the button clicked.

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if mouse_btn.isOver():
                        game(True)
                    if keyboard_btn.isOver():
                        game()
                    if control_btn.isOver():
                        controls()
                    if trophy_btn.isOver():
                        score_board()
                    if ships_btn.isOver():
                        ships()
                    if settings_btn.isOver():
                        settings()
                    if exit_btn.isOver():
                        run = False

            # Responds to mouse hover events and shows a white outline on buttons or any interactive elements the mouse hovers over.

            if event.type == pygame.MOUSEMOTION:
                if mouse_btn.isOver():
                    mouse_btn.outline = True
                else:
                    mouse_btn.outline = False

                if keyboard_btn.isOver():
                    keyboard_btn.outline = True
                else:
                    keyboard_btn.outline = False

                if control_btn.isOver():
                    control_btn.outline = True
                else:
                    control_btn.outline = False

                if trophy_btn.isOver():
                    trophy_btn.outline = True
                else:
                    trophy_btn.outline = False

                if settings_btn.isOver():
                    settings_btn.outline = True
                else:
                    settings_btn.outline = False

                if ships_btn.isOver():
                    ships_btn.outline = True
                else:
                    ships_btn.outline = False

                if exit_btn.isOver():
                    exit_btn.outline = True
                else:
                    exit_btn.outline = False

        # Breaks out of the loop and exits the game if 'Q' or 'ESC' key is pressed.

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE] or keys[pygame.K_q]:
            run = False

        # Takes user to the control information screen when 'C' key is pressed.

        if keys[pygame.K_c]:
            controls()

        # Takes user to the scoreboard screen when 'S' key is pressed.

        if keys[pygame.K_s]:
            score_board()

    # Deactivates the pygame library and then terminates the program with code 0, which indicates successful execution.

    pygame.quit()
    sys.exit(0)


main()

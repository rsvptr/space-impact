# Filename: controls.py

# Function: This file contains the code required to display the 'Controls' page in the game.

# The controls page essentially gives a low-down to new players on how the controls work in the game.
# There are four sets of control that are shown per list. The 'back' and 'next' arrows can be used to navigate b/w them.

# Importing all modules required for proper functioning of the code in this file.

import pygame
import sys

# Importing the required code from other modules of the game.

from .background import slow_bg_obj
from utils.assets import Assets
from models.icon_button import IconButton
from models.controls import audio_cfg, display_cfg
from config import config
from constants import Image, Font, Colors, Text


# Control screen definition begins below.

def controls():

    # Loop that runs the current screen. Value of run changes to false when game begins, another screen is called or if user quits the game.

    run = True

    # As mentioned above, there are 4 sub-sections in this screen which illustrates the controls.
    current_page = 1
    total_pages = 4

    # Loads all the fonts necessary for displaying text on the 'control' screen.

    control_title_font = pygame.font.Font(Font.edit_undo_font, 50)
    control_title_font_2 = pygame.font.Font(Font.edit_undo_font, 45)
    control_title_font_3 = pygame.font.Font(Font.edit_undo_font, 40)
    control_font = pygame.font.Font(Font.neue_font, 40)

    # Loads the 'BACK' button and 'NEXT' button images along with the ARROW to go back to the main menu. 

    go_back_btn = IconButton(Image.GO_BACK_IMAGE)
    back_btn = IconButton(Image.BACK_IMAGE)
    next_btn = IconButton(Image.NEXT_IMAGE)

    # Subscreen 1 - Moving / Aiming
    # Mouse: The ship can be moved in all degrees of freedom supported using a mouse. This is the most efficient way to control.
    # Keyboard: The W, A, S, D or UP, DOWN, LEFT, RIGHT arrows can be used to control the ship. This is a bit tedious.
    def moveControlPage():
        Assets.text.draw('MOVE', control_title_font, Colors.GREEN,
                         (config.center_x-265, 190))
        Assets.text.draw('/ AIM:', control_title_font, Colors.GREEN,
                         (config.center_x-265, 240))

        Assets.text.draw('MOUSE', control_title_font_2, Colors.MAGENTA,
                         (config.center_x+202, 190), True)
        Assets.image.draw(Image.MOUSE, (config.center_x+202, 240), True)

        Assets.text.draw('KEYBOARD', control_title_font_2, Colors.MAGENTA,
                         (config.center_x-265, 380))
        Assets.text.draw('OR', control_font, Colors.WHITE,
                         (config.center_x-20, 445), True)
        Assets.image.draw(Image.WASD_KEYS, (config.center_x-280, 440))
        Assets.image.draw(Image.ARROW_KEYS, (config.center_x+30, 440))

    # Subscreen 2 - Shooting
    # Mouse: Left click fires the onboard laser weapon.
    # Keyboard: Spacebar fires the onboard laser weapon.

    def shootControlPage():
        Assets.text.draw('Shoot:', control_title_font, Colors.YELLOW,
                         (config.center_x-265, 190))

        Assets.text.draw('MOUSE', control_title_font_2, Colors.CYAN,
                         (config.center_x+202, 190), True)
        Assets.image.draw(Image.LEFT_MOUSE_CLICK,
                          (config.center_x+202, 240), True)

        Assets.text.draw('KEYBOARD', control_title_font_2, Colors.CYAN,
                         (config.center_x-265, 380))
        Assets.image.draw(Image.SPACEBAR_KEY, (config.center_x-20, 470))
        Assets.text.draw('SPACEBAR', control_font, Colors.WHITE,
                         (config.center_x-265, 460))

    # Category 3 - Returning back home
    # Mouse: Right click can be used to return to the main menu.
    # Keyboard: Backspace can be used to return to the main menu.

    def returnControlPage():
        Assets.text.draw('RETURN BACK', control_title_font, Colors.MAGENTA,
                         (config.center_x-265, 190))
        Assets.text.draw('TO HOME:', control_title_font, Colors.MAGENTA,
                         (config.center_x-265, 240))

        Assets.text.draw('MOUSE', control_title_font_2, Colors.ORANGE,
                         (config.center_x+202, 190), True)
        Assets.image.draw(Image.RIGHT_MOUSE_CLICK,
                          (config.center_x+202, 240), True)

        Assets.text.draw('KEYBOARD', control_title_font_2, Colors.ORANGE,
                         (config.center_x-265, 380))
        Assets.image.draw(Image.BACKSPACE_KEY, (config.center_x-20, 470))
        Assets.text.draw('BACKSPACE', control_font, Colors.WHITE,
                         (config.center_x-265, 460))
    
    # Subscreen 4 - Miscellaneous Controls
    # + / - keys - increase / decrease audio.
    # M key - Disable audio (mute).
    # P key - Pause game.
    # F - Toggle fullscreen.

    def otherControlsPage():
        Assets.text.draw('VOLUME UP/DOWN:', control_title_font_3, Colors.GREEN,
                         (config.center_x-265, 200))
        Assets.image.draw(Image.PLUS_KEY,
                          (config.center_x+122, 190), True)
        Assets.image.draw(Image.MINUS_KEY,
                          (config.center_x+202, 190), True)

        Assets.text.draw('MUTE', control_title_font_3, Colors.GREEN,
                         (config.center_x-265, 290))
        Assets.image.draw(Image.M_KEY,
                          (config.center_x+162, 280), True)
        Assets.text.draw('PAUSE GAME', control_title_font_3, Colors.GREEN,
                         (config.center_x-265, 375))
        Assets.image.draw(Image.P_KEY,
                          (config.center_x+162, 365), True)
        Assets.text.draw('TOGGLE FULLSCREEN', control_title_font_3, Colors.GREEN,
                         (config.center_x-265, 460))
        Assets.image.draw(Image.F_KEY,
                          (config.center_x+162, 450), True)

    # Used to display the slow-scrolling background image

    while run:
        slow_bg_obj.update()
        slow_bg_obj.render()

        match current_page:
            case 1:
                moveControlPage()
            case 2:
                shootControlPage()
            case 3:
                returnControlPage()
            case 4:
                otherControlsPage()

        # Draws the back and next buttons on the screen.
        
        Assets.text.draw(Text.CONTROLS, control_title_font, Colors.ORANGE,
                         (config.center_x, 100), True, False, True)
        Assets.image.draw(Image.CONTROL_IMAGE, (config.center_x + 125, 90))

        go_back_btn.draw((config.starting_x + 65, 50), True, True)
        back_btn.draw(
            (config.center_x-Image.BACK_IMAGE.get_width()-30, config.ending_y-125))
        next_btn.draw((config.center_x + 30, config.ending_y - 125))

        # The following code given below are present on every screen component to ensure smooth functioning of the game. 

        # They include:

        # (a) Code to display the volume information
        # (b) Code to set the framerate to 60 FPS.
        # (c) Code to quit the game in case the user presses the 'X' button on window.
        # (d) Code to update the window size and dimensions of the background image in the event user resizes the window.
        # (e) Code to implement various keyboard button functions like modifying volume, quit game, mute, toggling full screen.
        # (f) Code to respond to mouse click events on buttons, set 'run' to false and return to main menu and switch between screens if the NEXT or BACK buttons are pressed.
        # (g) Code to respond to mouse hover events, set the white outline over interactive objects.

        # Each code block will be highlighted with their corresponding alphabets.

        # (a)
        audio_cfg.display_volume()

        # (b)
        pygame.display.flip()
        config.clock.tick(config.FPS)

        # (c)
        for event in pygame.event.get():
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
                    if back_btn.isOver():
                        if current_page == 1:
                            current_page = 1
                        else:
                            current_page -= 1
                    if next_btn.isOver():
                        if current_page == total_pages:
                            current_page = total_pages
                        else:
                            current_page += 1

            # (g)
            if event.type == pygame.MOUSEMOTION:
                if go_back_btn.isOver():
                    go_back_btn.outline = True
                else:
                    go_back_btn.outline = False

                if back_btn.isOver():
                    back_btn.outline = True
                else:
                    back_btn.outline = False

                if next_btn.isOver():
                    next_btn.outline = True
                else:
                    next_btn.outline = False

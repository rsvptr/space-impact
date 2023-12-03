# Filename: constants.py

# Function: Constants file that contains paths to various assets that are used in-game (such as buttons, spaceship and so on).

# Importing all modules required for proper functioning of the code in this file.

import pygame
import os

# Importing the required code from other modules of the game.

from utils.resource_path import resource_path
from utils.assets import Assets

# Array that holds the list of all sounds used in the game.

soundList = []

# Initializes the in-built sound module provided by pygame. 

pygame.mixer.init()

# Specifies the folders where various assets are present. 
# Fonts are present in /assets/fonts/
# Images (like arrows, buttons, spaceships, icons, logos) are present in /assets/graphics/
# Explosion sequence PNG files are present in /assets/graphics/explosion
# Audio files are present in /assets/sounds/

class Path:
    FONT_PATH = os.path.join('assets', 'fonts')
    EXPLOSION_PATH = os.path.join('assets', 'graphics', 'explosion')
    GRAPHICS_PATH = os.path.join('assets', 'graphics')
    SOUND_PATH = os.path.join('assets', 'sounds')

    # Loads the menu and in-game music files.

    GAME_MUSIC_PATH = resource_path(os.path.join(SOUND_PATH, 'ingame.wav'))
    MENU_MUSIC_PATH = resource_path(os.path.join(SOUND_PATH, 'menu.wav'))

# Loads various font files that are used in the game. 
# In our project, we use 3 different fonts:
# (a) Edit Undo BRK
# (b) Karmatic Arcade
# (c) Neue Pixel Sans
# Thanks & credits to all the authors of these fonts for their wonderful creations!

class Font:
    edit_undo_font = Assets.font.load(Path.FONT_PATH, 'edit_undo.ttf')
    neue_font = Assets.font.load(Path.FONT_PATH, 'neue.ttf')
    karmatic_arcade_font = Assets.font.load(Path.FONT_PATH, 'karmatic_arcade.ttf')

# Loads all the graphics files that are used in the game. First one loads the logo of the game, shown on the menu.
class Image:
    TITLE_LOGO = Assets.image.scale(Path.GRAPHICS_PATH, 'title_logo.png', 2/7)   

    # Loads the graphics assets for all enemy spaceships used in the game.

    EASY_SPACE_SHIP = Assets.image.load(Path.GRAPHICS_PATH, 'easy.png')
    MEDIUM_SPACE_SHIP = Assets.image.load(Path.GRAPHICS_PATH, 'medium.png')
    HARD_SPACE_SHIP = Assets.image.load(Path.GRAPHICS_PATH, 'hard.png')
    BOSS_SHIP = Assets.image.load(Path.GRAPHICS_PATH, 'boss.png')

    UFO_SPACE_SHIP = Assets.image.scale(Path.GRAPHICS_PATH, 'ufo.png', 1/7)

    # Loads the graphics assets for the user's spaceship and it's laser weapon.

    PLAYER_SPACE_SHIP = Assets.image.load(
        Path.GRAPHICS_PATH, 'retro-spaceship.png')
    PLAYER_LASER = Assets.image.load(
        Path.GRAPHICS_PATH, 'pixel_laser_cosmic.png')

    # Loads the graphics assets for the enemy spaceship's laser weapons.

    RED_LASER = Assets.image.load(Path.GRAPHICS_PATH, 'pixel_laser_red.png')
    BLUE_LASER = Assets.image.load(Path.GRAPHICS_PATH, 'pixel_laser_blue.png')
    GREEN_LASER = Assets.image.load(
        Path.GRAPHICS_PATH, 'pixel_laser_green.png')
    FLAME_LASER = Assets.image.load(
        Path.GRAPHICS_PATH, 'pixel_laser_flame.png')

    # Load the graphic assets for audio related icons that are used in the game.

    VOL_ICON = Assets.image.load(Path.GRAPHICS_PATH, 'audio.png')
    MUTE_ICON = Assets.image.load(Path.GRAPHICS_PATH, 'mute.png')

    DEMON_ICON = Assets.image.scale(Path.GRAPHICS_PATH, 'demon.png', 1/11)

    # Loads the graphic assets for icons / buttons that appear in the menu (such as settings, scoreboard, controls).

    CONTROL_IMAGE = Assets.image.load(Path.GRAPHICS_PATH, 'joystick.png')
    TROPHY_IMAGE = Assets.image.load(Path.GRAPHICS_PATH, 'trophy.png')
    SHIPS_IMAGE = Assets.image.scale(Path.GRAPHICS_PATH, 'medium.png', 5/6)
    SHIPS_IMAGE_2 = Assets.image.scale(Path.GRAPHICS_PATH, 'hard.png', 3/4)
    TOOLBOX_IMAGE = Assets.image.scale(Path.GRAPHICS_PATH, 'toolbox.png', 1/2)

    TOOLS_IMAGE = Assets.image.scale(Path.GRAPHICS_PATH, 'tools.png', 1/4)
    TOOLS_IMAGE = pygame.transform.rotate(TOOLS_IMAGE, -45)

    GO_BACK_IMAGE = Assets.image.scale(
        Path.GRAPHICS_PATH, 'back_arrow.png', 6/25)

    EXIT_IMAGE = Assets.image.scale(Path.GRAPHICS_PATH, 'exit_button.png', 1/3)

    # Loads the graphic assets for various other icons that are used throughout gameplay (such as scores, pause, lives).

    HEART_IMAGE = Assets.image.scale(Path.GRAPHICS_PATH, 'heart.png', 1)
    STAR_IMAGE = Assets.image.scale(Path.GRAPHICS_PATH, 'star.png', 1/4)
    SKULL_IMAGE = Assets.image.scale(Path.GRAPHICS_PATH, 'skull.png', 1/58)
    SKULL_IMAGE_2 = Assets.image.scale(Path.GRAPHICS_PATH, 'skull.png', 1/54)
    WON_IMAGE = Assets.image.scale(Path.GRAPHICS_PATH, 'won.png', 5/20)

    PLUS_IMAGE = Assets.image.scale(Path.GRAPHICS_PATH, 'plus.png', 1/6)
    MINUS_IMAGE = Assets.image.scale(Path.GRAPHICS_PATH, 'minus.png', 1/6)

    PAUSE_IMAGE = Assets.image.scale(Path.GRAPHICS_PATH, 'pause.png', 2/7)
    PLAY_IMAGE = Assets.image.scale(Path.GRAPHICS_PATH, 'play.png', 2/7)
    PLAY_IMAGE_2 = Assets.image.scale(Path.GRAPHICS_PATH, 'play.png', 1/2.9)

    HOME_IMAGE = Assets.image.scale(Path.GRAPHICS_PATH, 'home.png', 2/5)
    NEXT_IMAGE = Assets.image.scale(Path.GRAPHICS_PATH, 'next_button.png', 1/3)
    BACK_IMAGE = Assets.image.scale(Path.GRAPHICS_PATH, 'back_button.png', 1/3)
    LEVELS_IMAGE = Assets.image.scale(
        Path.GRAPHICS_PATH, 'levels_button.png', 1/3)
    SCORE_IMAGE = Assets.image.scale(
        Path.GRAPHICS_PATH, 'score_button.png', 1/3)
    KILLS_IMAGE = Assets.image.scale(
        Path.GRAPHICS_PATH, 'kills_button.png', 1/3)

    MOUSE = Assets.image.scale(Path.GRAPHICS_PATH, 'mouse.png', 1/2)
    LEFT_MOUSE_CLICK = Assets.image.scale(
        Path.GRAPHICS_PATH, 'left_click_mouse.png', 1/2)
    RIGHT_MOUSE_CLICK = Assets.image.scale(
        Path.GRAPHICS_PATH, 'right_click_mouse.png', 1/2)

    WASD_KEYS = Assets.image.scale(Path.GRAPHICS_PATH, 'wasd_keys.png', 1/2)
    ARROW_KEYS = Assets.image.scale(Path.GRAPHICS_PATH, 'arrow_keys.png', 1/2)
    BACKSPACE_KEY = Assets.image.scale(
        Path.GRAPHICS_PATH, 'backspace_key.png', 1/2)
    SPACEBAR_KEY = Assets.image.scale(
        Path.GRAPHICS_PATH, 'spacebar_key.png', 1/2)
    PLUS_KEY = Assets.image.scale(Path.GRAPHICS_PATH, 'plus_key.png', 1/2)
    MINUS_KEY = Assets.image.scale(Path.GRAPHICS_PATH, 'minus_key.png', 1/2)
    P_KEY = Assets.image.scale(Path.GRAPHICS_PATH, 'p_key.png', 1/2)
    F_KEY = Assets.image.scale(Path.GRAPHICS_PATH, 'f_key.png', 1/2)
    M_KEY = Assets.image.scale(Path.GRAPHICS_PATH, 'mute_key.png', 1/2)

# Loads the audio files associated with various actions (such as the player / enemy firing their laser weapons, explosions and so on).

class Sound:
    PLAYER_LASER_SOUND = Assets.sound.load(Path.SOUND_PATH, 'ownlaser.wav')
    ENEMY_LASER_SOUND = Assets.sound.load(Path.SOUND_PATH, 'enemylaser.wav')
    EXPLODE_SOUND = Assets.sound.load(Path.SOUND_PATH, 'explode.wav')
    LASER_HIT_SOUND = Assets.sound.load(Path.SOUND_PATH, 'laser_hit.wav')


# Adds the list of sounds to the array we declared earlier.

soundList.append(Sound.PLAYER_LASER_SOUND)
soundList.append(Sound.ENEMY_LASER_SOUND)
soundList.append(Sound.EXPLODE_SOUND)
soundList.append(Sound.LASER_HIT_SOUND)

# Defines the RGB color codes for various colors we use througout the game, especially for fonts.

class Colors:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BACKGROUND_BLACK = (7, 8, 16)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    GREEN2 = (0, 209, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    PURPLE = (131, 1, 123)
    ORANGE = (238, 98, 17)
    GREY = (200, 200, 200)
    TRANS = (1, 1, 1)

# Stores text in variables so as to reference them easier.

class Text:
    SHIPS = 'SHIPS'
    SETTINGS = 'SETTINGS'
    CONTROLS = 'CONTROLS'
    SCOREBOARD = 'SCOREBOARD'

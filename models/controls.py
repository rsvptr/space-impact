# Filename: controls.py

# Function: Model file that contains various audio / display related control functions that the game uses.

# This includes adjusting the volume, playing the music, and dynamically scaling to full-screen from windowed and vice-versa.

# Importing all modules required for proper functioning of the code in this file.

import pygame

# Importing the required code from other modules of the game.

from utils.assets import Assets
from config import config
from constants import Image, soundList, Font, Colors

# Audio related control functions defined below.

class AudioControls:

    # Initializes audio settings to default values.

    def __init__(self, soundList):
        self.soundList = soundList
        self.volume = 100
        self.muted = True if self.volume == 0 else False
        self.prev_volume = -1


        pygame.mixer.music.set_volume(self.volume / 100)
        for soundItem in self.soundList:
            soundItem.set_volume(self.volume / 100)

    # Below function is used to set volume level. If it is 0, audio will be disabled.
    # If it is a value greater than 0, mute value is set to false.
    def set_volume(self, level):
        if level == 0:
            self.muted = True
        if self.muted and level > 0:
            self.muted = False
            self.prev_volume = 50  # If you unmute at zero volume, volume level defaults to 50.

        # Volume level is usually set in the range of 0 to 1 for pygame mixer. 
        # Hence, we're converting the level in [0,1] by dividing it with 100.

        self.volume = level
        pygame.mixer.music.set_volume(level / 100)

        # Can be used to dynamically set different volumes for various sound effects.

        for soundItem in soundList:
            soundItem.set_volume(level / 100)
    
    # Function that decreases volume in steps on the settings page.

    def dec_volume(self, amt):
        amt = max(0, self.volume - amt)
        self.set_volume(amt)

    # Function that increases volume in steps on the settings page.

    def inc_volume(self, amt):
        amt = min(100, self.volume + amt)
        self.set_volume(amt)

    # Function that decreases volume in steps on the settings page.
    def toggle_mute(self):
        if self.muted:
            self.set_volume(self.prev_volume)
        else:
            self.prev_volume = self.volume
            self.set_volume(0)
    
    # Function that displays the current volume level.

    def display_volume(self):
        control_font = pygame.font.Font(Font.neue_font, 30)

        # If muted, draw the mute icon. If not muted, draw the volume icon accordingly.
        if self.muted:
            Assets.image.draw(
                Image.MUTE_ICON, (config.starting_x+20, config.ending_y-52))
            vol_lbl_text = " --"
        else:
            Assets.image.draw(
                Image.VOL_ICON, (config.starting_x + 20, config.ending_y - 52))
            vol_lbl_text = str(self.volume).rjust(3, " ")

        Assets.text.draw(vol_lbl_text, control_font, Colors.WHITE,
                         (config.starting_x + 70, config.ending_y - 57))

    # Function used to play music by loading the path.

    def play_music(self, path):
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1)

# Display related functions defined below.

class DisplayControls:

    # Initializes default value (i.e. not full screen).

    def __init__(self):
        self.fullscreen = False

    # Function used to toggle full screen mode, upon which all elements are dynamically scaled to fit the new resized window.
    # If not full screen mode, set window as resizable.

    def toggle_full_screen(self):
        self.fullscreen = not self.fullscreen
        if self.fullscreen:
            config.CANVAS = pygame.display.set_mode(
                config.monitor_size, pygame.FULLSCREEN)
        else:
            config.CANVAS = pygame.display.set_mode(
                (config.WIDTH, config.HEIGHT), pygame.RESIZABLE)


audio_cfg = AudioControls(soundList)
display_cfg = DisplayControls()

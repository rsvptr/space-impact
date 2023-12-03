# Filename: explosion.py

# Function: Model file that defines how explosions work in-game.

# Importing all modules required for proper functioning of the code in this file.

import os
import pygame

# Importing the required code from other modules of the game.

from utils.assets import Assets
from constants import Path, Sound

# Essentially, when it comes to implementing explosions, we have 7 PNG files. These PNG files depict various phases of an explosion.
# When played in a continous fashion, it turns out to be an explosion.
# Initially, we went with a GIF but it had more memory and processing power requirements. Hence the switch.

# Explosion sprite group definition.

explosion_group = pygame.sprite.Group()

# Explosion logic defined below.

class Explosion(pygame.sprite.Sprite):

    # Initializes default values (i.e. number of frames, explosion size)
    # All images are read and stored in array 'images[]'

    def __init__(self, x, y, size=60, num_frames=8):
        super().__init__()
        self.images = []

        # Play from tile1 to tile7 in quick succession.

        for num in range(0, num_frames):
            img = Assets.image.load(Path.EXPLOSION_PATH, f"tile{num:03}.png")
            img = pygame.transform.scale(img, (size, size))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0

        # Plays different sound based on the explosion size (in this case, if size < 40, play different audio).

        if size < 40:
            Sound.LASER_HIT_SOUND.play()
        else:
            Sound.EXPLODE_SOUND.play()

    def update(self):
        explosion_speed = 4

        # Update explosion animation by incrementing counter.

        self.counter += 1

        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        # If the animation is complete, reset animation index for playing again next time an explosion occurs.

        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill()

# Filename: ship.py

# Function: Model that contains all functions, parameters and implementations used by the spaceships.

# Importing all modules required for proper functioning of the code in this file.

import pygame

# Importing the required code from other modules of the game.

from utils.assets import Assets
from models.laser import Laser
from models.explosion import Explosion, explosion_group
from models.controls import audio_cfg
from models.scores import scores
from config import config
from constants import Path, Image, Colors, Sound


class Ship:

    # Initializing required variables that enemy spaceship would use (incl. position, health, ship image file and so on).

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0
        self.CoolDown = 25
        self.boss_max_health = 99
        self.SCORE = 0
        self.KILLS = 0
        self.level = 0

    def draw(self):

        # Draws lasers before the ship so that it doesn't appear like the lasers appear from above the ship

        for laser in self.lasers:
            laser.draw()

        # Makes ship's coordinates centered in the sprite

        Assets.image.draw(
            self.ship_img, (config.starting_x+self.x, self.y), True, True)

    # This is responsible for propagating a fired laser through the screen. Once it goes off-screen, it is removed.
    # If it collides with the player / enemy, it will destroy the enemy / reduce health for player.

    def move_lasers(self, vel, obj):
        self.coolDown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(config.HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    # Defines a cooldown period when enemy ships don't fire lasers. 
    # When it expires, they start firing again.

    def coolDown(self):
        if self.cool_down_counter >= self.CoolDown:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    # Responsible for firing lazer, when the cooldown timer value is set to 0.
    # Plays the laser firing audio and sends the laser image and position to be drawn.

    def shoot(self):
        if self.cool_down_counter == 0:
            Sound.PLAYER_LASER_SOUND.play()
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    # Below two functions are used to get the width and height of the enemy spaceship.

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

    # Below three functions return the current score, kill count and current level.
    # They are usually saved in the scoreboard matrix file.

    def get_score(self):
        return self.SCORE

    def get_kills(self):
        return self.KILLS

    def get_level(self):
        return self.level

    # Used to go to the next level (essentially sets the next level) when the current level is cleared.

    def set_level(self):
        self.level += 1

# Defines various variables related to the player's spaceship (incl. its health, image, laser image, velocity and so on).
class Player(Ship):
    def __init__(self, x, y, health=100, mouse_movement=False):
        super().__init__(x, y, health)
        self.ship_img = Image.PLAYER_SPACE_SHIP
        self.laser_img = Image.PLAYER_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
        self.mouse_movement = mouse_movement
        self.run = True
        self.vel = 5

    # Defines how to respond if the player chooses to use keyboard to play.
    # When the keys are pressed, it responds accordingly by calling the module required.

    def move_with_keyboard(self):
        keys = pygame.key.get_pressed()
        action = {'LEFT': keys[pygame.K_LEFT] or keys[pygame.K_a],
                  'RIGHT': keys[pygame.K_RIGHT] or keys[pygame.K_d],
                  'UP': keys[pygame.K_UP] or keys[pygame.K_w],
                  'DOWN': keys[pygame.K_DOWN] or keys[pygame.K_s],
                  'SHOOT': keys[pygame.K_SPACE],
                  'QUIT': keys[pygame.K_BACKSPACE]}

        # Return to main page
        if action['QUIT']:
            audio_cfg.play_music(Path.MENU_MUSIC_PATH)
            self.run = False
        # Left Key
        if action['LEFT'] and (self.x - self.vel) > self.get_width()/2:
            self.x -= self.vel
        # Right Key
        if action['RIGHT'] and (self.x + self.vel + self.get_width()/2) < config.WIDTH:
            self.x += self.vel
        # Up Key
        if action['UP'] and (self.y - self.vel) > 0:
            self.y -= self.vel
        # Down Key
        if action['DOWN'] and (self.y + self.vel + self.get_height()) < config.HEIGHT:
            self.y += self.vel
        # Shoots Laser
        if action['SHOOT']:
            self.shoot()

    # Defines how to respond if the player chooses to use a mouse to play.

    def move_with_mouse(self):

        # Below variables store information like position of the mouse, when it is pressed and when keys are also pressed.
        cx, cy = pygame.mouse.get_pos()
        button = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()

        # Facilitates movement

        if cx > self.get_width()/2 and cx < config.WIDTH - self.get_width()/2 \
                and cy > 0 and cy < config.HEIGHT:
            self.x = cx
            self.y = cy
        
        # Shoots laser on left click of mouse or using spacebar.

        if button[0] or keys[pygame.K_SPACE]:
            self.shoot()

        # Returns to main menu if the right mouse button or backspace key is pressed.
       

        if button[2] or keys[pygame.K_BACKSPACE]:
            score_obj = {
                "status": False,
                "level": self.get_level(),
                "score": self.get_score(),
                "kills": self.get_kills(),
            }

            # Saves the score data (which includes the levels finished, score and kill count).

            scores.append(False, self.get_level(), self.get_score(), self.get_kills())

            # Plays the menu music upon returning to menu.

            audio_cfg.play_music(Path.MENU_MUSIC_PATH)
            self.run = False
    
    # Stores information about the movement method selected by the user (i.e. Mouse or Keyboard).

    def move(self):
        if(self.mouse_movement):
            self.move_with_mouse()
        else:
            self.move_with_keyboard()

    # Responsible for propaganting the player's laser beam through the screen. 
    # Inputs include velocity and special parameters to distinguish the reward for laser hitting different spaceship.
    def move_lasers(self, vel, objs):
        self.coolDown()
        for laser in self.lasers:
            laser.move(vel)

            # Removes the laser when they go off screen.

            if laser.off_screen(config.HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):

                        # Special reward if boss spaceship is defeated. Adds 1000 score points flat and increases kills by 1.
                        # If it is just a normal spaceship, 50 score points and increases kills 1.

                        if obj.ship_type == 'boss':
                            if self.boss_max_health - 10 <= 0:
                                self.SCORE += 1000
                                self.KILLS += 1
                                objs.remove(obj)
                                self.boss_max_health = 100
                            else:
                                self.boss_max_health -= 10
                        else:
                            self.SCORE += 50
                            self.KILLS += 1

                            # Triggers enemy ship death explosion if laser hits the enemy ship.

                            explosion = Explosion(obj.x, obj.y)
                            explosion_group.add(explosion)
                            objs.remove(obj)

                        if laser in self.lasers:
                            self.lasers.remove(laser)

    # Draws the health bar for the player's spaceship.

    def draw(self):
        super().draw()
        self.healthBar()

    # Defines the behaviour of the health bar for the player's spaceship.
    # It is thing and rectangular in shape. When full, it is green in color.
    # When health is lost, those parts are replaced with red.
    # When health bar becomes empty, a life is deducted and the bar is replenished.

    def healthBar(self):
        x_offset, y_offset = self.ship_img.get_size()
        pygame.draw.rect(config.CANVAS, Colors.RED, (config.starting_x + self.x -
                         x_offset/2, self.y + y_offset/2 + 10, int(self.ship_img.get_width()), 10))
        pygame.draw.rect(config.CANVAS, Colors.GREEN, (config.starting_x + self.x - x_offset/2, self.y +
                         y_offset/2 + 10, int(self.ship_img.get_width() * (self.health/self.max_health)), 10))

# Defines the different types of enemy ships available.

# easy = Lanius Outrider
# medium = Zoltan Interceptor
# hard = Slug Instigator
# boss = Mantis Battlecruiser

class Enemy(Ship):
    TYPE_MODE = {
        'easy': (Image.EASY_SPACE_SHIP, Image.RED_LASER, 10),
        'medium': (Image.MEDIUM_SPACE_SHIP, Image.BLUE_LASER, 18),
        'hard': (Image.HARD_SPACE_SHIP, Image.GREEN_LASER, 25),
        'boss': (Image.BOSS_SHIP, Image.FLAME_LASER, 100)
    }

    ship_type = ''

    # Initializes the same functions as the player's ship had (such as moving the ship, firing the lasers, moving the laser).

    def __init__(self, x, y, ship_type, health=100):
        super().__init__(x, y, health)
        self.ship_type = ship_type
        self.ship_img, self.laser_img, self.damage = self.TYPE_MODE[self.ship_type]
        self.mask = pygame.mask.from_surface(self.ship_img)

    # Moves the ship with velocity defined in 'vel'.

    def move(self, vel):
        self.y += vel

    # Propagates enemy lasers through the screen with velocity specified in 'vel'.
    # Removes the lasers when they go off-screen.
    # If it hits player, display collision, explosion and reduce the health.

    def move_lasers(self, vel, obj):
        self.coolDown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(config.HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):

                # Display collision if enemy laser hits the player.

                sm_explosion = Explosion(laser.x, laser.y, size=30)
                explosion_group.add(sm_explosion)
                obj.health -= self.damage
                self.lasers.remove(laser)

    # Fires the laser. Plays the laser firing audio audio and sets cooldown timer to 1 after firing.
    def shoot(self):
        if self.cool_down_counter == 0 and self.y > 0:
            Sound.ENEMY_LASER_SOUND.play()
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

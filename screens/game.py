# Filename: game.py

# Function: This file contains the code required to display the 'game' screen and implement all gameplay logic.

# Since this file is responsible for the gameplay experience, it is also arguably quite important.
# Here, we define various gameplay logic and mechanics that will be used in the game.

# Importing all modules required for proper functioning of the code in this file.

import pygame
import sys
import time
import random

# Importing the required code from other modules of the game.

from models.ship import Player, Enemy
from models.explosion import Explosion, explosion_group
from models.controls import audio_cfg, display_cfg
from models.scores import scores
from models.icon_button import IconButton
from utils.collide import collide
from utils.assets import Assets
from .background import bg_obj
from config import config
from constants import Path, Image, Font, Colors

# Maintains the state for whether the game is paused or not. Since the game has only begun, pause is set to false initially. 

pause = False

# Loads the play button that shows up on the pause menu, which is used to resume the game.

play_btn = IconButton(Image.PLAY_IMAGE)

# Game screen configuration begins below. 
# Below three variables are for the pause function, hold the user lives information and velocity of the lasers fired.
# In case the user selects the keyboard option, isMouse is set to false. Else, it is set to true in the function call.

def game(isMouse=False):
    global pause
    lives = 5
    laser_vel = 10

    # Sets various parameters for the three fonts being loaded (such as the font size).

    sub_font = pygame.font.Font(Font.neue_font, 40)
    sub_small_font = pygame.font.Font(Font.neue_font, 35)
    pop_up_font = pygame.font.Font(Font.edit_undo_font, 55)

    # Loads and plays the in-game music

    audio_cfg.play_music(Path.GAME_MUSIC_PATH)

    # Arrays that holds details of the enemy type to spawn, their velocity and length of each level.

    enemies = []
    wave_length = 0
    enemy_vel = 1

    # Hide the mouse if player uses it for controlling spaceship. If using keyboard, display mouse.

    player = Player(config.center_x, 585, mouse_movement=isMouse)
    if isMouse == True:
        pygame.mouse.set_visible(False)
    elif isMouse == False:
        pygame.mouse.set_visible(True)

    # Boolean variables that trigger victory, defeat or the boss level.

    lost = False
    win = False
    boss_entry = True

    # Loads the pause button image.

    pause_btn = IconButton(Image.PAUSE_IMAGE)

    # Removes all pygame sprites from the explosion group. 

    explosion_group.empty()

    # Re-draw window function below is used to return to gameplay window in-case any external event is called that changes the same.
    
    def redraw_window():
        bg_obj.update()
        bg_obj.render()

        # Draws the player's ship on-screen using graphics from assets folder.

        player.draw()

        # Draws the enemy spaceships on-screen corresponding to the spaceship name stored in the array defined above.

        for enemyShip in enemies:
            enemyShip.draw()
        
        # If the game is paused, draw the play button at (y=45). If the game is not paused, draw the pause button at (y=45)

        if pause == True:
            play_btn.draw((config.center_x, 45), True, True)
        else:
            pause_btn.draw((config.center_x, 45), True, True)

        # Shows the number of lives the user has by drawing hearts using graphics from assets folder.
        # (Default = 5 lives)

        for index in range(1, lives + 1):
            Assets.image.draw(Image.HEART_IMAGE,
                              (config.starting_x + 37 * index - 7, 30))

        # Draw the current level number in the too-left corner, right below the number of lives (hearts).

        Assets.text.draw(f'{player.get_level()} / 10', sub_small_font, Colors.CYAN,
                         (config.starting_x + 33, 75))

        # Used to move the 'star' icon next to score a bit to the left.
        # This happens once when the score count crosses 100 and then again when it crosses 1000.

        score = player.get_score()
        leftScoreIdx = 0
        if score >= 100 and score < 1000:
            leftScoreIdx = 1
        elif score >= 1000:
            leftScoreIdx = 2

        # Renders & draws the score values as text in green color on the screen, along with the star icon.

        score_label = Assets.text.render(
            f'{score}', sub_font, Colors.GREEN)
        Assets.text.drawSurface(
            score_label, (config.ending_x - score_label.get_width() - 30, 20))
        Assets.image.draw(Image.STAR_IMAGE,
                          (config.ending_x - Image.SKULL_IMAGE.get_width() - 85 - leftScoreIdx*23, 26))

        # Used to move the 'skull' icon next to kill count a bit to the left.
        # This happens once when the score count crosses 100.

        kills = player.get_kills()
        leftKillsIdx = 0
        if kills >= 100:
            leftKillsIdx = 1

        # Renders & draws the skull icon along with the kill count as text in red on the screen.

        Assets.image.draw(Image.SKULL_IMAGE,
                          (config.ending_x - Image.SKULL_IMAGE.get_width() - 85 - leftKillsIdx*15, 82))
        kills_label = Assets.text.render(
            f'{kills}', sub_font, Colors.RED)
        Assets.text.drawSurface(
            kills_label, (config.ending_x - kills_label.get_width() - 30, 75))

        # Display the text 'WINNER :)' if the player clears 10 levels and defeats the boss too.

        if win:
            scores.append(True, player.get_level(), player.get_score(), player.get_kills())
            Assets.text.draw('WINNER :)', pop_up_font, Colors.GREEN,
                             (config.center_x, 350), True)

        # Display the text 'GAME OVER :)' if the player uses up all lives or allows too many enemies to pass through.

        if lost:
            scores.append(False, player.get_level(), player.get_score(), player.get_kills())
            Assets.text.draw('GAME OVER :(', pop_up_font, Colors.RED,
                             (config.center_x, 350), True)

        # Display the text 'BOSS LEVEL!!' if the player clears 10 levels.

        if player.get_level() >= 10 and boss_entry:
            Assets.text.draw('BOSS LEVEL!!', pop_up_font, Colors.RED,
                             (config.center_x, 350), True)

        # Used to draw and update the explosions when player's laser hits an enemy spaceship or vice-versa.

        explosion_group.draw(config.CANVAS)
        explosion_group.update()

        # Code to display the volume information.

        audio_cfg.display_volume()

        # Code to set the framerate to 60 FPS.

        pygame.display.flip()
        config.clock.tick(config.FPS)

    # Below codes contains a bit of game logic. 
    # This includes generating enemies randomly on each level.
    # Each enemy spaceship has a codename - easy, medium, hard and boss.
    # There's also a level length which determines the number of enemies that will be generated (less on lower levels).
    # The requisite function determines the level length and generates the enemies. 
    # When enemy count reaches zero, it advances to next level.

    while player.run:
        redraw_window()
        
        # When health bar reaches zero, deduct a life and refil the health bar. 
        # If the lives reach zero, the 'lost' value is set to 'true' to signal defeat.

        if lives > 0:
            if player.health <= 0:
                lives -= 1
                player.health = 100
        else:
            lost = True
            redraw_window()
            time.sleep(3)
            player.run = False
            pygame.mouse.set_visible(True)
        
        # If player crosses level 10, entry to the boss level is signalled.
        # If player manages to defeat the boss, the 'win' value is set to 'true' to signal victory.

        if player.get_level() == 10 and boss_entry:
            redraw_window()
            time.sleep(2)
            boss_entry = False
        elif player.get_level() > 10:
            win = True
            redraw_window()
            time.sleep(3)
            player.run = False

        # Enemy generation, level length determination and level system function as explained at the top.

        if len(enemies) == 0:
            player.set_level()
            wave_length += 4

            for i in range(wave_length if player.get_level() < 10 else 1):
                enemies.append(Enemy(
                    random.randrange(50, config.WIDTH - 100),
                    random.randrange(-1200, -100),
                    random.choice(['easy', 'medium', 'hard']) if player.get_level() < 10 else 'boss')
                )

        # Code to quit the game in case the user presses the 'X' button on window.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        # Code to update the window size and dimensions of the background image in the event user resizes the window.

            if event.type == pygame.VIDEORESIZE:
                if not display_cfg.fullscreen:
                    config.update(event.w, event.h)

        # Code to respond to mouse click events on buttons and in this case specifically, the pause command.

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if pause_btn.isOver():
                        pygame.mouse.set_visible(True)
                        pause = True
                        redraw_window()
                        paused(player, isMouse)

            # Code to implement various keyboard button functions like modifying volume, quit game, mute, toggling full screen.
            # Also containts code that pauses the game when 'P' key is pressed.

            if event.type == pygame.KEYDOWN:
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
                if event.key == pygame.K_p:
                    pygame.mouse.set_visible(True)
                    pause = True
                    redraw_window()
                    paused(player, isMouse)

        # Moves the player sprite.

        player.move()

        # Implements logic for firing enemy laser weapon system. A set laster velocity is used while range is randomly generated.

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)

            if random.randrange(0, 2 * config.FPS) == 1:
                enemy.shoot()

            # Implements the logic to increase kills & score while reducing health when the player's ship collides with an enemy ship.

            if collide(enemy, player):
                player.SCORE += 50
                player.KILLS += 1
                if enemy.ship_type == 'boss':
                    if enemy.boss_max_health - 5 <= 0:

                        # If the player is able to defeat the boss, it will trigger the boss explosion cutscene, followed by victory.

                        # Note: This is not seen as game is paused as soon as boss health reaches zero.
                        # It is on our TODO list to be fixed. (probably implement a short delay in pausing).

                        # Boss's laser weapons are capable of destroying player's ship in single shot as damage value is 100.

                        boss_crash = Explosion(player.x, player.y, size=100)
                        explosion_group.add(boss_crash)

                        enemies.remove(enemy)
                        enemy.boss_max_health = 100
                        player.health -= 100
                    else:
                        enemy.boss_max_health -= 5
                        player.health -= 100

                        # Triggers the player death explosion.

                        crash = Explosion(player.x, player.y)
                        explosion_group.add(crash)
                else:
                    player.health -= 10
                    crash = Explosion(enemy.x, enemy.y)
                    explosion_group.add(crash)
                    enemies.remove(enemy)
            elif enemy.y + enemy.get_height()/2 > config.HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        player.move_lasers(-laser_vel, enemies)

# Code to implement game pause is given below.
# Game pauses when 'P' key is pressed or when the 'Pause' button on the top is pressed with mouse.
# Player can choose to continue the game or return to the main menu.

def paused(player, isMouse):
    
    # Loads the font that will be used to display text

    main_font = pygame.font.Font(Font.edit_undo_font, 60)

    # Renders and displays the text 'Paused' on the screen in cyan color.

    pause_label = Assets.text.render('Paused', main_font, Colors.CYAN)
    Assets.text.drawSurface(
        pause_label, (config.center_x - pause_label.get_width()//2, 300))

    # Loads the 'home' and 'play' button that is displayed when the game is paused.

    play_2_btn = IconButton(Image.PLAY_IMAGE_2)
    home_btn = IconButton(Image.HOME_IMAGE)

    while pause:

        # Draws the 'home' and 'play' button at (x+66, 400) & (x-84, 400) respectively.

        home_btn.draw((config.center_x+66, 400), True, True)
        play_2_btn.draw((config.center_x-84, 400), True, True)

        # Code to update the window size and dimensions of the background image in the event user resizes the window.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
           
           # Code to respond to mouse click events on buttons. If user right clicks, it returns to main menu. 
           # If user clicks 'play' button, un-pause the game.
           # If user clicks 'home' button, return back to the main menu.

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if play_btn.isOver():
                        if isMouse == True:
                            pygame.mouse.set_visible(False)
                        elif isMouse == False:
                            pygame.mouse.set_visible(True)
                        unpause()
                    if play_2_btn.isOver():
                        if isMouse == True:
                            pygame.mouse.set_visible(False)
                        elif isMouse == False:
                            pygame.mouse.set_visible(True)
                        unpause()
                    if home_btn.isOver():
                        scores.append(False, player.get_level(), player.get_score(), player.get_kills())
                        player.run = False
                        unpause()
                        audio_cfg.play_music(Path.MENU_MUSIC_PATH)

            # Code to implement various keyboard button functions.
            # When 'P' is pressed, the game is paused.
            # When 'backspace is pressed, the game returns to main menu.
            # Also contains code to disable mouse when using it for controlling the spaceship and vice-versa.

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    if isMouse == True:
                        pygame.mouse.set_visible(False)
                    elif isMouse == False:
                        pygame.mouse.set_visible(True)
                    unpause()
                if event.key == pygame.K_BACKSPACE:
                    scores.append(False, player.get_level(), player.get_score(), player.get_kills())
                    player.run = False
                    unpause()

                    # Plays the main menu music.

                    audio_cfg.play_music(Path.MENU_MUSIC_PATH)

        pygame.display.flip()
        config.clock.tick(15)

# Global unpause variable that sets value of 'pause' to 'false'.
def unpause():
    global pause
    pause = False

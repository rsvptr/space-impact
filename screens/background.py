# Filename: background.py

# Function: This file contains code to implement the scrolling background image (i.e. space).

# It can be noted that in almost every screen, there is an image of space that is scrolling, which also dynamically adjusts to scaling.
# This background is implemented by using a pixel art of space, which is stored as a PNG file in the /assets/graphics folder.
# It is to be noted that the images are not directly used here. They are referenced via the function. 
# This file only contains the logic to implement the scrolling and also the dynamic scaling adjustment.

# There are two versions of the scrolling background: one that scrolls at normal speed and another that scrolls 1.5x slower. 
# The former is used in the game screen while the latter is used in the menu & other screens.

# Importing the required code from other modules of the game.

from config import config
from utils.assets import Assets

# In the below portion of code, the referenced image is stored in two different variables. 
# Then, for one, the resolution (bounding window) is calculated using get_rect(). The moving speed is then set.
# The update function then checks if the image has finished scrolling once by checking it's height.
# If it did, it loops the image from the beginning. It is rendered on-screen by the rendering function.

class ScrollBackground():
    def __init__(self, bg_img, moving_speed=3):
        self.bgimage = bg_img
        self.rectBGimg = self.bgimage.get_rect()

        self.bgY1 = 0

        self.bgY2 = - self.rectBGimg.height

        self.moving_speed = moving_speed

    def update(self):
        self.bgY1 += self.moving_speed
        self.bgY2 += self.moving_speed
        if self.bgY1 >= self.rectBGimg.height:
            self.bgY1 = - self.rectBGimg.height
        if self.bgY2 >= self.rectBGimg.height:
            self.bgY2 = - self.rectBGimg.height

    def render(self):
        Assets.image.draw(self.bgimage, (config.center_x, self.bgY1), True)
        Assets.image.draw(self.bgimage, (config.center_x, self.bgY2), True)

# Calls the function with input image and scrolling speed.

bg_obj = ScrollBackground(config.BG)
slow_bg_obj = ScrollBackground(config.BG, 1.5)

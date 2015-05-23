# The MIT License (MIT)

# Copyright (c) 2015 Adam Anh Doan Kim Caramés

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Animation snippet based on https://groups.google.com/d/msg/cocos-discuss/9UTExyiwIDE/HoCm-ZihXoYJ post

# Doge animation based on ZawiasJR's doge spritesheet
# http://www.reddit.com/r/spelunky/comments/1w9yls/i_made_my_first_damsel_mod_doge_sprite_sheet_in/

import cocos
import pyglet
from pyglet.window import key

import utils


class CharacterLayer(cocos.layer.Layer):
    """
        Layer that represents a character and some of its states: Standing, Walking and Running.
    """
    is_event_handler = True
    DOGE_SPRITESHEET_PATH = 'images/doge_spritesheet.png'

    def __init__(self):
        super(CharacterLayer, self).__init__()

        spritesheet_texture = self.__build_doge_spritesheet_texture()

        standing_sprite = spritesheet_texture[9]

        anim_running = pyglet.image.Animation.from_image_sequence(sequence=spritesheet_texture[9:],
                                                                  period=.005,
                                                                  loop=True)
        anim_walking = pyglet.image.Animation.from_image_sequence(sequence=spritesheet_texture[9:],
                                                                  period=.1,
                                                                  loop=True)

        self.add(self.__build_sprite(standing_sprite), name="standing")
        self.add(self.__build_sprite(anim_running), name="running")
        self.add(self.__build_sprite(anim_walking), name="walking")

        self.get("running").do(cocos.actions.Hide())
        self.get("walking").do(cocos.actions.Hide())

        self.scale_x = 1
        self.is_moving = False
        self.keyboard = key.KeyStateHandler()
        cocos.director.director.window.push_handlers(self.keyboard)

    def __build_doge_spritesheet_texture(self):
        raw = pyglet.image.load(utils.get_res_path(self.DOGE_SPRITESHEET_PATH))
        # From a spritesheet image we build an pyglet Image Grid with 2 rows and 9 columns
        grid = pyglet.image.ImageGrid(raw,
                                         rows=2,
                                         columns=9,
                                         item_height=73,
                                         item_width=80,
                                         column_padding=1,
                                         row_padding=25)
        return pyglet.image.TextureGrid(grid)

    @staticmethod
    def __build_sprite(sprite_src):
        sprite = cocos.sprite.Sprite(sprite_src)
        sprite.anchor = 0.5, 0.5
        sprite.position = 50, 50
        return sprite

    def on_key_press(self, _key, _):
        is_looking_left = (self.scale_x == -1) | -1
        left_trigger = self.keyboard[key.LEFT] | (_key == key.LEFT)
        right_trigger = self.keyboard[key.RIGHT] | (_key == key.RIGHT)
        self.is_moving = right_trigger | right_trigger
        running_trigger = self.keyboard[key.LSHIFT] | (_key == key.LSHIFT)

        if left_trigger | right_trigger:
            self.scale_x = is_looking_left*left_trigger | -1*is_looking_left*right_trigger
            self.get("standing").do(cocos.actions.Hide())
            self.get("running"*(not running_trigger) + "walking"*running_trigger).do(cocos.actions.Hide())
            self.get("running"*running_trigger + "walking"*(not running_trigger)).do(cocos.actions.Show())

    def on_key_release(self, _key, _):
        if _key == key.LSHIFT and self.is_moving:
            self.get("running").do(cocos.actions.Hide())
            self.get("walking").do(cocos.actions.Show())

        if (_key == key.RIGHT) | (_key == key.LEFT):
            self.is_moving = False
            self.get("standing").do(cocos.actions.Show())
            self.get("running").do(cocos.actions.Hide())
            self.get("walking").do(cocos.actions.Hide())


class AnimLayer(cocos.layer.Layer):
    def __init__(self):
        super(AnimLayer, self).__init__()
        self.add(CharacterLayer())

if __name__ == "__main__":
    pyglet.resource.path.append('../../../assets/')
    pyglet.resource.reindex()

    cocos.director.director.init(height=100, width=100)
    main_scene = cocos.scene.Scene(AnimLayer())
    cocos.director.director.run(main_scene)

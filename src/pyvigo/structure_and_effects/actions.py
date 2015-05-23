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
#
# Assets used in this code aren't attached to the described copyright.
# In order to use these resources for non free of charge purposes,
# you must ask to their respective authors the usage permission.

from cocos.actions import *
import cocos

import pyglet


class TextLayer(cocos.layer.Layer):
    """
        Layer that setups text labels and apply some actions on these labels
    """
    def __init__(self):
        super(TextLayer, self).__init__()

        window_width, window_height = cocos.director.director.get_window_size()

        label = cocos.text.Label("WoW Python Vigo!",
                                 font_name='Comic Sans MS',
                                 font_size=48,
                                 color=(255, 255, 255, 255),
                                 anchor_x='center',
                                 anchor_y='center')
        label.position = window_width*0.5, window_height*0.2
        label.do(Repeat(JumpTo(label.position, height=100, duration=2)))
        self.add(label, z=1)

        label2 = cocos.text.Label("Dat Scene",
                                  font_name='Comic Sans MS',
                                  font_size=52,
                                  color=(255, 0, 255, 255),
                                  anchor_x='center',
                                  anchor_y='center')
        label2.position = window_width*0.8, window_height*0.8
        label2.do(Repeat(ScaleBy(1.1, 0.2) + Reverse(ScaleBy(1.1, 0.2))))
        self.add(label2, z=1)

        label3 = cocos.text.Label("Such effects",
                                  font_name='Comic Sans MS',
                                  font_size=40,
                                  color=(0, 255, 255, 255),
                                  anchor_x='center',
                                  anchor_y='center')
        label3.position = window_width*0.25, window_height*0.6
        label3.do(Repeat(FadeTo(0, 1) + FadeTo(255, 1)))
        self.add(label3, z=1)


class DogeLayer(cocos.layer.Layer):
    """
        Layer that represents Doge and his jumping sunglasses!
    """
    def __init__(self):
        super(DogeLayer, self).__init__()

        window_width, window_height = cocos.director.director.get_window_size()
        self.position = 0, 100

        sprite = cocos.sprite.Sprite('images/sunglasses.png')
        sprite.scale = 2.5
        sprite.rotation = 6
        sprite.position = window_width*0.5, window_height
        sprite.do(JumpTo((window_width*0.4, window_height*0.6), duration=1) +
                  Repeat(RotateBy(10, 0.6) + Reverse(RotateBy(10, 0.6))))
        self.add(sprite, z=1)

        sprite = cocos.sprite.Sprite('images/doge.jpg')
        sprite.position = window_width*0.5, window_height*0.4
        self.add(sprite, z=0)


if __name__ == '__main__':
    # We configure the base assets dir
    pyglet.resource.path.append('../../../assets/')
    pyglet.resource.reindex()

    # Scenes and layers configuration
    cocos.director.director.init(width=1024, height=768)
    main_scene = cocos.scene.Scene()
    main_scene.add(TextLayer(), z=1)
    main_scene.add(DogeLayer(), z=0)
    cocos.director.director.run(main_scene)


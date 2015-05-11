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

import cocos
import pyglet
from pyglet.window import key


class CharacterLayer(cocos.layer.Layer):
    """
        Layer that represents the character entity.
        It's also responsible of the character movement using triggered key events.
    """
    STEP = 200
    TURBO = 4
    def __init__(self):
        super(CharacterLayer, self).__init__()

        self.keyboard = key.KeyStateHandler()
        cocos.director.director.window.push_handlers(self.keyboard)

        self.sprite = cocos.sprite.Sprite('spaceship.png')
        self.sprite.scale = 3
        self.sprite.position = 320, 240
        self.add(self.sprite)

        # key event helper functions
        self.get_new_pos = lambda actual, dt, state_helper: \
            actual + (dt * self.STEP * state_helper() * self.check_turbo())

        self.get_horizontal_state = lambda: self.keyboard[key.RIGHT] - self.keyboard[key.LEFT]
        self.get_vertical_state = lambda: self.keyboard[key.UP] - self.keyboard[key.DOWN]
        self.check_turbo = lambda: (self.TURBO * self.keyboard[key.LSHIFT]) | 1

        # scheduled update handler for sprite position management
        self.schedule(self.__update__)

    def __update__(self, dt):
        new_x = self.get_new_pos(self.sprite.position[0], dt, self.get_horizontal_state)
        new_y = self.get_new_pos(self.sprite.position[1], dt, self.get_vertical_state)

        self.sprite.position = new_x, new_y

    # functional alternative
    # def __update__(self, dt):
    #    self.sprite.position = tuple(
    #        map(self.get_new_pos,
    #            self.sprite.position,
    #            [dt, dt],
    #            [self.get_horizontal_state, self.get_vertical_state])
    #    )



if __name__ == '__main__':

    # We configure the base assets dir
    pyglet.resource.path.append('../../assets/')
    pyglet.resource.reindex()

    cocos.director.director.init()
    scene = cocos.scene.Scene()
    scene.add(CharacterLayer())
    cocos.director.director.run(scene)


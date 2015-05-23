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
import cocos.collision_model as cm
import cocos.euclid as eu

collision_manager = cm.CollisionManagerGrid(xmin=0.0, xmax=640.0, ymin=0.0, ymax=480.0, cell_width=20, cell_height=20)


class EnemyLayer(cocos.layer.Layer):
    def __init__(self):
        super(EnemyLayer, self).__init__()
        self.__add_enemy('e1', 100, 100, 2)
        self.__add_enemy('e2', 300, 400, 1)
        self.__add_enemy('e3', 100, 400, 1.5)

    def __add_enemy(self, name, x, y, scale):
        sprite = cocos.sprite.Sprite('images/spaceship.png')
        sprite.scale = scale
        sprite.position = x, y
        sprite.btype = 'enemy'

        sprite.on_collide = lambda: self.remove(sprite)
        sprite.cshape = cm.AARectShape(center=eu.Vector2(x, y),
                                       half_width=sprite.image.width*0.5,
                                       half_height=sprite.image.height*0.5)
        self.add(sprite, name=name)

    def draw(self):
        for _, sprite in self.children:
            collision_manager.add(sprite)


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

        self.sprite = cocos.sprite.Sprite('images/spaceship.png')
        self.sprite.scale = 3
        self.sprite.position = 320, 240
        self.sprite.btype = 'player'
        self.sprite.cshape = cm.AARectShape(eu.Vector2(320.0, 240.0),
                                            self.sprite.image.width*0.4,
                                            self.sprite.image.height*0.4)
        self.add(self.sprite)
        collision_manager.add(self.sprite)

        # key event helper functions
        self.get_new_pos = lambda actual, dt, state_helper: \
            actual + (dt * self.STEP * state_helper() * self.check_turbo())

        self.get_horizontal_state = lambda: self.keyboard[key.RIGHT] - self.keyboard[key.LEFT]
        self.get_vertical_state = lambda: self.keyboard[key.UP] - self.keyboard[key.DOWN]
        self.check_turbo = lambda: (self.TURBO * self.keyboard[key.LSHIFT]) | 1

        # scheduled update handler for sprite position management
        self.schedule(self.__update__)

        self._killedEnemies = []

    def __update__(self, dt):
        self.__handle_collisions()
        new_x = self.get_new_pos(self.sprite.position[0], dt, self.get_horizontal_state)
        new_y = self.get_new_pos(self.sprite.position[1], dt, self.get_vertical_state)
        self.sprite.cshape.center = eu.Vector2(new_x, new_y)
        self.sprite.position = new_x, new_y

    def __handle_collisions(self):
        for item in collision_manager.iter_colliding(self.sprite):
            if item.btype == 'enemy':
                self._killedEnemies.append(item)

        for item in self._killedEnemies:
            item.on_collide()
            collision_manager.remove_tricky(item)
        self._killedEnemies.clear()


if __name__ == '__main__':

    # We configure the base assets dir
    pyglet.resource.path.append('../../assets/')
    pyglet.resource.reindex()

    cocos.director.director.init()
    scene = cocos.scene.Scene()
    scene.add(CharacterLayer())
    scene.add(EnemyLayer())
    cocos.director.director.run(scene)

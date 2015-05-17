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
import random as rnd
from cocos.actions import *


class Entity(cocos.sprite.Sprite):

    def __init__(self, image, x=0.0, y=0.0):
        super(Entity, self).__init__(image)
        xmax, ymax = cocos.director.director.get_window_size()
        self.boundaries = (0.0, 0.0, xmax, ymax)
        self.anchor = 0.5, 0.5
        self.position = x, y
        self.center = self.image.width//2, self.image.height//2

    def draw(self):
        if self.x + self.center[0] < self.boundaries[0] or self.x - self.center[0] > self.boundaries[2]:
            self.parent.remove(self)
            return

        if self.y + self.center[1] < self.boundaries[1] or self.y - self.center[1] > self.boundaries[3]:
            self.parent.remove(self)
            return
        super(Entity, self).draw()


class SpawnerLayer(cocos.layer.ColorLayer):

    def __init__(self, image):
        super(SpawnerLayer, self).__init__(r=255, g=255, b=255, a=255)
        self.schedule_interval(callback=self.__spawn__, interval=1)
        self.image = image

    def __spawn__(self, _):
        y = rnd.uniform(10, 400)
        spawned = Entity(self.image, -100, y)
        spawned.scale = rnd.uniform(0.5, 1.5)
        spawned.do(MoveTo((800, y), rnd.randint(1, 8)))
        self.add(spawned)

if __name__ == '__main__':
    pyglet.resource.path.append('../../assets/')
    pyglet.resource.reindex()

    # Scenes and layers configuration
    cocos.director.director.init(width=640, height=480)
    main_scene = cocos.scene.Scene(SpawnerLayer('images/sunglasses.png'))
    cocos.director.director.run(main_scene)


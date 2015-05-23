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

import utils


pyglet.options['audio'] = ('openal', 'silent')


class MultimediaLayer(cocos.layer.Layer):
    """
        Base layer that handles background music player and sound effects
    """
    is_event_handler = True

    def __init__(self):
        super(MultimediaLayer, self).__init__()

        # background music
        music = pyglet.resource.media('music/Matts_Blues.wav')
        player = pyglet.media.Player()
        player.queue(music)
        player.volume = 1
        player.play()

        # sound effects
        self.sounds = {
            key.SPACE: self.__load_static_sound('sounds/Jump.wav'),
            key.LCTRL: self.__load_static_sound('sounds/Laser_Shoot.wav')
        }

    @staticmethod
    def __load_static_sound(path):
        sound_media = pyglet.media.load(utils.get_res_path(path))
        return pyglet.media.StaticSource(sound_media)

    def on_key_press(self, _key, modifiers):
        if _key in self.sounds:
            self.sounds[_key].play().volume = 0.5


if __name__ == '__main__':
    pyglet.resource.path.append('../../../assets/')
    pyglet.resource.reindex()

    cocos.director.director.init(100, 100)
    cocos.director.director.run(cocos.scene.Scene(MultimediaLayer()))

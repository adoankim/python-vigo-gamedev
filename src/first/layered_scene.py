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

# structured style
def create_layer():
    a_layer = cocos.layer.Layer()
    a_label = cocos.text.Label('structured',
                               font_size=30,
                               anchor_x='center',
                               anchor_y='center')
    a_label.position = 320, 240 # x, y
    a_layer.add(a_label)
    return a_layer
    
    
# object oriented style
class MyLayer(cocos.layer.Layer):
    def __init__(self):
        super(MyLayer, self).__init__()        
        a_label = cocos.text.Label('Object oriented',
                                   font_size=40,
                                   anchor_x='center',
                                   anchor_y='center')
        a_label.position = 320, 100  # x, y
        self.add(a_label)
    

if __name__ == '__main__': 
    print('test')
    cocos.director.director.init(width=640, height=480)
    a_scene = cocos.scene.Scene()
    a_scene.add(create_layer(), z=1)
    a_scene.add(MyLayer(), z=0)
    cocos.director.director.run(a_scene)

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
        a_label.position = 320, 100 # x, y
        self.add(a_label)
    

if __name__ == '__main__': 
    print('test')
    cocos.director.director.init(width=640, height=480)
    a_scene = cocos.scene.Scene()
    a_scene.add(create_layer(), z=1)
    a_scene.add(MyLayer(), z=0)
    cocos.director.director.run(a_scene)

import cocos

class HelloWorld(cocos.layer.Layer):
        def __init__(self):
                super(HelloWorld, self).__init__()
                
                label = cocos.text.Label('Hello, world',
                                         font_name='Times New Roman',
                                         font_size=32,
                                         anchor_x='center', anchor_y='center')

                label.position = 320, 240
                self.add(label)

#init and create a window
cocos.director.director.init()

#create HelloWorld instance
hello_layer = HelloWorld()

#create scene that contains HelloWorld layer as child
main_scene = cocos.scene.Scene(hello_layer)

#run the scene
cocos.director.director.run(main_scene)

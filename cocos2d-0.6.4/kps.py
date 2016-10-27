'''
TODO

-scene1: aloita peli
    paina nappia niin peli alkaa

-scene2:
    ruutu, jossa valitaan kivi, sakset tai paperi
    -> cpu valitsee (random), katsotaan voititko
    uusi peli/lopeta -nappi, tallennetaan tulos

-scene3 highscorelista johon pääsee lopeta-napista


'''


import cocos
from cocos.text import Label
from cocos import scene
from cocos.layer import Layer
from cocos.actions import *
from cocos.director import director
from cocos.sprite import Sprite
from pyglet.window.key import symbol_string

def changeScene(scene):
    #director.replace( FadeTransition( scene, duration=2) )
    director.replace(scene)


# StartGame layer #
class StartGame(cocos.layer.Layer):

    is_event_handler = True
    
    def __init__(self):
        super(StartGame, self).__init__()

        label = cocos.text.Label(
            'Start Screen',
            font_name='Helvetica',
            font_size=32,
            anchor_x='center', anchor_y='center'
            )
        label.position = 320, 240
        self.add(label)
               
#


class GameScreen(Layer):

    is_event_handler = True
    
    def __init__(self):
        super(GameScreen, self).__init__()

        x,y = director.get_window_size()
        
        label = cocos.text.Label(
            'Valitse kivi, sakset tai paperi',
            font_name='Helvetica',
            font_size=32,
            anchor_x='center', anchor_y='center'
            )
        label.position = x//2, y-y//10
        self.add(label)

class GameSprites(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super(GameSprites, self).__init__()

        x,y = director.get_window_size()

        self.kivi = Sprite('kps_img/kivi.png')
        self.kivi.position = 120, y-150
        self.add(self.kivi, z=1)
        
        self.sakset = Sprite('kps_img/sakset.png')
        self.sakset.position = 120, y-280
        self.add(self.sakset, z=1)
        
        self.paperi = Sprite('kps_img/paperi.png')
        self.paperi.position = 120, y-410
        self.add(self.paperi, z=1)

    def on_mouse_press(self, x, y, buttons, modifiers):
        print(buttons)
        if buttons == 1:
           #self.kivi.do(Jump(50, 0, 1, 1))
           #self.sakset.do(Jump(50, 0, 1, 1))
           #self.paperi.do(Jump(50, 0, 1, 1))
            print(self)
            

class KeyDisplay(cocos.layer.Layer):

    #layer receives director.window events 
    is_event_handler = True

    def __init__(self):
        super(KeyDisplay,self).__init__()

        self.text = cocos.text.Label('', x=100, y=280)

        #keeps track which keys are pressed
        self.keys_pressed = set()
        self.update_text()
        self.add(self.text)

    def update_text(self):
        key_names = [pyglet.window.key.symbol_string (k) for k in self.keys_pressed]
        text = 'Keys: '+','.join (key_names)
        #update self.text
        self.text.element.text = text

    def on_key_press (self, key, modifiers):
        # """This function is called when a key is pressed.
        #'key' is a constant indicating which key was pressed.
        #'modifiers' is a bitwise or of several constants indicating which
        #modifiers are active at the time of the press (ctrl, shift, capslock, etc.)
        self.keys_pressed.add(key)
        self.update_text()

    def on_key_release(self, key, modifiers):
        
        #constants from pyglet.window.key
        self.keys_pressed.remove(key)
        self.update_text()

    def update_text(self):
        key_names = [pyglet.window.key.symbol_string (k) for k in self.keys_pressed]
        text = 'Keys: '+','.join (key_names)
        #update self.text
        self.text.element.text = text

class MouseDisplay(cocos.layer.Layer):

    is_event_handler = True

    def __init__(self):
        super(MouseDisplay,self).__init__()

        self.posx = 100
        self.posy = 240
        self.text = cocos.text.Label('No mouse events yet', font_size=18, x=self.posx, y=self.posy)
        self.add(self.text)

    def update_text (self, x, y):
        # http://stackoverflow.com/questions/4288973/whats-the-difference-between-s-and-d-in-python-string-formatting
        text = 'Mouse @ %d, %d' % (x,y)
        self.text.element.text = text
        self.text.element.x = self.posx
        self.text.element.y = self.posy

    def on_mouse_motion(self,x,y,dx,dy):
        self.update_text(x,y)
    
    def on_mouse_drag(self,x,y,dx,dy,buttons,modifiers):
        self.update_text(x,y)

    def on_mouse_press(self,x,y,buttons,modifiers):
        self.posx, self.posy = director.get_virtual_coordinates(x,y)
        self.update_text(x,y)
        changeScene(game_scene)




        
director.init()

start_scene = cocos.scene.Scene(StartGame(), KeyDisplay(), MouseDisplay())
game_scene = cocos.scene.Scene(GameScreen(), GameSprites())
director.run(start_scene)


import cocos
from cocos.director import director
import pyglet



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

director.init(resizable=True)
director.run(cocos.scene.Scene(KeyDisplay(), MouseDisplay() ))

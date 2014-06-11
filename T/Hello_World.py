import pyglet
from pyglet.window import key, mouse
from pyglet.resource import image as pygImage
from pyglet.resource import media as pygMedia
from pyglet.sprite import Sprite as pygSprite
from pyglet.image import load as LocalImage

class CustomWindow(pyglet.window.Window):
    def __init__(self, IMG, SFX, *args, **kwargs):

        # Grab these for all to see
        self.IMG = IMG
        self.SFX = SFX

        
        # Window size is dynamic with respect to button sizes
        self.max_w = max(
            self.IMG['B01_norm'].width,
            self.IMG['B02_norm'].width,
            self.IMG['B03_norm'].width,
            self.IMG['B04_norm'].width,)
        self.max_h = max(
            self.IMG['B01_norm'].height,
            self.IMG['B02_norm'].height,
            self.IMG['B03_norm'].height,
            self.IMG['B04_norm'].height,)
        win_width = self.max_w * 4
        win_height = self.max_h + self.IMG['B05_norm'].height
        super(CustomWindow, self).__init__(win_width, win_height, caption='Transition()')

        self.set_icon(LocalImage('icon1.png'),LocalImage('icon2.png'))

        # Prep for Sprites
        self.batch = pyglet.graphics.Batch()
        self.layer = [ pyglet.graphics.OrderedGroup(x) for x in xrange(10)]

        # Prep for Buttons
        self.pressed = self.selected = -1

        self.options = [
            pygSprite( self.IMG['B01_norm'],
                       x = 0,
                       y = self.IMG['B05_norm'].height,
                       batch = self.batch,
                       group = self.layer[0]
                       ),
            pygSprite( self.IMG['B02_norm'],
                       x = self.max_w,
                       y = self.IMG['B05_norm'].height,
                       batch = self.batch,
                       group = self.layer[0]
                       ),
            pygSprite( self.IMG['B03_norm'],
                       x = self.max_w *2,
                       y = self.IMG['B05_norm'].height,
                       batch = self.batch,
                       group = self.layer[0]
                       ),
            pygSprite( self.IMG['B04_norm'],
                       x = self.max_w *3,
                       y = self.IMG['B05_norm'].height,
                       batch = self.batch,
                       group = self.layer[0]
                       ),
            ]
        self.save_button = pygSprite( self.IMG['B05_norm'],
                            x = (win_width/2) - (self.IMG['B05_norm'].width/2),
                            y = 0,
                            batch = self.batch, group = self.layer[0])

    def on_mouse_press(self, x, y, button, modifiers):
        # Button 5
        if y < self.IMG['B05_norm'].height:
            with open('saved_settings.txt','w') as f:
                f.write(str(self.selected+1)+'\n')
            self.SFX['go'].play()
            
        # Buttons 1-4
        elif x < self.max_w:    self.press_button(0)
        elif x < self.max_w*2:  self.press_button(1)
        elif x < self.max_w*3:  self.press_button(2)
        elif x < self.max_w*4:  self.press_button(3)

    def on_mouse_release(self, x, y, button, modifiers):
        # If a button is being pressed
        if self.pressed != -1:

            # ...and another button was already selected
            if self.selected != -1:
                # Set that button back to normal FIRST
                self.draw_button(self.selected,'norm')

            # Select it
            self.draw_button(self.pressed,'selec')
            self.selected = self.pressed

    def on_draw(self):
        self.clear()        # Reset
        self.batch.draw()   # Draw Everything

    def press_button(self, which):
        print "PRESSING BUTTON",which
        self.draw_button(which,'press')
        self.pressed = which
        self.SFX['click'].play()
    
    def draw_button(self, which, to_what):
        print "DRAWING BUTTON",which,"TO",to_what
        self.options[which].image = self.IMG['B0'+str(which+1)+'_'+to_what]

def main():
    # CONSTANTS
    IMAGE_FILES = ('B01_norm.png','B01_press.png','B01_selec.png',
                   'B02_norm.png','B02_press.png','B02_selec.png',
                   'B03_norm.png','B03_press.png','B03_selec.png',
                   'B04_norm.png','B04_press.png','B04_selec.png',
                   'B05_norm.png',
                   'icon1.png','icon2.png')
    SOUND_FILES = ('start.wav','go.wav','click.wav')

    # LOAD SOUND EFFECTS
    SFX = {}
    for sound in SOUND_FILES:
        SFX[ sound[:-4] ] = pygMedia(sound, streaming=False)

    # PLAY ASAP
    SFX['start'].play()

    # LOAD IMAGES
    IMG = {}
    for image in IMAGE_FILES:
        IMG[ image[:-4] ] = pygImage(image)

    # LAUNCH WINDOW
    WIN = CustomWindow(IMG, SFX)

    # GOGOGO
    ##WIN.push_handlers(pyglet.window.event.WindowEventLogger())
    pyglet.app.run()

if __name__ == '__main__':
    main()

from distutils import dir_util
from os import path

import pyglet
from pyglet.window import key, mouse
from pyglet.image import load as pygImage
from pyglet.media import load as pygMedia
from pyglet.sprite import Sprite as pygSprite


IMAGE_FILES = ('B01_norm.png','B01_press.png','B01_selec.png',
               'B02_norm.png','B02_press.png','B02_selec.png',
               'B03_norm.png','B03_press.png','B03_selec.png',
               'B04_norm.png','B04_press.png','B04_selec.png',
               'B05_norm.png',
               'icon1.png','icon2.png')
SOUND_FILES = ('start.wav','go.wav','click.wav')
FILE_LOC = ""

class CustomWindow(pyglet.window.Window):
    def __init__(self, IMG, SFX, *args, **kwargs):

        SFX['start'].play()

        # Image and sound libraries
        self.IMG = IMG
        self.SFX = SFX
        
        # Window size is dynamic with respect to button sizes
        #     Grab the largest width
        self.max_w = max(
            self.IMG['B01_norm'].width,
            self.IMG['B02_norm'].width,
            self.IMG['B03_norm'].width,
            self.IMG['B04_norm'].width,)
        #     Grab the largest height
        self.max_h = max(
            self.IMG['B01_norm'].height,
            self.IMG['B02_norm'].height,
            self.IMG['B03_norm'].height,
            self.IMG['B04_norm'].height,)
        #     Our window has 4 buttons across, adjust width to accomodate them
        win_width = self.max_w * 4
        #     Our window is 2 buttons high, adjust height to accomodate them
        win_height = self.max_h + self.IMG['B05_norm'].height
        #     Set the window height accordingly
        super(CustomWindow, self).__init__(win_width, win_height, caption='Transition()')

        # Set the icon
        self.set_icon(
            pygImage( path.join(FILE_LOC,'icon1.png') ),
            pygImage( path.join(FILE_LOC,'icon2.png') ))

        # Prep for Sprites
        self.batch = pyglet.graphics.Batch()
        self.layer = [ pyglet.graphics.OrderedGroup(x) for x in xrange(10)]

        # Draw Buttons
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
        # Button 5 is clicked
        if y < self.IMG['B05_norm'].height:     self.submit(self.selected)
            
        # Buttons 1-4 are clicked
        elif x < self.max_w:    self.press_button(0)
        elif x < self.max_w*2:  self.press_button(1)
        elif x < self.max_w*3:  self.press_button(2)
        elif x < self.max_w*4:  self.press_button(3)

    def on_mouse_release(self, x, y, button, modifiers):
        # If a button was pressed, select it.
        if self.pressed != -1:

            # If another button was already selected, reset it first.
            if self.selected != -1:
                self.draw_button(self.selected,'norm')

            # We've selected whichever button the user was pressing!
            self.draw_button(self.pressed,'selec')
            self.selected = self.pressed

    def on_draw(self):
        self.clear()        # Reset
        self.batch.draw()   # Draw Everything

    def press_button(self, which):
        """ If the user presses one of the 4 buttons """
        self.draw_button(which,'press')
        self.pressed = which
        self.SFX['click'].play()
    
    def draw_button(self, which, to_what):
        """ For changing button visuals. """
        self.options[which].image = self.IMG['B0'+str(which+1)+'_'+to_what]

    def submit(self, selec, playingSFX=True):
        """ Pull files from the selected directory into the target directory. """

        # Confirm button press.
        self.SFX['click'].play()
        
        # Reset to default values first.
        if selec != 0:
            self.submit(0,playingSFX=False)
        
        with open( path.join(FILE_LOC,"write_directories.txt") ,"r") as f:
            # List of directories
            directories = f.read().split("\n")

        # We write to directories[0] from directories[1 + what the user selected]
        dir_util.copy_tree( directories[selec+1], directories[0])

        # The sound file plays after everything's been copied.
        if playingSFX:
            self.SFX['go'].play()
        

if __name__ == '__main__':
    
    # LOAD SOUND EFFECTS
    SFX = {}
    for sound in SOUND_FILES:
        SFX[ sound[:-4] ] = pygMedia( path.join(FILE_LOC, sound), streaming=False)

    # LOAD IMAGES
    IMG = {}
    for image in IMAGE_FILES:
        IMG[ image[:-4] ] = pygImage( path.join(FILE_LOC,image) )

    # LAUNCH WINDOW
    WIN = CustomWindow(IMG, SFX)
    
    ##WIN.push_handlers(pyglet.window.event.WindowEventLogger())
    pyglet.app.run()

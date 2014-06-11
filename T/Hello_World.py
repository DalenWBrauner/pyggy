import pyglet
key, mouse = pyglet.window.key, pyglet.window.mouse
from pyglet.window import key, mouse
from pyglet.resource import image as pygImage
from pyglet.resource import media as pygMedia
from pyglet.sprite import Sprite as pygSprite

# CONSTANTS
IMAGE_FILES = ('B01_norm.png','B01_press.png','B01_selec.png',
               'B02_norm.png','B02_press.png','B02_selec.png',
               'B03_norm.png','B03_press.png','B03_selec.png',
               'B04_norm.png','B04_press.png','B04_selec.png',
               'B05_norm.png')
SOUND_FILES = ('start.wav','go.wav','click.wav')

# LOAD SOUND EFFECTS
SFX = {}
for sound in SOUND_FILES:
    SFX[ sound[:-4] ] = pygMedia(sound, streaming=False)

# LOAD IMAGES
IMG = {}
for image in IMAGE_FILES:
    IMG[ image[:-4] ] = pygImage(image)

# PREP FOR SPRITES
Batch = pyglet.graphics.Batch()
Layer = [ pyglet.graphics.OrderedGroup(x) for x in xrange(10)]

# WINDOW SETUP
WINDOW = pyglet.window.Window()
# Notice: window size is dynamic with image sizes
button_width = max(
    IMG['B01_norm'].width,
    IMG['B02_norm'].width,
    IMG['B03_norm'].width,
    IMG['B04_norm'].width,)
button_height = max(
    IMG['B01_norm'].height,
    IMG['B02_norm'].height,
    IMG['B03_norm'].height,
    IMG['B04_norm'].height,)
win_width = button_width * 4
win_height = button_height + IMG['B05_norm'].height

WINDOW.set_size(win_width, win_height)

# WE'RE GONNA HAVE FUN WITH THIS THING
# Notice: Sprite positions are dynamic with image sizes
buttons4 = [ pygSprite( IMG['B01_norm'],
                        x = 0,
                        y = IMG['B05_norm'].height,
                        batch = Batch,
                        group = Layer[0]
                        ),
             pygSprite( IMG['B02_norm'],
                        x = button_width,
                        y = IMG['B05_norm'].height,
                        batch = Batch,
                        group = Layer[0]
                        ),
             pygSprite( IMG['B03_norm'],
                        x = button_width *2,
                        y = IMG['B05_norm'].height,
                        batch = Batch,
                        group = Layer[0]
                        ),
             pygSprite( IMG['B04_norm'],
                        x = button_width *3,
                        y = IMG['B05_norm'].height,
                        batch = Batch,
                        group = Layer[0]
                        ),
             ]
save_label = pygSprite( IMG['B05_norm'],
                        x = (win_width/2) - (IMG['B05_norm'].width/2),
                        y = 0,
                        batch = Batch,
                        group = Layer[0]
                        )
BEING_PRESSED = None
USER_PREF = -1

SFX['start'].play()

@WINDOW.event
def on_mouse_press(x, y, button, modifiers):
    global BEING_PRESSED
    global USER_PREF
    
    # Button 5
    if y < IMG['B05_norm'].height:
        with open('saved_settings.txt','w') as f:
            f.write(str(USER_PREF)+'\n')
        SFX['go'].play()

    # Button 1
    elif x < button_width:
        buttons4[0].image = IMG['B01_press']
        BEING_PRESSED = 0
        SFX['click'].play()

    # Button 2
    elif x < button_width*2:
        buttons4[1].image = IMG['B02_press']
        BEING_PRESSED = 1
        SFX['click'].play()

    # Button 3
    elif x < button_width*3:
        buttons4[2].image = IMG['B03_press']
        BEING_PRESSED = 2
        SFX['click'].play()

    # Button 4
    elif x < button_width*4:
        buttons4[3].image = IMG['B04_press']
        BEING_PRESSED = 3
        SFX['click'].play()

@WINDOW.event
def on_mouse_release(x, y, button, modifiers):
    global BEING_PRESSED
    global USER_PREF
    
    # If a button is being pressed
    if BEING_PRESSED != None:

        # ...and another button was already selected
        if USER_PREF != -1:
            # Set that button back to normal FIRST
            buttons4[USER_PREF].image = IMG['B0'+str(USER_PREF+1)+'_norm']

        # Select it
        buttons4[BEING_PRESSED].image = IMG['B0'+str(BEING_PRESSED+1)+'_selec']
        USER_PREF = BEING_PRESSED

@WINDOW.event
def on_draw():
    WINDOW.clear()  # Set background color
    Batch.draw()    # Draw ALL the sprites!

#WINDOW.push_handlers(pyglet.window.event.WindowEventLogger())
pyglet.app.run()

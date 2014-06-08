import pyglet
key, mouse = pyglet.window.key, pyglet.window.mouse
from pyglet.window import key, mouse
from pyglet.resource import image as pygImage
from pyglet.resource import media as pygMedia
from pyglet.sprite import Sprite as pygSprite

# CONSTANTS
IMAGE_FILES = ('B_green.png','B_orange.png','B_green90.png','B_orange90.png','L_save.png')
SOUND_FILES = ('boing.wav','coin.wav')

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
button_width = max(( IMG['B_green'].width , IMG['B_orange'].width , IMG['B_orange90'].width , IMG['B_green90'].width ))
button_height = max(( IMG['B_green'].height , IMG['B_orange'].height , IMG['B_orange90'].height , IMG['B_green90'].height))
win_width = button_width * 4
win_height = button_height + IMG['L_save'].height

WINDOW.set_size(win_width, win_height)

# WE'RE GONNA HAVE FUN WITH THIS THING
# Notice: Sprite positions are dynamic with image sizes
buttons4 = [ pygSprite( IMG['B_green'],
                        x = 0,
                        y = IMG['L_save'].height,
                        batch = Batch,
                        group = Layer[0]
                        ),
             pygSprite( IMG['B_orange90'],
                        x = button_width,
                        y = IMG['L_save'].height,
                        batch = Batch,
                        group = Layer[0]
                        ),
             pygSprite( IMG['B_green90'],
                        x = button_width *2,
                        y = IMG['L_save'].height,
                        batch = Batch,
                        group = Layer[0]
                        ),
             pygSprite( IMG['B_orange'],
                        x = button_width *3,
                        y = IMG['L_save'].height,
                        batch = Batch,
                        group = Layer[0]
                        ),
             ]
save_label = pygSprite( IMG['L_save'],
                        x = (win_width/2) - (IMG['L_save'].width/2),
                        y = 0,
                        batch = Batch,
                        group = Layer[0]
                        )




@WINDOW.event
def on_mouse_press(x, y, button, modifiers):
    # Check the y range first.
    if y < IMG['L_save'].height:
        print "SAVE"
    elif x < button_width:
        print 1
    elif x < button_width*2:
        print 2
    elif x < button_width*3:
        print 3
    elif x < button_width*4:
        print 4
    else:
        print "Nope.avi"
        
        
        
##        
##        # If they've actually clicked a buttons, react appropriately.
##        for e in xrange(len(buttons)):
##            if buttons[e].x < x <= buttons[e].x + 76:
##                change_size(e)
##                break
##
##    # If they've clicked the GO/EXPORT button, export a .txt stating the resolution
##    elif  (bttn_y-76) <= y < (bttn_y) and (buttons[-1].x - 224 + 76 <= x <= buttons[-1].x + 76):
##        export_res()
##
##@window.event
##def on_key_press(symbol, modifiers):
##    pass
    pass

@WINDOW.event
def on_draw():
    WINDOW.clear()  # Set background color
    Batch.draw()    # Draw ALL the sprites!

def export():
    print "I'M EXPORTING THINGS I SWEAR"

#WINDOW.push_handlers(pyglet.window.event.WindowEventLogger())
pyglet.app.run()

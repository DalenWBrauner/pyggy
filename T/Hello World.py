import pyglet
key, mouse = pyglet.window.key, pyglet.window.mouse
from pyglet.window import key, mouse
from pyglet.resource import image as pygImage
from pyglet.resource import media as pygMedia
from pyglet.sprite import Sprite as pygSprite

# CONSTANTS
IMAGE_FILES = ('B_green.png','B_orange.png','L_save.png')
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
win_width = IMG['B_green'].width * 4
win_height = IMG['B_green'].height
WINDOW = pyglet.window.Window()
WINDOW.set_size(win_width, win_height)

# WE'RE GONNA HAVE FUN WITH THIS THING
4buttons = [ pygSprite( IMG['B_green'],
                        x = 0,
                        y = 0,
                        batch = Batch,
                        group = Layer[0]
                        ),
             pygSprite( IMG['B_orange'],
                        x = ( win_width/4 ),
                        y = 0,
                        batch = Batch,
                        group = Layer[0]
                        ),
             pygSprite( IMG['B_green'],
                        x = ( win_width/4 ) *2,
                        y = 0,
                        batch = Batch,
                        group = Layer[0]
                        ),
             pygSprite( IMG['B_orange'],
                        x = ( win_width/4 ) *3,
                        y = 0,
                        batch = Batch,
                        group = Layer[0]
                        ),
             ]


# FUNCTIONS
##def change_size(whichRes):
##    '''The user has decided to change their resolution!'''
##    # Play the sound effect
##    sfx.play()
##
##    # Grab the new resolution data
##    newRes = RESOLUTIONS[whichRes]
##    
##    # Set which resolution we're using
##    global current_resolution
##    current_resolution = whichRes
##
##    # Move the buttons to the center of the screen
##    for e in xrange(len(buttons)):
##        buttons[e].x = newRes[0]/2 - 76*len(buttons)/2 + e*76
##        buttons[e].y = newRes[1]/2 - 112   # y
##
##    # Adjust all other sprites accordingly
##    label.x, label.y = buttons[0].x, buttons[0].y
##    new_label.x = new_button.x = buttons[-1].x - 224 + 76
##    new_label.y = new_button.y = buttons[0].y - 76
##
##    # Change the resolution
##    window.set_size(newRes[0],newRes[1])
##
##def export_res():
##    '''The user has decided to save their selection!'''
##    with open('saved_resolution.txt','w') as f:
##        f.write(str(RESOLUTIONS[current_resolution])+'\n')
##    save_sfx.play()

@WINDOW.event
def on_mouse_press(x, y, button, modifiers):
##    # First, check they're even in the right y range.
##    bttn_y = buttons[0].y 
##    if  (bttn_y) <= y <= (bttn_y+224):
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
    print WINDOW.get_size()

@WINDOW.event
def on_draw():
    WINDOW.clear()  # Set background color
    Batch.draw()    # Draw ALL the sprites!

##window.push_handlers(pyglet.window.event.WindowEventLogger())
pyglet.app.run()

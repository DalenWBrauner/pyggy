import pyglet
from pyglet.window import key, mouse

# CONSTANTS
RESOLUTIONS = [(640,480),(800,600),(1024,640),(1024,800),(1080,720),(1280,720),(1680,1050)]

# SETUP
current_resolution = 0
window = pyglet.window.Window()
image0 = pyglet.resource.image("resolution_buttons.png")
image1 = pyglet.resource.image("resolution_button_individual.png")
image2 = pyglet.resource.image("resolution_labels.png")
image3 = pyglet.resource.image("resolution_button_individual_selected_rotated.png")
image4 = pyglet.resource.image("save_label.png")
sfx = pyglet.resource.media('boing.wav', streaming=False)
save_sfx = pyglet.resource.media('coin.wav', streaming=False)

# SPRITE STUFF
batch_of_sprites = pyglet.graphics.Batch()
layer = [ pyglet.graphics.OrderedGroup(x) for x in xrange(2)]
buttons = [ pyglet.sprite.Sprite(image1,
                                 x = 54 + (x*76),
                                 y = 128,
                                 batch = batch_of_sprites,
                                 group = layer[0])
            for x in xrange(len(RESOLUTIONS))]
label = pyglet.sprite.Sprite(image2,
                             x = buttons[0].x, y = 128,
                             batch = batch_of_sprites,
                             group = layer[1])
new_button = pyglet.sprite.Sprite(image3,
                                  x = buttons[-1].x - 224 + 76,
                                  y = buttons[0].y - 76,
                                  batch = batch_of_sprites,
                                  group = layer[0])
new_label = pyglet.sprite.Sprite(image4,
                                 x = new_button.x,
                                 y = new_button.y,
                                 batch = batch_of_sprites,
                                 group = layer[1])



# FUNCTIONS
def change_size(whichRes):
    '''The user has decided to change their resolution!'''
    # Play the sound effect
    sfx.play()

    # Grab the new resolution data
    newRes = RESOLUTIONS[whichRes]
    
    # Set which resolution we're using
    global current_resolution
    current_resolution = whichRes

    # Move the buttons to the center of the screen
    for e in xrange(len(buttons)):
        buttons[e].x = newRes[0]/2 - 76*len(buttons)/2 + e*76
        buttons[e].y = newRes[1]/2 - 112   # y

    # Adjust all other sprites accordingly
    label.x, label.y = buttons[0].x, buttons[0].y
    new_label.x = new_button.x = buttons[-1].x - 224 + 76
    new_label.y = new_button.y = buttons[0].y - 76

    # Change the resolution
    window.set_size(newRes[0],newRes[1])

def export_res():
    '''The user has decided to save their selection!'''
    with open('saved_resolution.txt','w') as f:
        f.write(str(RESOLUTIONS[current_resolution])+'\n')
    save_sfx.play()

@window.event
def on_mouse_press(x, y, button, modifiers):
    # First, check they're even in the right y range.
    bttn_y = buttons[0].y 
    if  (bttn_y) <= y <= (bttn_y+224):
        
        # If they've actually clicked a buttons, react appropriately.
        for e in xrange(len(buttons)):
            if buttons[e].x < x <= buttons[e].x + 76:
                change_size(e)
                break

    # If they've clicked the GO/EXPORT button, export a .txt stating the resolution
    elif  (bttn_y-76) <= y < (bttn_y) and (buttons[-1].x - 224 + 76 <= x <= buttons[-1].x + 76):
        export_res()

##@window.event
##def on_key_press(symbol, modifiers):
##    pass

@window.event
def on_draw():
    window.clear()  # Set background color
    batch_of_sprites.draw()    # Draw ALL the sprites!

#window.push_handlers(pyglet.window.event.WindowEventLogger())
pyglet.app.run()

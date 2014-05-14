import pyglet
from pyglet.window import key, mouse

# CONSTANTS
RESOLUTIONS = [(640,480),(800,600),(1024,640),(1024,800),(1080,720),(1280,720),(1680,1050)]

# SYSTEM SETTINGS
current_resolution = 0
offsets = {'resolution_buttons':[0,0]}
offsets['resolution_buttons'][0] = 640/2 - 266   # x
offsets['resolution_buttons'][1] = 480/2 - 112   # y

# OTHER
window = pyglet.window.Window()
image = pyglet.resource.image("resolution_buttons.png")
label = pyglet.text.Label('Select your resolution',
                          font_name='Arial',
                          font_size=25,
                          x=window.width,
                          y=window.height)
sfx = pyglet.resource.media('chestopen.wav', streaming=False)


# FUNCTIONS
def change_size(whichRes):
    # Play the sound effect
    sfx.play()

    # Grab the new resolution data
    newRes = RESOLUTIONS[whichRes]
    
    # Set which resolution we're using
    CURRENT_RESOLUTION = whichRes

    # Change the offset    
    offsets['resolution_buttons'][0] = newRes[0]/2 - 266   # x
    offsets['resolution_buttons'][1] = newRes[1]/2 - 112   # y

    # Change the resolution
    window.set_size(newRes[0],newRes[1])

##    # Print our result
##    print newRes[0],"x",newRes[1],';',offsets['resolution_buttons']

@window.event
def on_mouse_press(x, y, button, modifiers):
    bttn_x = offsets['resolution_buttons'][0]
    bttn_y = offsets['resolution_buttons'][1]
    if  (bttn_y) <= y <= (bttn_y+224):
        if   (bttn_x + (76*0)) < x <= (bttn_x + (76*1)):   change_size(0)
        elif (bttn_x + (76*1)) < x <= (bttn_x + (76*2)):   change_size(1)
        elif (bttn_x + (76*2)) < x <= (bttn_x + (76*3)):   change_size(2)
        elif (bttn_x + (76*3)) < x <= (bttn_x + (76*4)):   change_size(3)
        elif (bttn_x + (76*4)) < x <= (bttn_x + (76*5)):   change_size(4)
        elif (bttn_x + (76*5)) < x <= (bttn_x + (76*6)):   change_size(5)
        elif (bttn_x + (76*6)) < x <= (bttn_x + (76*7)):   change_size(6)
        

@window.event
def on_key_press(symbol, modifiers):
    pass

@window.event
def on_draw():
    # Set background color
    window.clear()

    # Draw the image at specified position
    image.blit(offsets['resolution_buttons'][0],
               offsets['resolution_buttons'][1])
    
    # Draw the label
    #label.draw()                       # Draw the label onto the window

#window.push_handlers(pyglet.window.event.WindowEventLogger())
pyglet.app.run()

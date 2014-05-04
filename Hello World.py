import pyglet
from pyglet.window import key, mouse

window = pyglet.window.Window()

image = pyglet.resource.image("640x480.png")

label = pyglet.text.Label('Select your resolution',
                          font_name='Arial',
                          font_size=25,
                          x=window.width,
                          y=window.height)

sfx = pyglet.resource.media('chestopen.wav', streaming=False)

@window.event
def on_mouse_press(x, y, button, modifiers):
    s= ''
    if (135 <= y <= 355):
        if   (55 < x <= 130):   s= "600 x 800"
        elif (130 < x <= 207):  s= "640 x 480"
        elif (208 < x <= 285):  s= "Door No.3"
        elif (285 < x <= 360):  s= "Door No.4"
        elif (360 < x <= 435):  s= "Door No.5"
        elif (435 < x <= 511):  s= "Door No.6"
        elif (511 < x <= 590):  s= "Door No.7"
    print s
        

@window.event
def on_key_press(symbol, modifiers):
    pass

@window.event
def on_draw():
    window.clear()          # Set to default background color
    image.blit(0,0)   # Draw the image at specified position
    label.draw()            # Draw the label onto the window

#window.push_handlers(pyglet.window.event.WindowEventLogger())

sfx = pyglet.resource.media('chestopen.wav')

##music = pyglet.resource.media('ez.mp3')
##music.play()

pyglet.app.run()

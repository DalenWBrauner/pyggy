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
    if (135 <= y <= 355):
        if   (55 < x <= 130):
            sfx.play()
            window.set_size(640,480)
            print "640 x 480"
            
        elif (130 < x <= 207):
            sfx.play()
            window.set_size(800, 600)
            print "800 x 600"
            
        elif (208 < x <= 285):
            sfx.play()
            window.set_size(1024, 640)
            print "1024 x 640"
            
        elif (285 < x <= 360):
            sfx.play()
            window.set_size(1024, 800)
            print "1024 x 800"
            
        elif (360 < x <= 435):
            sfx.play()
            window.set_size(1080, 720)
            print "1080 x 720"
            
        elif (435 < x <= 511):
            sfx.play()
            window.set_size(1280, 720)
            print "1280 x 720"
            
        elif (511 < x <= 590):
            sfx.play()
            window.set_size(1680, 1050)
            print "1680 x 1050"
        

@window.event
def on_key_press(symbol, modifiers):
    pass

@window.event
def on_draw():
    window.clear()          # Set to default background color
    image.blit(0,0)   # Draw the image at specified position
#    label.draw()            # Draw the label onto the window

#window.push_handlers(pyglet.window.event.WindowEventLogger())
pyglet.app.run()

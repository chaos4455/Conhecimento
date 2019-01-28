import pyglet

window = pyglet.window.Window()

@window.event
def on_key_press(symbol, modifiers):
    print('Uma tecla foi pressionada')

@window.event
def on_draw():
    window.clear()

pyglet.app.run()
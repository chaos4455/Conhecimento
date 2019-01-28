#importa o modulo pyglet
import pyglet
#cria uma variavel chamada window para o modulo pyglet.window.Window
window = pyglet.window.Window()
#cria uma variavel chamada label que possui um texto e suas especificações
label = pyglet.text.Label('Acorde, Neo',
                          font_name='Times New Roman',
                          font_size=50,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
#cria um evento que gera a janela na tela
@window.event
def on_draw():
#limpa a janela    
    window.clear()
#Executa o texto criado na variavel label e desenha na tela    
    label.draw()
#comando que executa a aplicação pyglet
pyglet.app.run()                              

from kivy.app import App
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.properties import ListProperty
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from random import randint



class LabelcomCor(Label):
    Labelcor = ListProperty([0,0,1,1])
    color = 0,0,0,1
    test = str('teste')
    def on_pos(self,*args):
        self.atualizarRec(self.test)
    def on_size(self,*args):
        self.atualizarRec(self.test)
    def atualizarRec(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=self.Labelcor)
            Ellipse(size=(self.height, self.height),
                    pos=self.pos)
            Ellipse(size=(self.height, self.height),
                    pos=(self.x + self.width - self.height, self.y))
            Rectangle(size=(self.width - self.height, self.height),
                      pos=(self.x + self.height / 2.0, self.y))
class LabelsemCor(Label):
    color = 0,0,0,1
    font_size = 17
    def atualizarTam(self,*args):
        self.font_size = 50
class Botao(ButtonBehavior,Label):
    corP = ListProperty([0,0,1,1])
    corA = ListProperty([1,1,0,1])
    corB = ListProperty([0,0,1,1])
    corLetra = ListProperty([1,1,1,1])
    color = 0,0,0,1

    def __init__(self, **kwargs):
        super(Botao,self).__init__(**kwargs)
        self.atualizar()
    def on_corP(self,*args):
        self.atualizar()
    def on_pos(self,*args):
        self.atualizar()
    def on_press(self,*args):
        self.corP = self.corA
    def on_size(self,*args):
        self.atualizar()
    def on_release(self,*args):
        self.corP = self.corB
    def atualizar(self,*args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=self.corP)
            Ellipse(size=(self.height,self.height),
                    pos=self.pos)
            Ellipse(size=(self.height, self.height),
                    pos=(self.x+self.width-self.height,self.y))
            Rectangle(size=(self.width-self.height,self.height),
                      pos=(self.x+self.height/2.0,self.y))
class Gerenciador(ScreenManager):
    pass
class Menuinicial(Screen):
    def confirmacao(self, *args):
        box = BoxLayout(orientation='vertical',padding=10,spacing=10)
        botoes = BoxLayout(padding=10, spacing=10)
        pop = Popup(title='Deseja mesmo sair?',content=box,size_hint=(None,None),size=(300,180))

        sim = Botao(text='Sim', on_release=App.get_running_app().stop)
        nao = Botao(text='Não', on_release=pop.dismiss)

        botoes.add_widget(sim)
        botoes.add_widget(nao)

        pop.open()

        box.add_widget(botoes)
class MenuOpcoes(Screen):
    pass  
class Pergunta1(Screen):
    def erro(self, *args):
        box = BoxLayout(orientation='vertical',padding=10,spacing=10)
        botoes = BoxLayout(padding=10, spacing=10)
        pop = Popup(title='Não é a cor azul. Vamos tentar novamente.',content=box,size_hint=(None,None),size=(300,180))

        sim = Botao(text='Sim', on_release=pop.dismiss)
        

        botoes.add_widget(sim)

        pop.open()

        box.add_widget(botoes)
    
    def acerto(self, *args):
        box = BoxLayout(orientation='vertical',padding=10,spacing=10)
        botoes = BoxLayout(padding=10, spacing=10)
        pop = Popup(title='Parabéns, você acertou. Vamos pra próxima.',content=box,size_hint=(None,None),size=(300,180))

        sim = Botao(text='Vamos', on_release=pop.dismiss)
        

        botoes.add_widget(sim)

        pop.open()

        box.add_widget(botoes)   

    def confirmacao(self, *args):
        box = BoxLayout(orientation='vertical',padding=10,spacing=10)
        botoes = BoxLayout(padding=10, spacing=10)
        pop = Popup(title='Deseja mesmo sair?',content=box,size_hint=(None,None),size=(300,180))

        sim = Botao(text='Sim', on_release=App.get_running_app().stop)
        nao = Botao(text='Não', on_release=pop.dismiss)

        botoes.add_widget(sim)
        botoes.add_widget(nao)

        pop.open()

        box.add_widget(botoes)
class Pergunta2(Screen):
    def erro(self, *args):
        box = BoxLayout(orientation='vertical',padding=10,spacing=10)
        botoes = BoxLayout(padding=10, spacing=10)
        pop = Popup(title='Não é o Melão. Vamos tentar novamente.',content=box,size_hint=(None,None),size=(300,180))

        sim = Botao(text='Sim', on_release=pop.dismiss)


        botoes.add_widget(sim)

        pop.open()

        box.add_widget(botoes)
    
    def acerto(self, *args):
        box = BoxLayout(orientation='vertical',padding=10,spacing=10)
        botoes = BoxLayout(padding=10, spacing=10)
        pop = Popup(title='Parabéns, você acertou. Vamos pra próxima.',content=box,size_hint=(None,None),size=(300,180))

        sim = Botao(text='Vamos', on_release=pop.dismiss)


        botoes.add_widget(sim)

        pop.open()

        box.add_widget(botoes)   
        
    def confirmacao(self, *args):
        box = BoxLayout(orientation='vertical',padding=10,spacing=10)
        botoes = BoxLayout(padding=10, spacing=10)
        pop = Popup(title='Deseja mesmo sair?',content=box,size_hint=(None,None),size=(300,180))

        sim = Botao(text='Sim', on_release=App.get_running_app().stop)
        nao = Botao(text='Não', on_release=pop.dismiss)

        botoes.add_widget(sim)
        botoes.add_widget(nao)

        pop.open()

        box.add_widget(botoes)
class Pergunta3(Screen):
    def erro(self, *args):
        box = BoxLayout(orientation='vertical',padding=10,spacing=10)
        botoes = BoxLayout(padding=10, spacing=10)
        pop = Popup(title='Não são 3 dedos. Vamos tentar novamente.',content=box,size_hint=(None,None),size=(300,180))

        sim = Botao(text='Sim', on_release=pop.dismiss)


        botoes.add_widget(sim)

        pop.open()

        box.add_widget(botoes)
    
    def acerto(self, *args):
        box = BoxLayout(orientation='vertical',padding=10,spacing=10)
        botoes = BoxLayout(padding=10, spacing=10)
        pop = Popup(title='Parabéns, você acertou. Vamos pra próxima.',content=box,size_hint=(None,None),size=(300,180))

        sim = Botao(text='Vamos', on_release=pop.dismiss)


        botoes.add_widget(sim)

        pop.open()

        box.add_widget(botoes)
class Pergunta4(Screen):
   pass
class MeuAplicativo(App):
    def build(self):
        Window.size = (400,660)
        Window.position = 'custom'
        Window.left = 0
        Window.top = 0
        return Gerenciador()

MeuAplicativo().run()

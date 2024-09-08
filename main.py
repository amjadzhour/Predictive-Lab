from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.core.window import Window
from joblib import load
Builder.load_file("main.kv")
class Pag1(Screen):
    pass 

class Pag2(Screen):
     pclass=0
     age=0
     sibsp=0
     fare=0
     sex=0
     ticket=0
     e=0
   
     def Spinner(self,v):
          p=["hight","median","low1"]
          if v==p[0]:
               self.pclass=3
          elif v==p[1]:
               self.pclass=2
          elif v==p[2]:
                self.pclass=1
    
     def sex(self,v):
        if v=='male':
            self.sex=1
        else:
             self.sex=0   
     def embarked(self,v):
          p=["Queenstown","Cherbourg",'Southampton']
          if v==p[0]:
               self.pclass=3
          elif v==p[1]:
               self.pclass=2
          elif v==p[2]:
                self.pclass=1
     def pred(self):
            self.age=(self.ids.age1.text) 
            self.sibsp=(self.ids.sibsp1.text)
            self.fare=(self.ids.fare1.text)
            self.ticket=(self.ids.ticket1.text)
            k=[[self.pclass,self.age,self.sibsp,self.fare,self.sex,self.ticket,self.e]]
            print(k)
              

class PredictiveLab(App):
    Window.size=(1080,2340)
    Window.clearcolor=(164/255,104/255,247/255,0.8)
    def build(self):
        sm=ScreenManager()
        sm.add_widget(Pag1(name="pag1"))
        sm.add_widget(Pag2(name="pag2"))
        return sm

if __name__=="__main__":
       PredictiveLab().run() 
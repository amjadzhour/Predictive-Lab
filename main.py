
from kivy.core.window import Window
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
import random
from kivy.animation import Animation

lang=Builder.load_file('XandO.kv')
class FirstWN(Screen):
     pass
class SecondWD(Screen):
    i=random.randint(0,2)
    y=0
    def play(self):
        o=""
        
        if self.i==0:
            o="X"
            self.ids.t1.text=f'play in O'
            i=(1,0,0,0.8)
            self.i=1
        else:    
            o="O"
            self.ids.t1.text=f'play in X'
            i=(255/255,223/255,132/255,1)
            self.i=0
        return o ,i   
            
    def cleack(self,l):
        
       
        if l=="1,1" and len(self.ids.b1.text)==0:
            o,i=self.play()
            self.ids.b1.text=o
            self.ids.b1.color=i
        elif l=="1,2" and len(self.ids.b2.text)==0:
            o,i=self.play()
            self.ids.b2.text=o   
            self.ids.b2.color=i 
        elif l=="1,3" and len(self.ids.b3.text)==0 :
            o,i=self.play()
            self.ids.b3.text=o   
            self.ids.b3.color=i
        elif l=="2,1" and len(self.ids.b4.text)==0:
            o,i=self.play()
            self.ids.b4.text=o  
            self.ids.b4.color=i 
        elif l=="2,2" and len(self.ids.b5.text)==0:
            o,i=self.play()
            self.ids.b5.text=o    
            self.ids.b5.color=i
        elif l=="2,3" and len(self.ids.b6.text)==0 :
            o,i=self.play()
            self.ids.b6.text=o 
            self.ids.b6.color=i
        elif l=="3,1" and len(self.ids.b7.text)==0 :
            o,i=self.play()
            self.ids.b7.text=o
            self.ids.b7.color=i
        elif l=="3,2" and len(self.ids.b8.text)==0 :
            o,i=self.play()
            self.ids.b8.text=o  
            self.ids.b8.color=i
        elif l=="3,3"and len(self.ids.b9.text)==0 :
            o,i=self.play()
            self.ids.b9.text=o
            self.ids.b9.color=i
        self.y+=1  
        self.win()  
    def reset(self):
        self.i=random.randint(0,2)
        self.play()
        self.ids.b1.text=''
        self.ids.b2.text=''
        self.ids.b3.text=''
        self.ids.b4.text=''
        self.ids.b5.text=''
        self.ids.b6.text=''
        self.ids.b7.text=''
        self.ids.b8.text=''
        self.ids.b9.text=''
    def win(self):
        i=0
        if self.y>=5:
            p=""
            if (self.ids.b1.text=="X" and self.ids.b4.text=="X") and self.ids.b7.text=="X":
                p="X" 

            elif (self.ids.b1.text=="O" and self.ids.b4.text=="O") and self.ids.b7.text=="O":
                p='O'     

            elif (self.ids.b1.text=="O" and self.ids.b2.text=="O") and self.ids.b3.text=="O":
                   p='O'  

            elif (self.ids.b1.text=="X" and self.ids.b2.text=="X") and self.ids.b3.text=="X":
                   p='X' 

            elif (self.ids.b4.text=="X" and self.ids.b5.text=="X") and self.ids.b6.text=="X":
                   p='X'  
                   
            elif (self.ids.b4.text=="O" and self.ids.b5.text=="O") and self.ids.b6.text=="O":
                   p='O'  

            elif (self.ids.b7.text=="O" and self.ids.b8.text=="O") and self.ids.b9.text=="O":
                   p='O' 

            elif (self.ids.b7.text=="X" and self.ids.b8.text=="X") and self.ids.b9.text=="X":
                   p='X' 



            elif (self.ids.b2.text=="O" and self.ids.b5.text=="O") and self.ids.b8.text=="O":
                p='O'  

            elif (self.ids.b2.text=="X" and self.ids.b5.text=="X") and self.ids.b8.text=="X":
                p='X'  

            elif (self.ids.b3.text=="X" and self.ids.b6.text=="X") and self.ids.b9.text=="X":
                p='X'    

            elif (self.ids.b3.text=="O" and self.ids.b6.text=="O") and self.ids.b9.text=="O":
                p='O'        

            elif (self.ids.b1.text=="O" and self.ids.b5.text=="O") and self.ids.b9.text=="O":
                p='O'  

            elif (self.ids.b1.text=="X" and self.ids.b5.text=="X") and self.ids.b9.text=="X":
                p='X'          

            elif (self.ids.b3.text=="O" and self.ids.b5.text=="O") and self.ids.b7.text=="O":
                p='O'

            elif (self.ids.b3.text=="X" and self.ids.b5.text=="X") and self.ids.b7.text=="X" :
                p='X'        
            if p!="":      
                self.ids.t1.text=f"The Wine in {p}"      
                i=1
                  
        


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstWN(name='FirstWN'))
        sm.add_widget(SecondWD(name='head'))
        
        Window.clearcolor=(153/255,18/255,135/255,0.8)
        return sm
    
MyApp().run()


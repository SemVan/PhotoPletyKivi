from kivy.app import App



from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class makApp(App):
    def form(self, instance):
        self.mass.append(str(instance.text))
        self.lbl.text=instance.text
        
    def prnt(self, instance):
        summ=''
        for i in self.mass:
            summ+=i
        self.lbl.text=summ
        self.mass=[]
        
    def build(self):
        self.mass=[]
        
        bl1=BoxLayout(orientation='vertical')
        bl2=BoxLayout()
        
        self.lbl=Label(text='0')
        bl1.add_widget(self.lbl)
        
        bl2.add_widget( Button(text='1',on_press=self.form))
        bl2.add_widget( Button(text='2',on_press=self.form))
        bl2.add_widget( Button(text='3',on_press=self.form))
        bl2.add_widget( Button(text='4',on_press=self.form))
        bl2.add_widget( Button(text='str',on_press=self.prnt))
        
        bl1.add_widget(bl2)
        
        return bl1

if __name__=='__main__':
    makApp().run()
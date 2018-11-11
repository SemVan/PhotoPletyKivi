from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import (Line,Color)
import threading
import numpy as np
import cv2
import time 

class LineApp(App):
    def build(self):
        return LineWidget()

class LineWidget(Widget):
    def __init__(self, **kwargs):
        super(LineWidget, self).__init__(**kwargs)
        
        with self.canvas:
            Color(0,1.,0)
            self.line=Line(points=())
            
    def on_touch_down(self, touch):
        def writer1(x, event_for_wait):
            for i in range(50):
                event_for_wait.wait()
                event_for_wait.clear()
                ret, frame = cap.read()   
                b,g,r=cv2.split(frame)
                self.line.points+=(i*2,(np.sum(b)+np.sum(g)+np.sum(r))//100000)
        
        def writer2(x, event_for_wait):
            for i in range(50):
                event_for_wait.wait()
                event_for_wait.clear()
                ret, frame = cap.read()    
                b,g,r=cv2.split(frame)
                self.line.points+=(i*2+1,(np.sum(b)+np.sum(g)+np.sum(r))//100000)
                
        e1 = threading.Event()
        e2 = threading.Event()

        t1 = threading.Thread(target=writer1, args=(0, e1))
        t2 = threading.Thread(target=writer2, args=(1, e2))  
        
        t1.start()
        t2.start()
        
        cap = cv2.VideoCapture(0)

        for i in range(51):
            time.sleep(0.1)
            e1.set()
            time.sleep(0.1)
            e2.set()
            
        t1.join()
        t2.join()

        cap.release()
        cv2.destroyAllWindows()

if __name__=='__main__':
    LineApp().run()
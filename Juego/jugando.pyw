from tkinter import *
from tkinter import messagebox
import random
import time

class Ball:
    def __init__(self, canvas, pa, color):
        self.canvas = canvas
        self.pa = pa
        self.id = canvas.create_oval(10, 10, 25, 25, fill = color)
        self.canvas.move(self.id, random.randint(1, 499), random.randint(1, 130))
        start = [-3, -2, -1, 1, 2, 3]
        random.shuffle(start)
        self.x = start[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        
    
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = random.randint(1, 5)
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if pos[0] <= 0:
            self.x = random.randint(1, 5)
        if pos[2] >= self.canvas_width:
            self.x = random.randint(-5, 1)
        if self.hit_pa(pos):
            self.y = -1
            

    
    def hit_pa(self, pos):
        pa_pos = self.canvas.coords(self.pa.id)
        if pos[2] >= pa_pos[0] and pos[0] <= pa_pos[2] and pos[3] >= pa_pos[1] and pos[3] <= pa_pos[3]:
            return True
        else:
            return False
            
        
class Pad:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill = color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>",self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>",self.turn_right)
        

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= self.canvas_width:
            self.x = 0

        
    def turn_left(self, evt):
        pos = self.canvas.coords(self.id)
        if pos[0] > 0:
            self.x = -3
        
    def turn_right(self, evt):
        pos = self.canvas.coords(self.id)
        if pos[2] < self.canvas_width:
            self.x = 3

    def do_nothing(self, evt):
        self.x = 0

raiz = Tk()
raiz.title("Primer juego de ZJQ")
raiz.resizable(False,False)

canvas = Canvas(raiz, width = 500, height = 500)
canvas.grid(row = 1)

raiz.update()

while True:
    pa = Pad(canvas, "black")
    bola = Ball(canvas, pa, "red")
    t0 = time.time()
        
    while True:
        if not bola.hit_bottom:
            bola.draw()
            pa.draw()
            t1 = time.time()
            Label(raiz, text = "Score: {}".format(int(t1-t0))).grid(row = 0)
        else:
            perdiste = messagebox.askyesno("Game over","Quieres volver a empezar?")
            if perdiste:
                bola.hit_bottom = False
                canvas.delete("all")
                del t0
                del pa
                del bola
            else:
                messagebox.showinfo("Quit","Tu puntuación es {}".format(int(t1-t0)))   
            break

        time.sleep(0.01)
        raiz.update()
    if not perdiste:
        break

if not perdiste:
    raiz.destroy()
        
raiz.mainloop()
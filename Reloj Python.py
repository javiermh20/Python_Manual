from tkinter import Label, Tk
from time import strftime

IG = Tk () 
IG.title("Reloj Python")
IG.config(bg='white')
IG.geometry('370x230')

def obtener_tiempo():
    hora =  strftime('%H:%M:%S')
    x = texto_hora.winfo_height()
    t = int((x-5)*0.32)
    texto_hora.config(text=hora, font = ('Sylfaen', t))

    texto_hora.after(1000, obtener_tiempo)

texto_hora = Label(IG,  fg = 'yellow', bg='black')
texto_hora.grid(row=0,sticky="nsew", ipadx=15, ipady=50)
obtener_tiempo()
IG.mainloop() 

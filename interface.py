import tkinter as tk
import winsound  # Módulo para reprodução de sons no Windows
from tkinter import messagebox
import sys as tk # tentativa de importar icons

def play_beep():
    winsound.Beep(1000, 500)  # Frequência e duração do beep

def exibir_sobre (): 
     messagebox.showinfo("Sobre", "Programa desenvolvido por :\n\nGeovani França\nJoão Victor\nJoão Mauricio\nBreno Xavier\n\nINF251") #menu


#config da tela
app = tk.Tk()
app.title("Analista de Beep")
app.config(bg="purple") 
 
#config do botão       
play_button = tk.Button(app, text="Play Beep", command=play_beep)
play_button.pack()
play_button.place(relx=0.4, rely=0.5)
play_button.configure(width="30", height="2")


#config da barra de menu
fonte_menu = ("Arial", 12)

menu_bar = tk.Menu(app)
app.config(menu=menu_bar) 

ajuda_menu = tk.Menu(menu_bar, tearoff=0, font=fonte_menu)
menu_bar.add_cascade(label="Ajuda", menu=ajuda_menu)
ajuda_menu.add_command(label="Sobre", command=exibir_sobre)
ajuda_menu.add_separator()
ajuda_menu.add_command(label="Sair", command=app.quit)





app.mainloop()

from tkinter import *
class ciudad:
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("pronostico del clima")
        self.raiz.iconbitmap("C:\\Users\\Tomas\\Desktop\\faq\\programación 2\\trabajo final\\nublado.ico")
        self.raiz.geometry("200x170")
        self.raiz.resizable(0,0)
        self.raiz.resizable(False,False)
        self.raiz.config(bg="gray")
        self.labelciudad = Label(self.raiz, text="Ingrese ciudad:")
        self.labelciudad.place(x = 50 , y = 30)
        self.ciudad = Entry(self.raiz)
        self.ciudad.place(x = 30 , y = 50)
        self.boton = Button(self.raiz,text="Enviar",bg="green").place(x = 70 , y = 80)
        self.raiz.mainloop()
    
    
    def abrirventana():   
        pass 
        cerrar_ventana()
    def cerrar_ventana(self):
        self.raiz.destroy()
        
app = ciudad()
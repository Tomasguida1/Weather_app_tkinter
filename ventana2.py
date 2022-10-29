from tkinter import *
from tkinter import ttk
import requests
import datetime
class app:
    


    
    def __init__(self):
        self.app = Tk()
        self.app.title("pronostico del clima")
        self.app.iconbitmap("C:\\Users\\Tomas\\Desktop\\faq\\programación 2\\trabajo final\\nublado.ico")
        self.app.geometry("1200x630+0+0")
        self.app.resizable(0,0)
        self.app.resizable(False,False)
        self.app.config(bg="turquoise")
        self.panel_sup = Frame(self.app, bd=1, relief=FLAT)
        self.panel_sup.pack(side="top")
        self.titulo = Label(self.panel_sup, text = "Pronóstico del clima", fg = "cadet blue", font = ("Dosis",58),bg = "aquamarine1",width = 27)
        self.titulo.grid(row = 0, column= 0)
        menuc =Menu(self.app)
        self.app.config(menu= menuc, width=300, height=300)
        ayuda = Menu(menuc, tearoff=0)
        ayuda.add_command(label="como usar el programa")
        menuc.add_cascade(label="ayuda", menu=ayuda)

        #panel derecho
        self.framed = Frame()
        self.framed.pack()
        self.framed.config(width = 600, height = 300)
        self.framed.config(bg="gray")
        self.framed.place(x = 0 , y = 100)
        img = PhotoImage(file = "clima.png")
        self.labeli = Label(self.framed, image = img)
        self.labeli.place(x = 0 , y = 0)

        self.url = f"https://api.openweathermap.org/data/2.5/weather?q=rosario&appid=ad82a5b3bf4c32ae52b43bde36ee8ce4"
        self.res = requests.get(self.url)
        self.climac = self.res.json()
        self.temp = self.climac["main"]["temp"]
        self.temp = round(self.temp - 273.15)
        self.tempmin = self.climac["main"]["temp_min"]
        self.tempmin = round(self.tempmin - 273.15)
        self.tempmax = self.climac["main"]["temp_max"]
        self.tempmax = round(self.tempmax - 273.15)
        self.humedad = self.climac["main"]["humidity"]
        self.labelpronostico = Label(self.framed, text= f"Temperatura: {self.temp}°", font=("Bahnschrift Condensed",30,"bold"), bg = "gray" )
        self.labelpronostico.place(x = 320 , y = 50)
        self.labeltempmin = Label(self.framed, text= f"Mínima: {self.tempmin}°", font=("Bahnschrift Condensed",30,"bold") , bg = "gray" )
        self.labeltempmin.place(x = 320 , y = 100)
        self.labeltempmax = Label(self.framed, text= f"Máxima: {self.tempmax}°", font=("Bahnschrift Condensed",30,"bold"), bg = "gray" )
        self.labeltempmax.place(x = 320 , y = 150)
        self.labelhumedad = Label(self.framed, text= f"Humedad: {self.humedad}%", font=("Bahnschrift Condensed",30,"bold"), bg = "gray" )
        self.labelhumedad.place(x = 320 , y = 200)
        #PANEL IZQUIERDO
        self.framei = Frame()
        self.framei.pack()
        self.framei.config(width = 600, height = 300)
        self.framei.config(bg="yellow")
        self.framei.place(x = 600 , y = 100)
        img1 = PhotoImage(file = "reloj.png")
        self.labeli = Label(self.framei, image = img1)
        self.labeli.place(x = 0 , y = 0)
        fecha = datetime.datetime.now()
        self.labelfecha = Label(self.framei, text=f"{fecha.day}/{fecha.month}/{fecha.year}", font=("Bahnschrift Condensed",40,"bold"), bg = "yellow")
        self.labelfecha.place(x = 360 , y = 60)
        self.labelhora = Label(self.framei, text=f"{fecha.hour}:{fecha.minute}", font=("Digital dream fat",40,"bold"), bg = "yellow")
        self.labelhora.place(x = 360 , y = 180)
        #panel inferior
        self.framein = Frame()
        self.framein.pack()
        self.framein.config(width = 1200, height = 230)
        self.framein.config(bg="red")
        self.framein.place(x = 0, y = 400)
        #HORARIO EUROPA
        self.labelhoraeu = Label(self.framein, text="HORARIOS EUROPA")
        self.labelhoraeu.place(x = 80 , y = 60)  
        self.labelhoraeu1 = Label(self.framein, text="00:00")
        self.labelhoraeu1.place(x = 80 , y = 100)   
        self.labelhoraeu2 = Label(self.framein, text="00:00")
        self.labelhoraeu2.place(x = 80 , y = 140)       
        self.labelhoraeu3 = Label(self.framein, text="00:00")
        self.labelhoraeu3.place(x = 80 , y = 180)    
        #HORARIO ASIA
        self.labelhoraas = Label(self.framein, text="HORARIOS ASIA")
        self.labelhoraas.place(x = 200 , y = 60) 
        self.labelhoraas1 = Label(self.framein, text="00:00")
        self.labelhoraas1.place(x = 200 , y = 100)   
        self.labelhoraas2 = Label(self.framein, text="00:00")
        self.labelhoraas2.place(x = 200 , y = 140)       
        self.labelhoraas3 = Label(self.framein, text="00:00")
        self.labelhoraas3.place(x = 200 , y = 180)     
        #HORARIOS OCEANIA  
        self.labelhoraoc = Label(self.framein, text="HORARIOS OCEANIA")
        self.labelhoraoc.place(x = 300 , y = 60)     
        self.labelhoraoc1 = Label(self.framein, text="00:00")
        self.labelhoraoc1.place(x = 300 , y = 100)   
        self.labelhoraoc2 = Label(self.framein, text="00:00")
        self.labelhoraoc2.place(x = 300 , y = 140)       
        self.labelhoraoc3 = Label(self.framein, text="00:00")
        self.labelhoraoc3.place(x =300 , y = 180)         
        #HORARIOS NORTEAMERICA
        self.labelhorausa = Label(self.framein, text="HORARIOS NORTEAMERICA")
        self.labelhorausa.place(x = 425 , y = 60)  
        self.labelhorausa1 = Label(self.framein, text="00:00")
        self.labelhorausa1.place(x =425 , y = 100)   
        self.labelhorausa2 = Label(self.framein, text="00:00")
        self.labelhorausa2.place(x =425 , y = 140)       
        self.labelhorausa3 = Label(self.framein, text="00:00")
        self.labelhorausa3.place(x = 425, y = 180) 
        #conversor a fahrenheit/celsius
        self.labelc = Label(self.framein, text="CONVERTIR TEMPERATURA A:")
        self.labelc.place(x = 800 , y = 60)  
        celsius = Button(self.framein,text="KELVIN",bg="white",height = 5, width = 30).place(x = 670 , y = 100)       
        fahrenheit = Button(self.framein,text="FAHRENHEIT",bg="white",height = 5, width = 30).place(x = 900 , y = 100)    
        self.app.mainloop()
    

miapp = app()



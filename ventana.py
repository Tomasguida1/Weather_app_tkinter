from tkinter import *
from tkinter import ttk
import requests
import datetime
import pytz
from pytz import timezone
from tkinter import messagebox
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
        #COMANDO AYUDA
        def ayudaop():
            messagebox.showinfo("ayuda","Ingresá la ciudad de la que deseas saber el clima y presioná el botón de enviar , aparte el programa mostrará la hora y el día actual en la ciudad de Rosario, tambien en la parte inferior se muestra que hora es en otras zonas horarias, y a la derecha un conversor a grados kelvin y fahrenheit")
        ayuda.add_command(label="como usar el programa",command = ayudaop)
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
        #INGRESO DE CIUDAD
        labelciudad = Label(self.framed, text="Ciudad:",font=("Bahnschrift Condensed",30,"bold"), bg = "gray")
        labelciudad.place(x = 320 , y = 10)
        ciudad = Entry(self.framed)
        ciudad.place(x = 430 , y = 30)
        def obtenerclima(ciudad):
            api = "ad82a5b3bf4c32ae52b43bde36ee8ce4"
            self.url = "https://api.openweathermap.org/data/2.5/weather"
            parametros = {"APPID": api , "q":ciudad}
            self.res = requests.get(self.url, params = parametros)
            self.climac = self.res.json()
            self.temp = self.climac["main"]["temp"]
            self.temp = round(self.temp - 273.15)
            self.tempmin = self.climac["main"]["temp_min"]
            self.tempmin = round(self.tempmin - 273.15)
            self.tempmax = self.climac["main"]["temp_max"]
            self.tempmax = round(self.tempmax - 273.15)
            self.humedad = self.climac["main"]["humidity"]
            self.labelpronostico = Label(self.framed, text= f"Temperatura: {self.temp}°", font=("Bahnschrift Condensed",30,"bold"), bg = "gray" )
            self.labelpronostico.place(x = 320 , y = 80)
            self.labeltempmin = Label(self.framed, text= f"Mínima: {self.tempmin}°", font=("Bahnschrift Condensed",30,"bold") , bg = "gray" )
            self.labeltempmin.place(x = 320 , y = 130)
            self.labeltempmax = Label(self.framed, text= f"Máxima: {self.tempmax}°", font=("Bahnschrift Condensed",30,"bold"), bg = "gray" )
            self.labeltempmax.place(x = 320 , y = 180)
            self.labelhumedad = Label(self.framed, text= f"Humedad: {self.humedad}%", font=("Bahnschrift Condensed",30,"bold"), bg = "gray" )
            self.labelhumedad.place(x = 320 , y = 230)
            

        botonclima = Button(self.framed, text = "Enviar",bg="purple",command = lambda:obtenerclima(ciudad.get())).place(x = 550 , y = 30)

        #PANEL IZQUIERDO
        self.framei = Frame()
        self.framei.pack()
        self.framei.config(width = 600, height = 300)
        self.framei.config(bg="yellow")
        self.framei.place(x = 600 , y = 100)
        #HORA Y DÍA
        img1 = PhotoImage(file = "reloj.png")
        self.labeli = Label(self.framei, image = img1)
        self.labeli.place(x = 0 , y = 0)
        fecha = datetime.datetime.now()
        self.labelfecha = Label(self.framei, text=f"{fecha.day}/{fecha.month}/{fecha.year}", font=("Bahnschrift Condensed",40,"bold"), bg = "yellow")
        self.labelfecha.place(x = 360 , y = 60)
        self.labelhora = Label(self.framei, text=f"{fecha.hour}:{fecha.minute}", font=("Digital dream fat",40,"bold"), bg = "yellow")
        self.labelhora.place(x = 340 , y = 180)
        #panel inferior
        self.framein = Frame()
        self.framein.pack()
        self.framein.config(width = 1200, height = 230)
        self.framein.config(bg="red")
        self.framein.place(x = 0, y = 400)
        #HORARIO EUROPA
        self.labelhoraeu = Label(self.framein, text="HORARIOS EUROPA",bg = "grey")
        self.labelhoraeu.place(x = 80 , y = 60) 
        ahora = datetime.datetime.now(timezone("UTC"))
        horalon = ahora.astimezone(timezone("Europe/London"))
        self.labelhoraeu1 = Label(self.framein, text=f"Londres: {horalon.hour}:{horalon.minute}",bg = "grey")
        self.labelhoraeu1.place(x = 80 , y = 100)   
        horamad = ahora.astimezone(timezone("Europe/Madrid"))
        self.labelhoraeu2 = Label(self.framein, text=f"Madrid: {horamad.hour}:{horamad.minute}",bg = "grey")
        self.labelhoraeu2.place(x = 80 , y = 140)  
        horarom = ahora.astimezone(timezone("Europe/Rome"))     
        self.labelhoraeu3 = Label(self.framein, text=f"Roma: {horarom.hour}:{horarom.minute}",bg = "grey")
        self.labelhoraeu3.place(x = 80 , y = 180)    
        #HORARIO ASIA
        
        self.labelhoraas = Label(self.framein, text="HORARIOS ASIA",bg = "grey")
        self.labelhoraas.place(x = 200 , y = 60) 
        horadub = ahora.astimezone(timezone("Asia/Dubai"))
        self.labelhoraas1 = Label(self.framein, text=f"Dubai : {horadub.hour}:{horadub.minute}",bg = "grey")
        self.labelhoraas1.place(x = 200 , y = 100)  
        horajap = ahora.astimezone(timezone("Asia/Tokyo")) 
        self.labelhoraas2 = Label(self.framein, text=f"Tokio : {horajap.hour}:{horajap.minute}",bg = "grey")
        self.labelhoraas2.place(x = 200 , y = 140)   
        horatur = ahora.astimezone(timezone("Asia/Istanbul"))    
        self.labelhoraas3 = Label(self.framein, text=f"Estambul : {horatur.hour}:{horatur.minute}",bg = "grey")
        self.labelhoraas3.place(x = 200 , y = 180)     
        #HORARIOS OCEANIA  
        self.labelhoraoc = Label(self.framein, text="HORARIOS OCEANIA",bg = "grey")
        self.labelhoraoc.place(x = 300 , y = 60)     
        horaaus = ahora.astimezone(timezone("Australia/Sydney"))
        self.labelhoraoc1 = Label(self.framein, text=f"Sidney: {horaaus.hour}:{horaaus.minute}",bg = "grey")
        self.labelhoraoc1.place(x = 300 , y = 100)  
        horanz = ahora.astimezone(timezone("NZ")) 
        self.labelhoraoc2 = Label(self.framein, text=f"Auckland: {horanz.hour}:{horanz.minute}",bg = "grey")
        self.labelhoraoc2.place(x = 300 , y = 140)               
        #HORARIOS NORTEAMERICA
        self.labelhorausa = Label(self.framein, text="HORARIOS NORTEAMERICA",bg = "grey")
        self.labelhorausa.place(x = 425 , y = 60)  
        horaang = ahora.astimezone(timezone("America/Los_Angeles")) 
        self.labelhorausa1 = Label(self.framein, text=f"Los Angeles: {horaang.hour}:{horaang.minute}",bg   = "grey" )
        self.labelhorausa1.place(x =425 , y = 100) 
        horator = ahora.astimezone(timezone("America/Toronto"))   
        self.labelhorausa2 = Label(self.framein, text=f"Toronto: {horator.hour}:{horator.minute}",bg = "grey")
        self.labelhorausa2.place(x =425 , y = 140)   
        horamx = ahora.astimezone(timezone("America/Mexico_City"))     
        self.labelhorausa3 = Label(self.framein, text=f"Ciudad de Mexico: {horamx.hour}:{horamx.minute}", bg = "grey")
        self.labelhorausa3.place(x = 425, y = 180) 
        #conversor a fahrenheit/celsius
        self.labelc = Label(self.framein, text="CONVERTIR TEMPERATURA A:")
        self.labelc.place(x = 800 , y = 60)  
               
            

        def conkelvin():
            url = f"https://api.openweathermap.org/data/2.5/weather?q=rosario&appid=ad82a5b3bf4c32ae52b43bde36ee8ce4"
            resu = requests.get(url)
            climak = resu.json()
            tempk = climak["main"]["temp"]
            messagebox.showinfo("Kelvin",f"La temperatura en kelvin es: {tempk}°K")
        def confahrenheit():
            url = f"https://api.openweathermap.org/data/2.5/weather?q=rosario&appid=ad82a5b3bf4c32ae52b43bde36ee8ce4"
            resu = requests.get(url)
            climaf = resu.json()
            tempf = climaf["main"]["temp"]
            tempf = round((tempf - 273.15) * 9/5 + 32)

            messagebox.showinfo("Fahrenheit",f"La temperatura en fahrenheit es: {tempf}°F")
        kelvin = Button(self.framein,text="KELVIN",bg="white",height = 5, width = 30,command = conkelvin).place(x = 670 , y = 100)
        fahrenheit = Button(self.framein,text="FAHRENHEIT",bg="white",height = 5, width = 30,command = confahrenheit).place(x = 900 , y = 100)
        self.app.mainloop()

miapp = app()



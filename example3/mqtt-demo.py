from tkinter import *
# from gpiozero import LED, PWMLED
from signal import pause

class LedsGui(Frame):
    def __init__(self, master = None):
        Frame.__init__(self,master)

        self.ban = BooleanVar(value=False) # Bandera que indica si la luz esta prendida o apagada.
        
        """ Configurando elementos fisicos de la rPi """
        # self.led = LED(17)                  # pin del led: GPIO17 
        # self.led.off()
        # self.ledPWM = PWMLED(18)            # pin del led pwm: GPIO18 
        # self.ledPWM.value = 0


        """ Agregando los elementos de la interfaz grafica """
        self.pack()   # Frame raiz

        # Frame superior (Contiene el boton ON/OFF y el indicador del estado del led)
        self.frameLed = Frame(self)  
        self.buttonLed = Button(self.frameLed , text='ON', command=self.ledChange) # Boton ON/OFF
        self.buttonLed.pack(side = 'left')
        self.labelLed = Label(self.frameLed,text = "Led apagado", width = 16)  # Label indicador del estado del led
        self.labelLed.pack(side = 'left')
        self.frameLed.pack(pady=1) # Colocando el Superior en el frame raiz

        # Slider para el pwm (Contenido en la parte inferio del frame raiz)
        self.ledPWMScale = Scale(self,label='Dutty',
                            command=self.changePWM,
                            from_=0 , to=100 ,length=200,
                            tickinterval=20,
                            orient='horizontal')
        self.ledPWMScale.pack(expand=YES, fill=Y)

    
    def ledChange(self):
        if self.ban.get() == False:
            self.ban.set(True)
            print("led on")
            self.buttonLed.config(text = "OFF") 
            self.labelLed.config(text = "Led encendido") 
            # self.led.on()
        else:
            self.ban.set(False)
            print("led off")
            self.buttonLed.config(text = "ON")
            self.labelLed.config(text = "Led apagado")
            # self.led.off()

    
    def changePWM(self,value):
        #print(self.pwm.get())
        dutty = float(value)/100
        print(dutty)
        # self.ledPWM.value = dutty

if __name__ == '__main__':
    LedsGui().mainloop()
    
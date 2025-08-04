# PBX-Asterisk-Python-Mysql

Este desarrollo consiste en registrar las llamadas que recibe una centralita en una base de datos (Mysql) con el lenguaje de programación en Python.
En el lenguaje Asterisk se utiliza la funcion AGI para interactuar con el script de Python. 
Este es el contenido del fichero de configuración
[PBX] 
;RUTINA DE LLAMADA 
exten => _1XX,1,Answer() 
exten => _1XX,n,Set(arg=1) 
exten => _1XX,n,AGI(CheckCall.py,${arg})

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/354858b3-59ba-4383-a404-dee01f1fe9e6" />

# PBX-Asterisk-Python-Mysql

Este desarrollo tiene como objetivo verificar si las llamadas entrantes a una centralita están registradas en una base de datos MySQL, utilizando el lenguaje de programación Python. En caso de que el número del llamante esté identificado en la base de datos, se ejecutarán determinadas acciones predefinidas.


La función AGI (Asterisk Gateway Interface) en Asterisk permite ejecutar scripts externos para controlar el flujo de llamadas de forma dinámica. Es como una “puerta de enlace” entre Asterisk y otros lenguajes de programación como Python, PHP o Perl.

Este es el contenido del fichero de configuración\n
[PBX]\n 
;RUTINA DE LLAMADA\n 
exten => _1XX,1,Answer()\n
exten => _1XX,n,Set(arg=1)\n
exten => _1XX,n,AGI(CheckCall.py,${arg})\n

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/354858b3-59ba-4383-a404-dee01f1fe9e6" />

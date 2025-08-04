#!/usr/bin/python3

import sys
import mysql.connector
from asterisk.agi import AGI

agi = AGI()
agi.verbose("Started rutinacall")
callerId = agi.env['agi_callerid']
agi.verbose("callerID: "+callerId)
codigo=sys.argv[1]


cnx = mysql.connector.connect(user='user', password='user', host='127.0.0.1', database='usersNumber')
cursor = cnx.cursor()

'CONSULTA DEL NUMERO DE LLAMADA'
query_codigo = ("SELECT id, name, phone from users where phone=" + callerId)
cursor.execute(query_codigo)
query_result = cursor.fetchall()
if query_result==[]:
    usuario =['0','0','0']
else:
    usuario=(list(query_result[0]))

'COMPROBACION SI EL NUMERO ESTA REGISTRADO EN LA BBDD
if usuario[2]==callerId:
   
	'PREGUNTA PASSWORD'
	'-- PASSWORD INCORRECT --'
	if usuario[3]!=codigo:
		log='la password es incorrecta %s %s'%(usuario[0],usuario[1])
		agi.appexec('Playback','auth-incorrect')
		agi.hangup()
	else:
		'-- PASSWORD CORRECT --'
		log='la password es correcta %s %s'%(usuario[0],usuario[1])

		'SCRIPT DE CONEXION'
		os.system('python3 /ejecuu.py')
		agi.appexec('Playback','auth-thankyou')
		agi.hangup()
else:
    agi.hangup()
        
cursor.close()
cnx.close()
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import call
import subprocess
import os
import commands
import subprocess as sub
import time
	

def rojo(skk): print("\033[91m {}\033[01m" .format(skk))
def purple(skk): print("\033[90m {}\033[01m" .format(skk)) 
def verde(skk): print("\033[92m {}\033[01m" .format(skk)) 


amarillo="\x1b[1;33m"
cs_color='\033[0;m'
purpura="\x1b[1;35m"
verde="\x1b[1;32m"



print " "
print " "
os.system('toilet -f pagga --gay "OffShell  System"')
time.sleep(0.5)
print (verde + ' -OffShell System is an independent technological society-')
time.sleep(0.3)
rojo (verde + '                         -Community Software Development-')
time.sleep(0.3)
rojo (verde + '                                    -Technological Souls-' + cs_color)
time.sleep(0.5)


rojo ('			                   |')
time.sleep(0.1)

rojo ('			                   |')
time.sleep(0.1)

rojo ('                    Actualizando Sistema - - ')
time.sleep(0.3)

rojo ('			                   |')
time.sleep(0.1)

rojo ('			                   |' + cs_color)
time.sleep(0.1)

os.system('sudo apt-get install dnsutils -y')

rojo ('			                   |')
time.sleep(0.1)

rojo ('			                   |')
time.sleep(0.1)

rojo ('			  OffShell System - - ')
time.sleep(0.5)

rojo ('			                   |')
time.sleep(0.1)

rojo ('			                   |')
time.sleep(0.1)

rojo ('		   Sociedad Independiente - - ')
time.sleep(0.5)

rojo ('			                   |')
time.sleep(0.1)

rojo ('			                   |')
time.sleep(0.1)

purple (verde + '      Introducir Host-IP-Url-Dominio-DNS - - ' + cs_color)
time.sleep(0.2)

user = raw_input(verde + '			  		  - - Analizar---- > ' + cs_color)


host = commands.getoutput('dig ' + str(user) + ' +short')
puertos_abiertos = commands.getoutput('nmap ' + str(user))



print " "
rojo ('                      Guardando Variable - - ' + verde + str(user) + cs_color)

time.sleep(0.1)

rojo ('			                   |')
time.sleep(0.1)

rojo ('			                   |')
time.sleep(0.1)

rojo ('			  Comprobando DNS - - ' + verde + str(user) + ' - - ' + str(host) + cs_color)
time.sleep(0.5)

rojo ('			                   |')
time.sleep(0.1)

rojo ('			                   |')
time.sleep(0.1)


rojo ('			 Validando Domain - - ' + verde + str(user) + ' - - ' + str(host) + cs_color)
time.sleep(0.5)

rojo ('			                   |')
time.sleep(0.1)

rojo ('			                   |')
time.sleep(0.1)


rojo ('	      Información General Pública - - ' + verde + str(user) + ' - - ' + str(host) + cs_color)
time.sleep(0.5)

rojo ('			                   |')
time.sleep(0.1)

rojo ('			                   |')
time.sleep(0.1)

rojo ('                                Objetivo - - ' + verde + str(user) + ' - - ' + str(host) + cs_color)
time.sleep(0.5)

rojo ('			                   |')
time.sleep(0.1)

rojo ('			                   |')
time.sleep(0.1)

rojo ('         Recopilando información técnica - - ' + verde + str(user) + ' - - ' + str(host) + cs_color)
time.sleep(0.5)

rojo ('			                   |')
time.sleep(0.1)

rojo ('			                   |' + cs_color)
time.sleep(0.1)

os.system('whatweb ' + str(user)) 

rojo ('------------------------------------------')

rojo ('			                   |')
time.sleep(0.1)
rojo ('             Escaneando puertos abiertos - - ' + verde + str(user) + ' - - ' + str(puertos_abiertos) + cs_color)
rojo ('			                   |' + cs_color)
time.sleep(0.1)


rojo ('------------------------------------------')

rojo ('			                   |')
time.sleep(0.1)
rojo ('                         Analizando Host - - ' + verde + str(user) + ' - - ' + str(host) + cs_color)
rojo ('			                   |' + cs_color)
time.sleep(0.1)

os.system('host ' + str(user))

rojo ('------------------------------------------')

rojo ('			                   |')
time.sleep(0.1)
rojo ('             Procesando Herramienta para - - ' + verde + str(user) + ' - - ' + str(host) + cs_color)
rojo ('			                   |' + cs_color)
time.sleep(0.1)

os.system('dig ' + str(user))

rojo ('------------------------------------------')

rojo ('			                   |')
time.sleep(0.1)
rojo ('                     Buscando Datos para - - ' + verde + str(user) + ' - - ' + str(host) + cs_color)
rojo ('			                   |' + cs_color)
time.sleep(0.1)

os.system('nslookup ' + str(user))

rojo ('------------------------------------------')

rojo ('			                   |')
time.sleep(0.1)
rojo ('             Procesando Herramienta para - - ' + verde + str(user) + ' - - ' + str(host) + cs_color)
rojo ('			                   |' + cs_color)
time.sleep(0.1)

os.system('dig ' + str(user) + ' +short')

rojo ('------------------------------------------')

rojo ('			                   |')
time.sleep(0.1)
rojo ('             Procesando Herramienta para - - ' + verde + str(user) + ' - - ' + str(host) + cs_color)
rojo ('			                   |' + cs_color)
time.sleep(0.1)

os.system('dig ' + str(user) + ' +noall')

rojo ('------------------------------------------')

rojo ('			                   |')
time.sleep(0.1)
rojo ('             Procesando Herramienta para - - ' + verde + str(user) + ' - - ' + str(host) + cs_color)
rojo ('			                   |' + cs_color)
time.sleep(0.1)

os.system('dig ' + str(user) + ' +noall' + ' +answer')

rojo ('------------------------------------------')

rojo ('			                   |')
time.sleep(0.1)

rojo ('			                   |' + cs_color)
time.sleep(0.1)




time.sleep(0.7)
purple ('                  Cita de Linus Tordvals - - ')
print (amarillo + '"En los humanos existen 3 categorías de motivaciones:\n "supervivencia","vida social" y "entretenimiento", \nasí el trabajo basado en las TIC tiende\n a abolir la distancia entre las dos últimas categorías“' + cs_color)

rojo ('			                   |')
time.sleep(0.1)

rojo ('			                   |' + cs_color)
time.sleep(0.1)

purple ('         @@@@@@@@@@@@@@@@@@-----------------------------------------------')
time.sleep(0.1)
purple ('         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
time.sleep(0.1)
purple ('         @@ Proceso finalizado. Gracias por confiar en OffShell System. @@')
time.sleep(0.1)
purple ('         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
time.sleep(0.1)
purple ('         -------------------------------------------@@@@@@@@@@@@@@@@@@@@@@')
time.sleep(0.1)

rojo ('			                   |')
time.sleep(0.1)

rojo ('			                   |' + cs_color)
time.sleep(0.1)

os.system('toilet -f pagga --gay "Proceso Terminado"')



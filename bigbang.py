#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 01 11:11:23 2016
LCI
@author: pedroalpacheco
Deve ser executado no servidor master;
	-Atualiza PWM (PwmConfiguration.xml) no servidor pato2;
        -Envia o arquivo para demais servers-client;
	-Alterado 15/03/2016 --No servidor deve estar com permissão chmod 664 /var/lib/tomcat7/webapps/pwm/WEB-INF/PwmConfiguration.xml
	-Verificar a mudança da variavel PWM1 por PWM2;
"""

from datetime import datetime
import shutil
import os
import pysftp
from ConfigParser import SafeConfigParser

#-------VARIAVEIS---------
# Pega data e hora
agora = datetime.now()
hoje = str(agora)

#Arquivo de log
arqlog = ("update.log")

#Arquivo que será copiado para os servidores clients
arqorigem = "/var/lib/tomcat7/webapps/pwm/WEB-INF/PwmConfiguration.xml"

#Variavel de local de backup
lcbackup = "/home/atualizapwm/"

#Diretorio de destino do arquivo dentro dos clients
dirdestino = "/var/lib/tomcat7/webapps/pwm/WEB-INF/"

# Faz leitura do arquivo de configuracoes====================
parser = SafeConfigParser()
parser.read("Configuracoes.ini")

srvptum = parser.get("informacoes", "serverum")

srvusu = parser.get("informacoes", "serverumusu")

srvumpass = parser.get("informacoes", "serverumpass")

srvumport = parser.get("informacoes", "serverumport")

pth = int(srvumport)

#Realiza conexão-----

#Conecta ao client
srv = pysftp.Connection(host=srvptum, username=srvusu,password=srvumpass,log=arqlog,port=pth)


#Realizabackup##
#Cria variavel de data do diretorio de backup
dirbackup = lcbackup + hoje
#Cria diretorio
srv.mkdir(dirbackup)
#Vai até o diretorio 
with srv.cd(dirbackup):
    #Faz backup
    srv.put(arqorigem)

#Atualiza o servidor client
with srv.cd(dirdestino):
        # Envia arquivo ao site
	#Seta permissão no arquivo
        srv.execute("sudo chmod 664 " + arqorigem)
        srv.put(arqorigem)
        print("Atualização de server-->client OK!")
        srv.execute("sudo /etc/init.d/tomcat7 restart")
        print("Tomcat reiniciado no client!")
        
        
        


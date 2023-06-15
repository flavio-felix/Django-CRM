#install Mysql on your computer
#https://dev.mysql.com/downloads/installer/
#pip install mysql
#pip install mysql-connector
#pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
    user = 'root',
    passwd = 'felix',
    
)

## preparar um cursor object
cursorObject =  dataBase.cursor()

#criar um database
cursorObject.execute("CREATE DATABASE ppf")

print("concluido com sucesso.")
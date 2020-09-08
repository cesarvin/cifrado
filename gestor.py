import os
import os.path
from os import listdir
from os.path import isfile, join
import time

from db import *


def encryptMainPass(password):
    # TODO - encriptar password
    ecn_pass = password
    return ecn_pass



def decryptMainPass(password):
    # TODO - deencriptar password
    dec_pass = password
    return dec_pass


clear = lambda: os.system('cls')


if os.path.isfile(db_file):

    while True: 
        
        password = str(input("Enter password: "))
        #TODO - encriptar el password
        ep = encryptMainPass(password)
        
        #TODO - confirmar el password en la db
        if login(ep):
            break
        else:
            print("password incorrecto")
            
    clear()

    while True:
        #TODO - todo lo de encriptar
        
        choice = int(input(
            "1. Presiona '1' para salir.\n"))
        clear()
        if choice == 1:
            exit()
        else:
            print("no valido, intenta de nuevo") 
else:
    while True:
        clear()
        password = str(input("Ingrese la clave maestra: "))
        repassword = str(input("Confirm clave: "))
        if password == repassword:
            break
        else:
            print("Los passwords no coinciden!")

    
    #encripta el password principal
    ep = encryptMainPass(password)

    register(ep)

    print("Por favor reinicie el programa")
    time.sleep(15)



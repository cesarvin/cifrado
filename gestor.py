import os
import os.path
from os import listdir
from os.path import isfile, join
import time

from db import *
from Crypto.Cipher import AES


def encryptMainPass(password):
    # TODO - encriptar password
    ecn_pass = password
    return ecn_pass



def decryptMainPass(password):
    dec_pass = password
    return dec_pass

def encryptPasswords(webpage, password):
    encrypted = password.encode('utf8')
    data = webpage.encode('utf8')
    cipher = AES.new(encrypted, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data)
    print("Parte Cifrada")
    print("Llave: " + str(encrypted))
    print("Nonce: " + str(nonce))
    print("Ciphertext: " + str(ciphertext))
    print("Mac - tag: " + str(tag))
    return encrypted, data, cipher, nonce, ciphertext, tag

def decryptPasswords(webpage, nonce, ciphertext, tag):
    decrypted = webpage.encode('utf8')
    cipher = AES.new(decrypted, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        print("La contraseña es: ", plaintext)
    except ValueError:
        print("La llave no es la misma")





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
            "1. Presiona '1' para salir.\n"
            "2. Presiona '2' para ingresa una nueva contraseña\n"))
        clear()
        if choice == 1:
            exit()
        elif choice == 2:
            webpage = input('Ingrese el nombre del sitio\n')
            password = input('Ingrese la contraseña que desea guardar\n')

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



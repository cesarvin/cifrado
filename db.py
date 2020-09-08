import sqlite3
from sqlite3 import Error

db_file = 'storage.db'

def conection(db_file):
    cnn = None
    try: 
        #coneccion a la db, la crea si no existe
        cnn = sqlite3.connect(db_file)
        return cnn

    except Error as e:
        print (e)
    return cnn


def createSystemTables(cnn):
    try: 
        #coneccion a la db, la crea si no existe
        c = cnn.cursor()
        #crea la tabla para la clave principal
        c.execute("""CREATE TABLE main_pass (password text);""")
        
        #TODO: 

    except Error as e:
        print (e)


def insertMainPass(cnn, password):
    try:
        c = cnn.cursor()
        c.execute("INSERT INTO main_pass(password) VALUES(?)", (password,))

    except Error as e: 
        print(e)

def register(password):
    
    try: 
        #coneccion a la db, la crea si no existe
        cnn = conection(db_file)
        
        createSystemTables(cnn)

        insertMainPass(cnn, password)

        cnn.commit()

        cnn.close()

    except Error as e:
        print (e)
    finally:
        if cnn:
            cnn.close()

def login(password):
    logged = False
    try: 
        cnn = conection(db_file)
        c = cnn.cursor()
        #consulta si el password está en la db
        c.execute("""SELECT password FROM main_pass WHERE password=?""", (password,))
        #c.execute("SELECT * FROM main_pass ")
        
        rows = c.fetchall()
        
        for row in rows: 
            if row[0] == password:
                logged= True
        
    except Error as e:
        print (e)
    finally:
        if cnn:
            cnn.close()

    return logged
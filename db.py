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
        c.execute("""CREATE TABLE All_info (Page text,pass text);""")

        #TODO: 

    except Error as e:
        print (e)


def Set_Values(site, password):
    try:
        #coneccion a la db, la crea si no existe
        
        # if (Find_Values(site,1)== None):
        if (Find_Values(site)== None):
            op = input ("El sitio ya existe , desea actualizarlo?(1=si/2=no) ")
            if (op==1):
                
                cnn = conection(db_file)

                c = cnn.cursor()
                c.execute("INSERT INTO All_info (Page,pass) VALUES(?,?)", (site,password,))
                cnn.commit()

                cnn.close()
            else:
                print ("no se ha modificado ningun registro")
            
        else:
            cnn = conection(db_file)

            c = cnn.cursor()
            c.execute("INSERT INTO All_info (Page,pass) VALUES(?,?)", (site,password,))
            cnn.commit()

            cnn.close()

    except Error as e: 
        print(e)


def Find_Values(site, acc):       
    try:
        #coneccion a la db, la crea si no existe
        cnn = conection(db_file)
               

        c = cnn.cursor()

        c.execute("SELECT pass FROM All_info WHERE Page = ?", (site,))
        data=c.fetchall()
        if len(data)==0:

            # if (acc==0):
            print('There is no component named %s'%site)
           
            return True
        else:
            print('El registro existe -- siguiendo con la operacion ')
            #if (acc==0):
                
            password = str(data[0])
            print ('Password is ', password[2:-3])
            return None
        cnn.commit()

        cnn.close()

        
    except Error as e: 
        print(e)

def Delete_values(site):
    
    try:
        
        #coneccion a la db, la crea si no existe
        
        if (Find_Values(site,1)!= None):
            print ("El sitio no existe")
            return False
        else:
            cnn = conection(db_file)

            c = cnn.cursor()
            c.execute("""DELETE from All_info where Page = ?""", (site,))
            cnn.commit()

            cnn.close()
            print ("Se elimino satisfactoriamente el registro del sitio ", site)
            return True

    except Error as e: 
        print(e)

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
        #consulta si el password est� en la db
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

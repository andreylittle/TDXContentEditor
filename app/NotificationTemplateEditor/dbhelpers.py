import sqlite3
from sqlite3 import Error
import os

def getDataFromDB(template_id):
    cwd = os.getcwd()
    conn = sqlite3.connect(f'{cwd}/templates.sqlite')
    try:
        cursor = conn.cursor()
        cursor.execute("Select * FROM templates WHERE template_id = ?", (template_id,))
        result = cursor.fetchall()
        if len(result) == 0:
            print("Result Did Not Exist")
            return False
        else:
            print(result[0][1])
            print("conenction successful")
            return result[0][1]


    except Error as e:
        print(e)
        return False
    finally:
        conn.close()

def addNewUUIDtoDB(template_id,template_content):
    cwd = os.getcwd()
    conn = sqlite3.connect(f'{cwd}/templates.sqlite')
    try:
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO templates (template_id, template_content) 
                                  VALUES (?, ?)''', (template_id, template_content))
        conn.commit()
        return True
    except Error as e:
        conn.rollback()
        print(e)
        return False
    finally:
        conn.close()

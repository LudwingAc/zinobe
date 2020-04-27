import datetime
import requests
import random
import hashlib
import pandas as pd
import sqlite3
import json

def encryptLan(lan):
    m = hashlib.sha1()
    m.update(lan.encode('utf-8'))
    return m.hexdigest()

def getlanguages(paises, pais):
    for i in paises:
        if i["name"]==pais:
            for lan in i["languages"]:
                return encryptLan(lan["name"])

def construction(df):
    for i in regiones:
        if i["region"] not in listRegiones and i["region"]!="":
            listRegiones.append(i["region"])
            start = datetime.datetime.now()
            responsePaises = requests.request("GET", "https://restcountries.eu/rest/v2/region/" + i["region"], headers=headers)
            paises = responsePaises.json()
            pais = (random.choice(paises)["name"])
            idioma = getlanguages(paises, pais)
            end = datetime.datetime.now()
            e = end - start
            a_row = pd.Series([i["region"], pais, idioma, e])
            row_df = pd.DataFrame([a_row])
            df = pd.concat([row_df, df])
    print(df)
    tiempo_total = float(str(df[[3]].sum().item())[13:])
    promedio = float(str(df[[3]].mean().item())[13:])
    min = float(str(df[[3]].min().item())[13:])
    max = float(str(df[[3]].max().item())[13:])
    dbRegister(tiempo_total, promedio, min, max)

def dbRegister(tiempo_total, promedio, min, max):
    try:
        sqliteConnection = sqlite3.connect("db")
        cursor = sqliteConnection.cursor()
        print("Conectado a la base de datos")
        count = cursor.execute("insert into main.tiempos (tiempo_total, promedio, min, max) values (?, ?, ?, ?)", (tiempo_total, promedio, min, max))
        sqliteConnection.commit()
        dat = cursor.execute("select * from main.tiempos")
        consulta = dat.fetchall()
        js = []
        for i in consulta:
            js.append({'tiempo_total':i[1], 'promedio':i[2], 'min':i[3], 'max':i[4]})
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump({'items':js}, f, ensure_ascii=False, indent=4)
        print("Datos registrados", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("No se ingresaron datos en la BD", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("Desconectado de la BD")


url = "https://restcountries-v1.p.rapidapi.com/all"
headers = {
    'x-rapidapi-host': "restcountries-v1.p.rapidapi.com",
    'x-rapidapi-key': "fc45f1ffc3msh4f0a7938a76fd23p1a9169jsncf3e86a79b88"
    }
responseRegiones = requests.request("GET", url, headers=headers)
regiones = responseRegiones.json()
listRegiones = []
a_row = pd.Series([1, 2, 3, 4])
df = pd.DataFrame()
construction(df)
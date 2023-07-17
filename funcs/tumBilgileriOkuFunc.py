import sqlite3

def tumBilgileriOku():
    database_connect = sqlite3.connect("sınıf.db")
    imlec = database_connect.cursor()
    imlec.execute("""SELECT * from araclar""")

    tumBilgileriYazdir = imlec.fetchall()
    for i in tumBilgileriYazdir:
        print(i)

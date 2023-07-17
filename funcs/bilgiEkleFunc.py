import sqlite3
import funcs.texts

def bilgiEkle():
    database_connect = sqlite3.connect("sınıf.db")
    imlec = database_connect.cursor()

    def plakaBilgiEkle():
        global yeniPlaka
        yeniPlaka = str(input(funcs.texts.plakaSorgu)).upper()

    def renkBilgiEkle():
        global yeniRenk
        yeniRenk = input(funcs.texts.renkSorgu).upper()

    def markaBilgiEkle():
        global yeniMarka
        yeniMarka = input(funcs.texts.markaSorgu).upper()

    def modelBilgiEkle():
        global yeniModel
        yeniModel = input(funcs.texts.modelSorgu).upper()

    def kmBilgiEkle():
        global yeniKm
        yeniKm = int(input(funcs.texts.kmSorgu))

    def frigoBilgiEkle():
        global yeniFrigo
        yeniFrigo = str(input(funcs.texts.frigoSorgu).upper())

        if yeniFrigo == ("EVET"):
            yeniFrigo = True
        else:
            if yeniFrigo == ("HAYIR"):
                yeniFrigo = False
            else:
                print("Lütfen Yalnızca 'Evet' ya da 'Hayır' Yazınız.")
                frigoBilgiEkle()

    def isActiveBilgiEkle():
        global yeniIsActive
        yeniIsActive = str(
            input(funcs.texts.isActiveSorgu).upper())

        if yeniIsActive == ("EVET"):
            yeniIsActive = True
        else:
            if yeniIsActive == ("HAYIR"):
                yeniIsActive = False
            else:
                print("Lütfen Yalnızca 'Evet' ya da 'Hayır' Yazınız.")
                isActiveBilgiEkle()

    plakaBilgiEkle()
    renkBilgiEkle()
    markaBilgiEkle()
    modelBilgiEkle()
    kmBilgiEkle()
    frigoBilgiEkle()
    isActiveBilgiEkle()

    imlec.execute("""CREATE TABLE IF NOT EXISTS
       araclar(plaka TEXT,
       renk TEXT,
       marka TEXT,
       model TEXT,
        KM INTEGER,
        frigo TEXT,
        isActive TEXT
        )""")

    imlec.execute("""INSERT INTO araclar VALUES(?, ?, ?, ?, ?, ?, ?)""",(str(yeniPlaka), str(yeniRenk), str(yeniMarka), str(yeniModel), yeniKm, bool(yeniFrigo), bool(yeniIsActive)))

    database_connect.commit()

    database_connect.close()

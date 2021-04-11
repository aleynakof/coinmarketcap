import sqlite3


# con = sqlite3.connect('mycompany.db')
# cursor = con.cursor()
#
# cursor.execute('create table employees(id INTEGER PRIMARY KEY,'
#                'name TEXT, salary REAL,department text,position TEXT)')
# # selection dışındaki her şeyde con.commit koyalım
# con.commit()
# cursor.close()
# con.close()


def vt_baglan():
    con = sqlite3.connect('personel.db')

    return con


def tablo_olustur():
    con = vt_baglan()
    cursor = con.cursor()
    cursor.execute('create table employees(id INTEGER PRIMARY KEY,'
                   'name TEXT, salary REAL,department text,position TEXT)')
    con.commit()
    cursor.close()
    con.close()


def tablo_insert():
    con = vt_baglan()
    cursor = con.cursor()

    cursor.execute("insert into employees values(1,'Bora Yüret','3000','BI','Şef')")
    con.commit()
    cursor.close()


def tablo_insert2():
    con = vt_baglan()
    cursor = con.cursor()
    # another way to insert data
    cursor.execute("insert into employees values(?,?,?,?,?)", (2, 'Aziz Sancar', '15000', 'Lab', 'DNA'))
    con.commit()
    cursor.close()


def tablo_select():
    con = vt_baglan()
    cursor = con.cursor()

    cursor.execute("insert into employees values(1,'Bora Yüret','3000','BI','Şef')")
    con.commit()
    cursor.close()


def tablo_update():
    con = vt_baglan()
    cursor = con.cursor()
    # another way to insert data
    cursor.execute("update employees set salary=? where id=?", (6000, 1))
    con.commit()
    cursor.close()


def tablo_delete():
    con = vt_baglan()
    cursor = con.cursor()
    # (1) olduğunda hata veriyor, (1,) olmalı
    cursor.execute("delete from employees where id=?", (2,))
    con.commit()
    cursor.close()

# burada bir sıkıntı var, kontrol et!!!
# def tablo_drop():
#     con = vt_baglan()
#     cursor = con.cursor()
#     # (1) olduğunda hata veriyor, (1,) olmalı
#     cursor.execute("drop employees")
#     con.commit()
#     cursor.close()


def kayit_sayisi():
    con = vt_baglan()
    cursor = con.cursor()

    cursor.execute('select count(*) from employees')
    data = cursor.fetchone()

    cursor.close()
    con.close()

    return data[0]


sayi = kayit_sayisi()
print('Kayıt sayısı:', sayi)

# tablo_delete()
# tablo_insert()
# tablo_insert2()
# tablo_drop()

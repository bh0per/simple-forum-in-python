import mysql.connector
from tkinter import *
import datetime
import socket

# Połączenie z bazą danych MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="forum_db"
)

mycursor = mydb.cursor()

# Funkcja dodająca post do bazy danych wraz z godziną i adresem IP
def dodaj_post(tresc):
    now = datetime.datetime.now()
    ip = socket.gethostbyname(socket.gethostname())
    sql = "INSERT INTO posts (tresc, godzina, ip) VALUES (%s, %s, %s)"
    val = (tresc, now, ip)
    mycursor.execute(sql, val)
    mydb.commit()

# Funkcja pobierająca wszystkie posty z bazy danych
def pobierz_posty():
    mycursor.execute("SELECT id, tresc, godzina FROM posts")
    posty = mycursor.fetchall()
    return posty

# Funkcja wyświetlająca posty w GUI
def wyswietl_posty():
    for widget in frame.winfo_children():
        widget.destroy()
    posty = pobierz_posty()
    for idx, post in enumerate(posty):
        Label(frame, text=f"Post {post[0]}: {post[1]} (Dodano: {post[2]})").pack()

# Funkcja obsługująca przycisk "Dodaj post"
def dodaj_post_click():
    tresc = entry.get()
    dodaj_post(tresc)
    entry.delete(0, END)
    wyswietl_posty()

# Tworzenie GUI
root = Tk()
root.title("Forum")

frame = Frame(root)
frame.pack()

Label(root, text="Dodaj nowy post:").pack()
entry = Entry(root, width=50)
entry.pack()
Button(root, text="Dodaj post", command=dodaj_post_click).pack()

wyswietl_posty()

root.mainloop()

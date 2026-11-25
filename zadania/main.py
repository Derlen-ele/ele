
from tkinter import *

samogloski = "aeiouyąęóAEIOUYĄĘÓ"
cyfry = "0123456789"

def sprawdz():
    tekst = pole.get()
    s = 0
    w = 0
    sp = 0
    zsc = 0
    c = 0

    for znak in tekst:
        if znak in samogloski:
            s = s + 1
        elif znak in cyfry:
            c = c + 1
        elif znak == " ":
            sp = sp + 1
        elif znak.isalpha():
            w = w + 1
        else:
            zsc = zsc + 1

    wynik.config(text="samogloski: " + str(s) +
                      " wspolgloski: " + str(w) +
                      " spacje: " + str(sp) +
                      "  znaki specjalne: " + str(zsc) +
                      "  cyfry: " + str(c))

def wyczysc():
    pole.delete(0, END)
    wynik.config(text="")
    pole.focus()

def max50(*args):
    if len(txt.get()) > 50:
        txt.set(txt.get()[:50])

okno = Tk()
okno.title("Franek Marciniak")
okno.geometry("640x250")
okno.config(bg="lightblue")

napis = Label(okno, text="wpisz tekst (max 50 znakow):", bg="lightblue")
napis.place(x=10, y=10)

txt = StringVar()
txt.trace_add("write", max50)
pole = Entry(okno, textvariable=txt, width=80, bg="white")
pole.place(x=10, y=40)
pole.focus()

przycisk1 = Button(okno, text="sprawdz", command=sprawdz, bg="darkblue", fg="white")
przycisk1.place(x=10, y=60)
przycisk1.place(x=10, y=80)

przycisk2 = Button(okno, text="wyczysc", command=wyczysc, bg="darkblue", fg="white")
przycisk2.place(x=80, y=80)

wynik = Label(okno, text="", bg="lightblue", fg="blue", font=("Arial", 10))
wynik.place(x=10, y=200)

okno.mainloop()
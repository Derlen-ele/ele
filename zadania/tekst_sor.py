import tkinter as tk
from tkinter import ttk

SAMOGLOSKI = "aeiouyąęóAEIOUYĄĘÓ"
CYFRY = "0123456789"


def analizuj(tekst: str):
    samogloski = sum(1 for c in tekst if c in SAMOGLOSKI)
    cyfry = sum(1 for c in tekst if c in CYFRY)
    spacje = sum(1 for c in tekst if c == " ")
    litery = sum(1 for c in tekst if c.isalpha())
    wspolgloski = litery - samogloski
    specjalne = len(tekst) - litery - cyfry - spacje
    return samogloski, wspolgloski, spacje, specjalne, cyfry


def ogranicz_dlugosc(entry_text):
    # limit 50 znakow
    if len(entry_text.get()) > 50:
        entry_text.set(entry_text.get()[:50])


def sprawdz():
    tekst = wejscie.get()
    s, w, sp, zsc, cy = analizuj(tekst)
    wynik_label.config(
        text=(f"Samogłoski: {s}   |   Współgłoski: {w}   |   Spacje: {sp}   |   "
              f"Znaki specjalne: {zsc}   |   Cyfry: {cy}")
    )


def wyczysc():
    wejscie.delete(0, "end")
    wynik_label.config(text="")
    wejscie.focus()


root = tk.Tk()
root.title("Analizator ciągu znaków")
root.geometry("620x240")
root.resizable(False, False)

ttk.Label(root, text="Wprowadź ciąg (maks. 50 znaków):", font=("Segoe UI", 11)).pack(anchor="w", padx=10, pady=(10, 2))

entry_text = tk.StringVar()
entry_text.trace_add("write", lambda *_: ogranicz_dlugosc(entry_text))
wejscie = ttk.Entry(root, textvariable=entry_text, font=("Segoe UI", 11), width=60)
wejscie.pack(anchor="w", padx=10, pady=(0, 8))
wejscie.focus()

przyciski = ttk.Frame(root)
przyciski.pack(anchor="w", padx=10, pady=(0, 10))
ttk.Button(przyciski, text="Sprawdź", command=sprawdz).pack(side="left", padx=(0, 8))
ttk.Button(przyciski, text="Wyczyść", command=wyczysc).pack(side="left")

# wynik w lewym dolnym rogu okna
wynik_label = ttk.Label(root, text="", font=("Segoe UI", 11), foreground="#1a4f8a", wraplength=600)
wynik_label.pack(side="bottom", anchor="w", padx=10, pady=15)

root.mainloop()
"""Aplikacja okienkowa Kalkulator.
   Autor: Piotr Frydman.
"""
from tkinter import Tk, Button, Label, Entry
import operator
import sys

calc = Tk()
calc.title("Kalkulator")
calc.geometry('600x400')

l1 = Label(calc, text = "1. liczba")
l1.pack()
e1 = Entry(calc, bd =3)
e1.pack()

l2 = Label(calc, text = "2. liczba")
l2.pack()
e2 = Entry(calc, bd =3)
e2.pack()

"""Wykonywanie operacji matematycznych: dodawanie, odjemowanie, mnożenie i dzielenie."""
def add():
    try:
        a = int(e1.get())
        b = int(e2.get())
        result = operator.add(a, b)
        label.config(text=result)
    except ValueError:
        label.config(text="Proszę podać 2 liczby.")

def sub():
    try:
        a = int(e1.get())
        b = int(e2.get())
        result = (operator.sub(a, b))
        label.config(text=result)
    except ValueError:
        label.config(text="Proszę podać 2 liczby.")

def mul():
    try:
        a = int(e1.get())
        b = int(e2.get())
        result = (operator.mul(a, b))
        label.config(text=result)
    except ValueError:
        label.config(text="Proszę podać 2 liczby.")

def div():
    try:
        a = int(e1.get())
        b = int(e2.get())
        result = (operator.truediv(a, b))
        label.config(text=result)
    except ZeroDivisionError:
        label.config(text="Nie wolno dzielić przez zero !")
    except ValueError:
        label.config(text="Proszę podać 2 liczby.")


def exit_button():
    sys.exit()

"Przypisywanie funkcji do przycisków."
exit_button = Button(calc, text="WYJŚCIE", width=12, command=exit_button)
add_button = Button(calc, text="Dodawanie", width=12, command=add)
sub_button = Button(calc, text="Odejmowanie", width=12, command=sub)
mul_button = Button(calc, text="Mnożenie", width=12, command=mul)
div_button = Button(calc, text="Dzielenie", width=12, command=div)

add_button.pack()
sub_button.pack()
mul_button.pack()
div_button.pack()

result_label = Label(calc, text="Wynik")
result_label.pack(pady=10)
label = Label(calc)
label.pack(pady=5)

exit_button.pack(pady=8)

calc.mainloop()




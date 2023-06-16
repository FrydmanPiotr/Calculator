"""Aplikacja okienkowa Kalkulator.
   Autor: Piotr Frydman.
"""
from tkinter import Tk, Button, Label, Entry
import operator

calc = Tk()
calc.title("Kalkulator")
calc.geometry('400x450')

l1 = Label(calc, text = "1. liczba")
l1.pack()
e1 = Entry(calc, bd =3)
e1.pack()

l2 = Label(calc, text = "2. liczba")
l2.pack()
e2 = Entry(calc, bd =3)
e2.pack()

def calculate(operation):
    try:
        a = int(e1.get())
        b = int(e2.get())
        if operation == "+":
            result = operator.add(a, b)
        elif operation == "-":
            result = operator.sub(a, b)
        elif operation == "*":
            result = operator.mul(a, b)
        elif operation == "/":
            result = operator.truediv(a, b)
        label.config(text=result)
    except ZeroDivisionError:
        label.config(text="Nie wolno dzielić przez zero!")
    except ValueError:
        label.config(text="Proszę podać 2 liczby.")

add_button = Button(calc, text="+", width=6,command=lambda: calculate("+"))
sub_button = Button(calc, text="-", width=6, command=lambda: calculate("-"))
mul_button = Button(calc, text="*", width=6, command=lambda: calculate("*"))
div_button = Button(calc, text="/", width=6, command=lambda: calculate("/"))

add_button.pack()
sub_button.pack()
mul_button.pack()
div_button.pack()

result_label = Label(calc, text="Wynik")
result_label.pack(pady=10)
label = Label(calc)
label.pack(pady=5)

calc.mainloop()

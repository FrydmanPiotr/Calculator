"""Aplikacja okienkowa Kalkulator.
   Autor: Piotr Frydman.
"""
import tkinter as tk
import operator
import time

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kalkulator")
        self.geometry('300x350')

        self.l1 = tk.Label(self, text = "1. liczba")
        self.l1.pack()
        self.e1 = tk.Entry(self, bd =3)
        self.e1.pack()

        self.l2 = tk.Label(self, text = "2. liczba")
        self.l2.pack()
        self.e2 = tk.Entry(self, bd =3)
        self.e2.pack()

        badd = tk.Button(self, text="+", width=6, command=lambda: self.calculate("+"))
        bsub = tk.Button(self, text="-", width=6, command=lambda: self.calculate("-"))
        bmul = tk.Button(self, text="*", width=6, command=lambda: self.calculate("*"))
        bdiv = tk.Button(self, text="/", width=6, command=lambda: self.calculate("/"))

        badd.pack()
        bsub.pack()
        bmul.pack()
        bdiv.pack()

        self.label = tk.Label(self, text="Wynik")
        self.label.pack(pady=10)
        self.outcome = tk.Label(self)
        self.outcome.pack(pady=5)

    def calculate(self, operation):            
        try:
            a = int(self.e1.get())
            b = int(self.e2.get())
            if operation == "+":
                result = operator.add(a,b)
            elif operation == "-":
                result = operator.sub(a, b)
            elif operation == "*":
                result = operator.mul(a, b)
            elif operation == "/":
                if b == 0:
                    self.outcome.config(text="Nie wolno dzielić przez zero!")
                    return
                
                result = operator.truediv(a, b)
            self.outcome.config(text=result)
            
        except ValueError:
            self.outcome.config(text="Proszę podać 2 liczby.")
            
calc = Calculator()
calc.mainloop()

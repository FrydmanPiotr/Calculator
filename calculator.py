"""Aplikacja okienkowa Kalkulator.
   Autor: Piotr Frydman.
"""
import tkinter as tk
from tkinter import messagebox
import operator


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kalkulator")
        self.geometry('300x350')
        self.memory = []

        self.entry = tk.Entry(self, bd =3)
        self.entry.pack()

        buttons = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
        }

        for symbol, op in buttons.items():
            btn = tk.Button(self, text=symbol, width=6, command=lambda op=op: self.calculate(op))
            btn.pack()

    def calculate(self, operation):            
        try:
            num = int(self.entry.get())
            self.memory.append(num)
            self.clear_entries()
            
            if len(self.memory) == 2:
                result = operation(self.memory[0], self.memory[1])

                if operation == operator.truediv and self.memory[1] == 0:
                    messagebox.showerror("Błąd", "Nie wolno dzielić przez zero!")
                    self.clear_entries()
                else:
                    self.clear_entries()
                    self.entry.insert(0, result)
                    self.memory = []
            
        except ValueError:
            messagebox.showerror("Błąd", "Proszę podać poprawne liczby.")
            
    def clear_entries(self):
        self.entry.delete(0, 'end')
        
calc = Calculator()
calc.mainloop()

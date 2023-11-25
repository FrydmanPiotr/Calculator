"""
Aplikacja okienkowa Kalkulator.
Autor: Piotr Frydman.
"""
import tkinter as tk
from tkinter import messagebox
import operator

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kalkulator")
        self.geometry('250x200+500+250')
        self.resizable(False, False)
        self.memory = []
        
        #położenie elementów w oknie
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3,weight=1)
        self.rowconfigure(4,weight=1)
        
        self.entry = tk.Entry(self,justify="right",bd =3,width=20,
                              font=('Arial',9))
        self.entry.grid(column=3,row=0)
        self.entry.focus()
        
        buttons = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
        }
        i=1
        for i, (symbol, op) in enumerate(buttons.items(), start=0):
            btn = tk.Button(self, text=symbol, command=lambda op=op:
                            self.calculate(op),width=4)
            i+=1
            btn.grid(column=3,row=i)

        btn1 = tk.Button(self,text="1",width=4, command=lambda:self.set_text("1"))
        btn1.grid(column=0,row=1)
        btn2 = tk.Button(self,text="2",width=4, command=lambda:self.set_text("2"))
        btn2.grid(column=1,row=1)
        btn3 = tk.Button(self,text="3",width=4, command=lambda:self.set_text("3"))
        btn3.grid(column=2,row=1)
        
        btn4 = tk.Button(self,text="4",width=4, command=lambda:self.set_text("4"))
        btn4.grid(column=0,row=2)
        btn5 = tk.Button(self,text="5",width=4, command=lambda:self.set_text("5"))
        btn5.grid(column=1,row=2)
        btn6 = tk.Button(self,text="6",width=4,command=lambda:self.set_text("6"))
        btn6.grid(column=2,row=2)

        btn7 = tk.Button(self,text="7",width=4,command=lambda:self.set_text("7"))
        btn7.grid(column=0,row=3)
        btn8 = tk.Button(self,text="8",width=4,command=lambda:self.set_text("8"))
        btn8.grid(column=1,row=3)
        btn9 = tk.Button(self,text="9",width=4,command=lambda:self.set_text("9"))
        btn9.grid(column=2,row=3)

        result_btn = tk.Button(self, text=".", width=4,command=lambda:self.set_text("."))
        result_btn.grid(column=0,row=4)
        
        clear_btn = tk.Button(self, text="C", width=4,command=self.clear_entry)
        clear_btn.grid(column=1,row=4)
            
    def calculate(self, operation):            
        try:
            number = float(self.entry.get())
            self.memory.append(number)
            self.clear_entry()
            
            if len(self.memory) == 2:
                result = operation(self.memory[0], self.memory[1])

                if operation == operator.truediv and self.memory[1] == 0:
                    messagebox.showerror("Błąd", "Nie wolno dzielić przez zero!")
                    self.clear_entry()
                else:
                    self.clear_entry()
                    self.entry.insert(0,result)
                    self.memory = []
            
        except ValueError:
            messagebox.showerror("Błąd", "Proszę podać poprawne liczby.")
    
    def set_text(self,text):
        cursor_position = self.entry.index(tk.INSERT)
        self.entry.insert(cursor_position,text)
        
    def clear_entry(self):
        self.entry.delete(0, tk.END)
        
calc = Calculator()
calc.mainloop()

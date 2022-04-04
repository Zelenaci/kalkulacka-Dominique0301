import math
from importlib.metadata import PathDistribution
from os.path import basename, splitext
import tkinter as tk
from tkinter import messagebox, IntVar
from tkinter.messagebox import showerror


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Kalkulačka"
    
    
    


    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.geometry("400x400")

        self.vstup =tk.Entry(self)
        self.vstup.grid(row=1,column=1)

        self.dva_operandy = {}
        self.dva_operandy["+"] = lambda a, b: a + b
        self.dva_operandy["-"] = lambda a, b: a - b
        self.dva_operandy["*"] = lambda a, b: a * b
        self.dva_operandy["/"] = lambda a, b: a / b
        self.dva_operandy["//"] = lambda a, b: a // b
        self.dva_operandy["**"] = lambda a, b: a ** b

        self.jeden_operand = {}
        self.jeden_operand["sin"] = math.sin
        self.jeden_operand["cos"] = math.cos
        self.jeden_operand["tg"] = math.tan
        self.jeden_operand["tan"] = math.tan

        self.zasobnik= []

    


    def operace(self,token):
        if token.upper() == "Q":
            exit()
        if token.upper() == "PI":
            self.zasobnik.append(math.pi)
        if token == "+":
            b = self.zasobnik.pop()
            a = self.zasobnik.pop()
            self.zasobnik.append(a + b)
        if token == "-":
            b = self.zasobnik.pop()
            a = self.zasobnik.pop()
            self.zasobnik.append(a - b)
        if token == "*":
            b = self.zasobnik.pop()
            a = self.zasobnik.pop()
            self.zasobnik.append(a * b)
        if token == "**":
            b = self.zasobnik.pop()
            a = self.zasobnik.pop()
            self.zasobnik.append(a ** b)
        if token == "sin":
            a = self.zasobnik.pop()
            self.zasobnik.append(math.sin(a))
        if token == "cos":
            a = self.zasobnik.pop()
            self.zasobnik.append(math.cos(a))





    def operace(self, token):
        if token.upper() == "Q":
            exit()
        if token.upper() == "PI":
            self.zasobnik.append(math.pi)
        if token.upper() == "SW":
            b = self.zasobnik.pop()
            a = self.zasobnik.pop()
            self.zasobnik.append(b)
            self.zasobnik.append(a)
        if token in self.dva_operandy.keys():
            if len(self.zasobnik) >= 2:
                b = self.zasobnik.pop()
                a = self.zasobnik.pop()
                self.zasobnik.append(self.dva_operandy[token](a, b))
            else:
                messagebox.showerror("Chyba", "Počet operandů je nedostačující.")
        if token in self.jeden_operand.keys():
            if len(self.zasobnik) >= 1:
                a = self.zasobnik.pop()
                self.zasobnik.append(self.jeden_operand[token](a))
            else:
                messagebox.showerror("Chyba", "Počet operandů je nedostačující.")


    def zpracuj(self,radek):
        tokeny = radek.split()
        for token in tokeny:
            try:
                self.zasobnik.append(float(token))
            except ValueError:
                self.operace(token)

    def ctu(self, token):
        a = self.vstup.get()

app = Application()
app.mainloop()


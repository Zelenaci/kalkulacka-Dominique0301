import math
from importlib.metadata import PathDistribution
from os.path import basename, splitext
import tkinter as tk
from tkinter import messagebox, IntVar, END
from tkinter.messagebox import showerror

dva_operandy = {}
dva_operandy["+"] = lambda a, b: a + b
dva_operandy["-"] = lambda a, b: a - b
dva_operandy["*"] = lambda a, b: a * b
dva_operandy["/"] = lambda a, b: a / b
dva_operandy["//"] = lambda a, b: a // b
dva_operandy["**"] = lambda a, b: a ** b

jeden_operand = {}
jeden_operand["sin"] = math.sin
jeden_operand["cos"] = math.cos
jeden_operand["tg"] = math.tan
jeden_operand["tan"] = math.tan

class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Kalkulačka"
    
    
    


    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.geometry("400x400")

        self.vstup = tk.Entry(self)
        self.vstup.grid(row=2,column=1,padx=10,pady=10)

        self.listBox = tk.Listbox(self)
        self.listBox.grid(row=3,column=1,padx=10,pady=10)

        self.btn2 = tk.Button(self, text="Vložit", command=self.fce)
        self.btn2.grid()
        #self.bind("<Return>",self.zpracuj())
    

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


    def fce(self):
        self.zpracuj(self.vstup.get())

    def operace(self, token, event=None):
        token = str(self.vstup.get())
        if token in dva_operandy.keys():
            if len(self.zasobnik) >= 2:
                b = self.zasobnik.pop()
                a = self.zasobnik.pop()
                self.zasobnik.append(dva_operandy[token](a, b))
            else:
                messagebox.showerror("Chyba", "Počet operandů je nedostačující.")
        if token in jeden_operand.keys():
            if len(self.zasobnik) >= 1:
                a = self.zasobnik.pop()
                self.zasobnik.append(jeden_operand[token](a))
            else:
                messagebox.showerror("Chyba", "Počet operandů je nedostačující.")
        self.listBox.delete(0,tk.END)
        for token in self.zasobnik:
            self.listBox.insert(END,token)
        
    def zpracuj(self,token):
        try:
            self.zasobnik.append(float(token))
            self.listBox.insert(tk.END,token)
        except ValueError:
            self.operace(self,token)

app = Application()
app.mainloop()


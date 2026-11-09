import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Treeview
from ascii_table import ASCIITable
from custom_exceptions import *

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.window_settings()
        MainContainer(self)
    
    def window_settings(self):
        self.title("Learning Exceptions in Python")
        self.geometry("400x300")

class MainContainer(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
   
        self.config(bg="#1468A8")
        self.pack(expand=True, side=tk.TOP, fill="both", padx=10, pady=10)

        ## data
        self.ascii_table = ASCIITable()


        fr_form_section = tk.Frame(self, padx=10, pady=10)
        lbl_symbol = tk.Label(fr_form_section, text="Enter a symbol: ")
        self.in_symbol = tk.Entry(fr_form_section)
        btn_add_symbol = tk.Button(fr_form_section, text="Add", command=self.add_symbol)
        btn_search = tk.Button(fr_form_section, text="Search", command=self.search_symbol)
        ### form configuration
        fr_form_section.config(bg="#A85414")
        fr_form_section.pack(fill="x")

        lbl_symbol.pack(side=tk.LEFT, padx=5)
        self.in_symbol.pack(side=tk.LEFT, padx=(0, 5))
        btn_add_symbol.pack(side=tk.LEFT, padx=(0, 5))
        btn_search.pack(side=tk.LEFT, padx=(0, 5))
        

        ### table configuration 
        self.table = Treeview(self, columns=("number", "symbol"), show="headings")
        self.table.heading("number", text="Number")
        self.table.heading("symbol", text="Symbol")

        self.table.column("number", width=100, anchor=tk.W)
        self.table.column("symbol", width=100, anchor=tk.W)
        self.table.pack(expand=True,side=tk.TOP,  pady=(10, 10))


    def add_symbol(self):

        symbol = self.in_symbol.get()
        try:
            self.ascii_table.set(symbol)
            self.table.insert(parent="", index="end", values=(self.ascii_table.get(symbol), symbol))
            
        except Exception as e:
            messagebox.showerror("You got an error :p", message=e) 


    def search_symbol(self):
        symbol = self.in_symbol.get()

        try:
            result = self.ascii_table.get(symbol)
            messagebox.showinfo("result", message=f"the number asociated to {symbol} is {result}")

        except TooManyArguments as e:
            messagebox.showerror("too many arguments", "The input should be just one letter") 
        except NullValueError as e:
            messagebox.showerror("null values error", message=e ) 
        except SymbolNotFoundError as e:
            messagebox.showerror("404", message=e)
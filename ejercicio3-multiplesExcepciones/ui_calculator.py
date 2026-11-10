import tkinter as tk
from pages import *
class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.window_settings()
        self.side_bar = tk.Frame(self) 
        self.main_container = MainContainer(self)

        self.btn_calculate_ln = tk.Button(self.side_bar, text="natural logarithm", command=self.open_ln_calculator)
        self.btn_calculate_root = tk.Button(self.side_bar, text="square root", command=self.open_root_calculator)
        self.btn_calculate_slope = tk.Button(self.side_bar, text="Slope", command=self.open_slope_calculator)
        self.btn_calculate_mean = tk.Button(self.side_bar, text="mean point", command=self.open_mean_point_calculator)
        self.btn_calculate_eq_root = tk.Button(self.side_bar, text="cuadratic eq. root", command=self.open_eq_root_calculator)
        self.btn_calculate_new_base = tk.Button(self.side_bar, text="base 10 to base 'b'", command=self.open_base_change_calculator)

        self.side_bar.config(bg="#4779D7")

        self.btn_calculate_ln.pack(padx=5, pady=10)
        self.btn_calculate_root.pack(padx=5, pady=(0,10))
        self.btn_calculate_slope.pack(padx=5, pady=(0, 10))
        self.btn_calculate_mean.pack(padx=5, pady=(0, 10))
        self.btn_calculate_eq_root.pack(padx=5, pady=(0, 10))
        self.btn_calculate_new_base.pack(padx=5, pady=(0, 10))


        self.side_bar.pack(side=tk.LEFT, fill="y", ipadx=5, ipady=10)
        self.main_container.pack(side=tk.RIGHT, fill="both", expand=True)     

    def window_settings(self):
        self.title("Raising Exceptions in Python")
        self.geometry("500x250")

    def open_ln_calculator(self):
        self.main_container.clean_frame()
        CalculatorLnPage(self.main_container)

    def open_root_calculator(self):
        self.main_container.clean_frame()
        CalculatorRootPage(self.main_container)

    def open_slope_calculator(self):
        self.main_container.clean_frame()
        CalculatorSlopePage(self.main_container)

    def open_mean_point_calculator(self):
        self.main_container.clean_frame()
        CalculatorMeanPage(self.main_container)

    def open_eq_root_calculator(self):
        self.main_container.clean_frame()
        CalculatorEqRootPage(self.main_container)

    def open_base_change_calculator(self):
        self.main_container.clean_frame()
        CalculatorNewBase(self.main_container)

class MainContainer(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        # self.config(bg="#D7A547")

    def clean_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

import tkinter as tk
from pages import zeroDivitionPage, outOfLimitPage, NumberFormatPage
class CatchErrorWindow(tk.Tk):
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
        self.pack(expand=True)
        self.add_buttons()

    def add_buttons(self):
        div_error_btn = tk.Button(self, text="launch zero division error test", command=self.open_0_division_error_window) 
        index_error_btn = tk.Button(self, text="Launch out of limit index error page", command=self.open_out_range_index_window) 
        bad_format_btn = tk.Button(self, text="Launch string to integer error page", command=self.open_bad_formatting_window) 
        div_error_btn.pack(pady=10, padx=20)
        index_error_btn.pack(pady=10, padx=20)
        bad_format_btn.pack(pady=10, padx=20)

    def open_0_division_error_window(self):
        zeroDivitionPage(self)

    def open_out_range_index_window(self):
        outOfLimitPage(self)

    def open_bad_formatting_window(self):
        NumberFormatPage(self)

    def clean_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def back_main_menu(self):
        self.clean_frame()
        self.add_buttons()
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Treeview
from custom_exceptions import *
from coding_marathon_team import CodingMarathonTeam
from pages import AddTeamMembersPage, TeamInformationPage

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
        

        self.coding_team = None
        
        self.config(bg="#1468A8")
        self.pack(expand=True, side=tk.TOP, fill="both", padx=10, pady=10)

        # AddTeamMembersPage(self, self.coding_team)
        TeamInformationPage(self) 

    def clean_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

 
    def open_team_members_form(self):
        AddTeamMembersPage(self)
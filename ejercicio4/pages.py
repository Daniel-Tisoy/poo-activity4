import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Treeview
from custom_exceptions import *
from coding_marathon_team import CodingMarathonTeam
class AddTeamMembersPage():
    def __init__(self, frame):
        self.master = frame

                # get data to update
        self.coder_name_var = tk.StringVar()

        fr_form_section = tk.Frame(frame, padx=10, pady=10)
        lbl_symbol = tk.Label(fr_form_section, text="Enter coder name, i.e 'jhon doe': ")

        self.in_full_name = tk.Entry(fr_form_section, textvariable=self.coder_name_var)
        btn_add_coder = tk.Button(fr_form_section, text="Add", command=self.add_coder)
        ### form configuration
        fr_form_section.config(bg="#A85414")
        fr_form_section.pack(fill="x")

        lbl_symbol.pack(side=tk.LEFT, padx=5)
        self.in_full_name.pack(side=tk.LEFT, padx=(0, 5))
        btn_add_coder.pack(side=tk.LEFT, padx=(0, 5))
        

        ### table configuration 
        self.table = Treeview(frame, columns=("name", "lastname"), show="headings")
        self.table.heading("name", text="Name")
        self.table.heading("lastname", text="lastname")

        self.table.column("name", width=100, anchor=tk.W)
        self.table.column("lastname", width=100, anchor=tk.W)
        self.table.pack(side=tk.RIGHT,  pady=(10, 10))
        
        #show team inf
        fr_team = tk.Frame(frame)
        lbl_team_name = tk.Label(fr_team, text=f"Team Name: {frame.coding_team.team_name}")
        lbl_college = tk.Label(fr_team, text=f"College: {frame.coding_team.college}")
        lbl_coding_language = tk.Label(fr_team, text=f"Coding language: {frame.coding_team.programming_language}")
        lbl_team_size = tk.Label(fr_team, text=f"Max team members: {frame.coding_team.max_team_size}")

        fr_team.pack(side=tk.LEFT)
        lbl_team_name.pack()
        lbl_college.pack()
        lbl_coding_language.pack()
        lbl_team_size.pack()


    def add_coder(self):
        full_name = self.coder_name_var.get()

        try:
            if len(full_name.split(" ")) > 2 or len(full_name) == 0:
                raise InvalidInputError("Just enter a name and a lastname separated by space")

            name, lastname = full_name.split(" ")

            self.master.coding_team.join_programmer(name, lastname)
            self.table.insert(parent="", index="end", values=(name.capitalize(), lastname.capitalize()))

        except InvalidInputError as e:
            messagebox.showerror("Invalid input", str(e))
        except FullTeamError as e:
            messagebox.showerror("Full team", str(e))
        except TooLongStringError as e:
            messagebox.showerror("Too long input", str(e))
        except Exception as e:
            messagebox.showerror("unexpected error", str(e))
        finally:
            self.coder_name_var.set("")

class TeamInformationPage():
    def __init__(self, frame): 
        self.master = frame
        
        fr_team_name = tk.Frame(frame)
        fr_team_name.config(bg="#1468A8")
        self.lbl_team_name = tk.Label(fr_team_name, text="Team name")
        self.txt_team_name = tk.Entry(fr_team_name)

        fr_team_name.pack(fill="x")
        self.lbl_team_name.pack(side=tk.LEFT)
        self.txt_team_name.pack(side=tk.LEFT)

        fr_college = tk.Frame(frame)
        fr_college.config(bg="#1468A8")
        self.lbl_college = tk.Label(fr_college, text="College")
        self.txt_college = tk.Entry(fr_college)

        fr_college.pack(fill="x")
        self.lbl_college.pack(side=tk.LEFT)
        self.txt_college.pack(side=tk.LEFT)

        fr_coding_lang = tk.Frame(frame)
        fr_coding_lang.config(bg="#1468A8")
        self.lbl_coding_lang = tk.Label(fr_coding_lang, text="Coding language")
        self.txt_coding_lang= tk.Entry(fr_coding_lang)

        fr_coding_lang.pack(fill="x")
        self.lbl_coding_lang.pack(side=tk.LEFT)
        self.txt_coding_lang.pack(side=tk.LEFT)

        btn_set_info = tk.Button(frame, text="Set info", command=self.set_team_info)
        btn_set_info.pack()

    def set_team_info(self):
        try: 
            team_name = self.txt_team_name.get()
            college = self.txt_college.get()
            coding_lang = self.txt_coding_lang.get()

            from coding_marathon_team import Programmer
            Programmer.check_field(team_name, "Team Name") 
            Programmer.check_field(college.replace(" ", ""), "College") 

            if len(coding_lang) == 0:
                raise InvalidInputError("Enter a coding Language")

            self.master.coding_team = CodingMarathonTeam(team_name, college, coding_lang) 

            self.master.clean_frame()
            self.master.open_team_members_form()

        except InvalidInputError as e:
            messagebox.showerror("Invalid input", str(e))
        except FullTeamError as e:
            messagebox.showerror("Full team", str(e))
        except TooLongStringError as e:
            messagebox.showerror("Too long input", str(e))
        except Exception as e:
            messagebox.showerror("unexpected error", str(e))

        
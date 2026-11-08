from tkinter import Button, Label, Entry, TOP, LEFT, BOTTOM, messagebox
class defaultPage:
    """ adds navigation buttons """
    def __init__(self, master_frame):
        master_frame.clean_frame() # empty frame to put the following widgets
        back_main_menu = Button(master_frame, text="Back to main menu",command=master_frame.back_main_menu)
        back_main_menu.pack(padx=20, pady=10)

class zeroDivitionPage(defaultPage):
    def __init__(self, master_frame):
        super().__init__(master_frame)
        ## basic calculator:
        lbl_section_title = Label(master_frame, text="dividing by zero: ")
        self.txt_first_number = Entry(master_frame)
        lbl_separator = Label(master_frame, text="/")
        self.txt_second_number= Entry(master_frame)
        self.txt_second_number.insert(0, "0")
        self.txt_second_number.config(state="disabled")
        btn_calculate = Button(master_frame, text="Calculate", command=self.calculate)

        lbl_section_title.pack(side=TOP)
        self.txt_first_number.pack(side=LEFT, padx=4)
        lbl_separator.pack(side=LEFT, padx=4)
        self.txt_second_number.pack(side=LEFT, padx=4)
        btn_calculate.pack(side=BOTTOM, padx=4)

    def calculate(self):
        try:
            dividend = int(self.txt_first_number.get())
            divider = int(self.txt_second_number.get())
            result = dividend / divider
            print(result)

        except ZeroDivisionError as e:
            messagebox.showerror(title="zero division", message="Operation error: " + str(e))

        except ValueError as e:
            messagebox.showerror(title="not decimal input", message="Format error, please enter decimal numbers" )

class outOfLimitPage(defaultPage):
    def __init__(self, master_frame):
        super().__init__(master_frame)
        self.master_frame = master_frame
        lbl_section_title = Label(master_frame, text="getting index out of range in string: ")
        self.txt_user_input= Entry(master_frame)
        btn_calculate = Button(master_frame, text="Get Last char index (error)", command=self.calculate)

        lbl_section_title.pack(side=TOP)
        self.txt_user_input.pack(side=LEFT, padx=4)
        btn_calculate.pack(side=BOTTOM, padx=4)


    def calculate(self):
        word = self.txt_user_input.get()
        try:
            lastIndexerror = word[len(word)]
        except IndexError as e:
            message = str(e) + f": you're getting index {len(word)} the right index is {len(word) - 1}"
            messagebox.showerror(title="index error", message=message)

        finally:
            print(f"the right index is {len(word) - 1}")

class NumberFormatPage(defaultPage):
    def __init__(self, master_frame):
        super().__init__(master_frame)
        self.master_frame = master_frame
        lbl_section_title = Label(master_frame, text="formating string to integer: ")
        self.txt_user_input= Entry(master_frame)
        btn_calculate = Button(master_frame, text="convert to integer", command=self.calculate)

        lbl_section_title.pack(side=TOP)
        self.txt_user_input.pack(side=LEFT, padx=4)
        btn_calculate.pack(side=LEFT, padx=4)


    def calculate(self):
        word = self.txt_user_input.get()
        try:
            numberFormatError= int(word) 
            lbl_result = Label(self.master_frame, text=f"{word} +  10 is {numberFormatError + 10}" )
            lbl_result.pack(side=BOTTOM)
        except ValueError as e:
            messagebox.showerror(title="not decimal input", message="Format error, please enter decimal numbers" )

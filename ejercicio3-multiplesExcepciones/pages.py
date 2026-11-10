from tkinter import Label, LEFT, TOP, Entry, Button, messagebox, Frame
from calculations import NumericOperations, CartesianPoint
from custom_exceptions import InvalidInputError

class CalculatorLnPage():
    def __init__(self, frame):
        self.lbl_input = Label(frame, text="Enter the number: ")
        self.txt_input_number = Entry(frame)
        self.btn_calculate = Button(frame, text="Calculate Ln", command=self.calculate)

        self.lbl_input.pack(side=LEFT, padx=5)
        self.txt_input_number.pack(side=LEFT, padx=(0, 5))
        self.btn_calculate.pack(side=LEFT, padx=(0, 5))

    def calculate(self):
        try:
            input_number = self.txt_input_number.get()
            result = NumericOperations.calculate_natural_logaritm(float(input_number))
            messagebox.showinfo("Result",result )

        except ArithmeticError as e:
            messagebox.showerror("Invalid Input", e)

        except ValueError as e:
            messagebox.showerror("Input Error", "Input must be a real number, not a string.") 
        # this is if I'm not considered an error
        except Exception as e:
            messagebox.showerror("You got an unexpected error", str(e) + " Please send me an email with the screenshoot :)")

class CalculatorRootPage():
    def __init__(self, frame):
        self.lbl_input = Label(frame, text="Enter the number: ")
        self.txt_input_number = Entry(frame)
        self.btn_calculate = Button(frame, text="Calculate square root", command=self.calculate)

        self.lbl_input.pack(side=LEFT, padx=5)
        self.txt_input_number.pack(side=LEFT, padx=(0, 5))
        self.btn_calculate.pack(side=LEFT, padx=(0, 5))

    def calculate(self):
        try:
            input_number = self.txt_input_number.get()
            result = NumericOperations.calculate_square_root(float(input_number))
            messagebox.showinfo("Result",result)

        except ArithmeticError as e:
            messagebox.showerror("Invalid Input", e)

        except ValueError as e:
            messagebox.showerror("Input Error", "Input must be a real number, not a string.") 
        # this is if I'm not considered an error
        except Exception as e:
            messagebox.showerror("You got an unexpected error", str(e) + " Please send me an email with the screenshoot :)")

class PointCalculatorsBase():
    def __init__(self, frame, description, btn_text):
        
        self.lbl_title = Label(frame, text=f"Enter the points to calculate the {description}")
        self.fr_p1 = Frame(frame)
        self.lbl_p1 = Label(self.fr_p1, text="point 1: x,y ")
        self.txt_p1 = Entry(self.fr_p1)

        self.fr_p2 = Frame(frame)
        self.lbl_p2 = Label(self.fr_p2, text="point 2: x,y ")
        self.txt_p2 = Entry(self.fr_p2)

        self.btn_calculate = Button(frame, text=btn_text, command=self.calculate)

        self.lbl_title.pack(side=TOP)
        self.fr_p1.pack(fill="x")
        self.fr_p2.pack(fill="x")
        self.lbl_p1.pack(side=LEFT)
        self.txt_p1.pack(side=LEFT)
        self.lbl_p2.pack(side=LEFT)
        self.txt_p2.pack(side=LEFT)
        self.btn_calculate.pack(side=TOP)

    def calculate(self, operation):
        try:
            str_p1 = self.txt_p1.get()
            if len(str_p1) == 0:
                raise ValueError("Enter a valid point 1 x,y")
            str_p1 = tuple(str_p1.split(","))
            point1 = CartesianPoint(str_p1).point

            str_p2 = self.txt_p2.get()
            if len(str_p2) == 0:
                raise ValueError("Enter a valid point 2 x,y")
            str_p2 = tuple(str_p2.split(","))
            point2 = CartesianPoint(str_p2).point

            result = operation(point1, point2)

            messagebox.showinfo("Result", result)

        except Exception as e:
            messagebox.showerror("you got an error", str(e))

class CalculatorSlopePage(PointCalculatorsBase):
    def __init__(self, frame):
        super().__init__(frame, "slope", "calculate slope")

    def calculate(self):
        super().calculate(NumericOperations.calculate_slope)

class CalculatorMeanPage(PointCalculatorsBase):
    def __init__(self, frame):
        super().__init__(frame, "mean point", "calculate Mean point")

    def calculate(self):
        super().calculate(NumericOperations.calculate_mean_point)

class CalculatorEqRootPage():
    def __init__(self, frame):
        
        self.lbl_title = Label(frame, text="Enter the formula")
        self.fr_formula = Frame(frame)

        self.txt_a = Entry(self.fr_formula, width=5)
        self.label_a= Label(self.fr_formula, text="x^2 +")
        self.txt_b = Entry(self.fr_formula, width=5)
        self.label_b = Label(self.fr_formula, text="x +")
        self.txt_c = Entry(self.fr_formula, width=5)
        self.label_0 = Label(self.fr_formula, text="= 0")

        self.btn_calculate = Button(frame, text="calculate", command=self.calculate)
        self.lbl_title.pack()

        self.fr_formula.pack(pady=10)
        self.txt_a.pack(side=LEFT)
        self.label_a.pack(side=LEFT, padx=(0, 3))
        self.txt_b.pack(side=LEFT, padx=(0, 3))
        self.label_b.pack(side=LEFT, padx=(0, 3))
        self.txt_c.pack(side=LEFT, padx=(0, 3))
        self.label_0.pack(side=LEFT, padx=(0, 3))

        self.btn_calculate.pack(side=TOP)

    def calculate(self):
        try:

            a = self.txt_a.get()
            b = self.txt_b.get()
            c = self.txt_c.get()

            result = NumericOperations.calculate_cuadratic_eq_root(a, b, c)
            messagebox.showinfo("Result", result)
        except ArithmeticError as e:
            messagebox.showwarning("couldn't calculate", str(e))
        except Exception as e:
            messagebox.showerror("An error just ocurred", str(e))

class CalculatorNewBase():
    def __init__(self, frame):
        self.lbl_title = Label(frame, text="Enter the number and the base")

        self.fr_number= Frame(frame)
        self.lbl_number = Label(self.fr_number, text="number: ")
        self.txt_number = Entry(self.fr_number)

        self.fr_base= Frame(frame)
        self.lbl_base = Label(self.fr_base , text="Base: ")
        self.txt_base= Entry(self.fr_base)

        self.btn_calculate = Button(frame, text="Convert", command=self.calculate)

        self.lbl_title.pack(side=TOP)
        self.fr_number.pack(fill="x")
        self.fr_base.pack(fill="x")
        self.lbl_number.pack(side=LEFT)
        self.txt_number.pack(side=LEFT)
        self.lbl_base.pack(side=LEFT)
        self.txt_base.pack(side=LEFT)
        self.btn_calculate.pack(side=TOP)

    def calculate(self):
        try:
            number = self.txt_number.get() 
            base = self.txt_base.get() 

            result = NumericOperations.calculate_decimal_base_b(number, base)

            messagebox.showinfo("Result", result)

        except InvalidInputError as e:
            messagebox.showerror("Enter right values", str(e))
        except Exception as e:
            messagebox.showerror("Error :(", str(e))
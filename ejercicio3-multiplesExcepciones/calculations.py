import math
from custom_exceptions import *
class NumericOperations:
    @staticmethod
    def calculate_natural_logaritm(number):
        if number <= 0:
            raise ArithmeticError("The number must be a positive number greater than 0.") 
        result = math.log(number)

        return f"Result = {round(result, 4)} aprox."

    @staticmethod
    def calculate_square_root(number):
        if number < 0:
            raise ArithmeticError("The number must be a positive number.") 
        result = math.sqrt(number)
        return f"Result = {result}"

    @staticmethod
    def calculate_slope(p1: CartesianPoint, p2: CartesianPoint):
        slope = (p2[0] - p1[0]) / (p2[1] - p1[1])
        return f"The slope is: {slope}"
    
    @staticmethod
    def calculate_mean_point(p1:CartesianPoint, p2: CartesinaPoint):
        mean_point = (str(sum((p1[0], p2[0])) / 2), str(sum((p1[1], p2[1])) / 2))

        result = CartesianPoint(mean_point).point
        return f"the mean point is: {result}"

    @staticmethod
    def calculate_cuadratic_eq_root(a, b, c):
        if len(a) == 0 or len(b) == 0 or len(c) == 0:
            raise InvalidInputError("Enter real numbers, if argument does not exist just enter 0")
        try:
            a = float(a)
            b = float(b)
            c = float(c)
        except ValueError as e:
            raise ValueError("Please enter valid numbers. " + str(e))
        except Exception as e:
            raise e
    
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            raise ArithmeticError("Not real roots")
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"x = {root1}, x = {root2}"

    @staticmethod
    def calculate_decimal_base_b(decimal_number, base):
        """ calculate decimal number in base b where b is between 2 and 9 and a natural number"""
    
        if not base.isdecimal():
            raise InvalidInputError("The base number must be a integer number")
        if int(base) > 9 or int(base) < 2:
            raise InvalidInputError("The Base must be a natural number between 2 and 9")
        if not decimal_number.isdecimal():
            raise InvalidInputError("The number must be a integer number")

        decimal_number = int(decimal_number)
        base = int(base)

        if decimal_number == 0:
            return f"The number {decimal_number} in base {base} is {0}"
        else:
            result = ""
            auxiliar_number = abs(decimal_number) 
            while auxiliar_number > 0:
                res = auxiliar_number % base
                result = str(res) + result
                auxiliar_number = auxiliar_number // base
            if decimal_number < 0:
                result = "-" + result

        return f"The number {decimal_number} in base {base} is {result}"

# TODO: modify the __str__ method to get the point
class CartesianPoint:
    """ always get a tuple with str elements """
    def __init__(self, point):
        if len(point) > 2 or len(point) == 0:
            raise InvalidCartesianPoint("The point must have two coordinates")
   
        if point[0].isalpha() or point[1].isalpha():
            raise ValueError("The point must contain real numbers")

        self.point = (float(point[0]), float(point[1])) 
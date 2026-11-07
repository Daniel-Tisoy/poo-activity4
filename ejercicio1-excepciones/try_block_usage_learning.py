class ExceptionTest:
    def learning_exceptions(self):
        try:
            print("Into the first try block")
            result = 10000 / 0
            print("After the operation")
        except ZeroDivisionError as e:
            print("Error: ",e)
        finally:
            print("Into the finally block")

        try:
            print("Into the second try block")
            # all objects have str method available so 
            result_object = 13 + "a"
            print("Printing bad operation")
        except TypeError as e:
            print("An exception has been raised: ", e)
        finally:
            print("Into the second finally.")
    def out_limit_exception(self):
        try:
            text = "Programming"
            print("printing out of bounds: ")
            print(text[len(text)]) # creating the error
        except IndexError as e:
            print("Error raised: ", e)
    def number_format_excetion(self):
        try:
            number = int("programming") # generating the error
            print(number)
        except ValueError as e:
            print("Cannot parse a text to integer -", e)
        finally:
            print("Nothing happened :)")
class SalesPerson:

    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        self.age = 0

    def show_info(self):
        print(f"Seller name: {self.name}")
        print(f"Seller lastname: {self.lastname}")
        print(f"Seller age: {self.age}")

    def verify_age(self, age):
        if (age < 18):
            raise ValueError("The seller must be 18 or older")
        elif (age < 120):
            self.age = age
        else:
            raise ValueError("The age cannot be negative or more than 120")

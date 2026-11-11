from custom_exceptions import *

class CodingMarathonTeam():
    def __init__(self, team_name, college, programming_language):
        self.team_name = team_name
        self.college = college
        self.programming_language = programming_language
        self.programmers = []
        self.max_team_size = 3

    def is_full(self):
        return self.max_team_size == len(self.programmers)

    def join_programmer(self, name, lastname):
        if self.is_full():
            raise FullTeamError("The team is full, couldn't add the new programmer")
        coder = Programmer(name, lastname)
        self.programmers.append(coder)


class Programmer():

    def __init__(self, name, lastname): 
            Programmer.check_field(name, "name")
            Programmer.check_field(lastname, "lastname")
            self.name = name.capitalize()
            self.lastname = lastname.capitalize()

    @staticmethod
    def check_field(field, label):
        if len(field) == 0:
            raise InvalidInputError(f"The {label} must be larger than 1 character")

        if not field.isalpha():
            raise InvalidInputError(f"The {label} can't contain numbers or special characters")

        if len(field) > 20:
            raise TooLongStringError(f"The lenght of {label} can't be larger than 20 letters.")
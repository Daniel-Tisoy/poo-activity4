from custom_exceptions import *

class ASCIITable:
    def __init__(self):
        self.table = dict()

    def set(self, symbol):
        if symbol is None or symbol == "":
            raise NullValueError("The symbol cannot be null.")
        
        if len(symbol) > 1:
            raise TooManyArguments("The symbol must be a single letter.")
        
        if symbol in self.table:
            raise SymbolAlreadyExists("The symbol is already in the table")
        
        self.table[symbol] = ord(symbol)

    def get(self, symbol):
        if symbol is None or symbol == "":
            raise NullValueError("The symbol cannot be None.")
        
        if symbol not in self.table:
            raise SymbolNotFoundError(f"The symbol '{symbol}' doesn't exist in the table.")

        return self.table[symbol]
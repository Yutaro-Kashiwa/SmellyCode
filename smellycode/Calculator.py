import csv


class Calculator:
    def __init__(self):
        self.total = 0

    def return_invariant_value(self, a):  # NonCompliant
        b = 12
        if a == 1:
            return b
        return b

    look_up = False
    def look_up(self): # method name does not fit
        return self.look_up

    def one_variable_is_not_used(self, a1, a2, a3):
        return a1*a2

    def the_first_variable_should_be_self(yours):
        return None

    def not_implemented_method(self):
        pass


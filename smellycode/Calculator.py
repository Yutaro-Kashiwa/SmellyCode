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
    def lookup(self): # method name does not fit
        return self.look_up

    def one_(a1, a2, a3):
        return a1*a2
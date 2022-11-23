import csv


class SmellyClass:
    def __init__(self):
        self.total = 0

    def return_invariant_value(self, a):
        b = 12
        if a == 1:
            return b
        return b

    look_up = False

    def look_up(self):  # method name does not fit
        return self.look_up

    def one_variable_is_not_used(self, a1, a2, a3):
        return a1 * a2

    def the_first_variable_should_be_self(yours):
        return None

    def not_implemented_method(self):
        pass

    def raise_method(self):
        try:
            raise  # Noncompliant
        except ValueError as e:
            self.handle_error()
        except:
            raise
        self.same_handle_error()

    def handle_error(self):
        raise  # Noncompliant. This works but is hard to understand.

    def same_handle_error(self):
        raise  # Noncompliant. This works but is hard to understand.

    def check_my_none(self):
        my_none = None
        if my_none == None:
            pass
        if my_none is not None:
            pass
        if my_none == None:
            pass
        return my_none

    def add_value(self, a, b):
        if a == None:
            return None
        if b == None:
            return None
        return a + b

    def plus_value(self, a, b):
        if a == None:
            return None
        if b == None:
            return None
        return a + b

    def return_String_value(self, i):
        if (i==1):
            return "one"
        if (i==2):
            return "two"
        if (i==3):
            return "three"
        if (i==4):
            return "four"
        if (i==5):
            return "five"
        if (i==6):
            return "six"
        if (i==1):
            return "one"
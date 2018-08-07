
class Expression:
    def eval(self, env):
        raise NotImplementedError()        
    

class Atom(Expression):
    def __init__(self, val):
        self.val = val    

    def __str__(self):
        return "{}".format(self.val)

    def __repr__(self):
        cls_name = self.__class__.__name__
        return "{name}({val})".format(name=cls_name, val=self.val)

    def __eq__(self, other):
        return type(self) is type(other) and self.val == other.val


class Number(Atom):

    def eval(self, env):
        """Defined to return another Number instance, NOT a Python number type"""
        return self

    def __int__(self):
        """Conversion to Python int"""
        return int(self.val)

    def __float__(self):
        """Conversion to Python float"""
        return float(self.val)

    ### Operator Overloads ###

    def __add__(self, other):
        return Number(self.val + other.val)

    def __sub__(self, other):
        return Number(self.val - other.val)

    def __mul__(self, other):
        return Number(self.val * other.val)

    def __truediv__(self, other):
        return Number(self.val / other.val)

    def __mod__(self, other):
        return Number(self.val % other.val)

    def __pow__(self, other):
        return Number(self.val ** other.val)


class Symbol(Atom):
    def eval(self, env):
        return env[str(self)]

from proc import Proc

class List(Expression):
    def __init__(self, values):
        self.values = values

    def __str__(self):
        vals = " ".join(str(v) for v in self.values)
        return "({})".format(vals)

    def __repr__(self):
        vals = ", ".join(repr(v) for v in self.values)
        return "List({})".format(vals)

    def __eq__(self, other):
        return type(self) is type(other) and self.values == other.values

    def __iter__(self):
        """Allows a List to be iterated over directly"""
        return iter(self.values)

    def __getitem__(self, i):
        """Defines array subscript notation on List instances"""
        return self.values[i]

    def eval(self, env) -> Expression:
        first = self.values[0]
        rest = self.values[1:]
        if type(first) is Proc:
            proc = first
            args = rest
            # apply takes a list comprehension 
            # with every value in args evaluated.
            return proc.apply([a.eval(env) for a in args])
        elif type(first) is Symbol:
            if str(first) == "define":
                if type(rest[0]) is not Symbol:
                    raise Error("First arg to define must be a symbol!")
                if len(rest) != 2:
                    raise Error("Define requires exactly 2 arguments!")

                sym, value = rest       # Split rest into two parts
                env.declare(str(sym))   # Declare the symbol
                value = value.eval(env) # Evaluate the value-to-be-assigned
                env[str(sym)] = value   # Assign the value

            elif str(first) == "lambda":
                raise NotImplementedError("Define lambda!")
            else: # it must be a user-defined symbol
                proc = first.eval(env)
                
                if type(proc) is not Proc:
                    raise Error("Initial list element must be a Proc!")

                new_self = List([proc] + rest)
                return new_self.eval(env)

        return None
        

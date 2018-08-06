from proc import Proc

class Expression:
    def eval(self, env):
        
    

class Atom(Expression):
    def __init__(self, val):
        self.val = val    

    def __str__(self):
        return "{}".format(self.val)

    def __repr__(self):
        cls_name = self.__class__.__name__
        return "{name}({val})".format(name=cls_name, val=self.val)


class Number(Atom):
    def eval(self, env):
        return self


class Symbol(Atom):
    def eval(self, env):
        return env[self.val] # val is a str (the symbol's name).


class List(Expression):
    def __init__(self, values):
        self.values = values

    def __str__(self):
        vals = " ".join(str(v) for v in self.values)
        return "({})".format(vals)

    def __repr__(self):
        vals = ", ".join(repr(v) for v in self.values)
        return "List({})".format(vals)

    def eval(self, env) -> Expression:
        first_arg = self.values[0]
        rest_args = self.values[1:]
        if type(first_arg) is Proc:
            proc = first_arg
            args = rest_args
            # apply takes a list comprehension 
            # with every value in args evaluated.
            return proc.apply([a.eval(env) for a in args])
        elif type(first_arg) is Symbol:
            if first_arg.val == "define":
                if type(rest_args[0]) is Symbol:
                    env.declare(rest_args[0].val)
                    retVal = rest_args[1].eval(env) 
                    env[rest_args[0].val] = retVal
                else: raise Error("Define only accepts Symbol")
            elif first_arg.val == "lambda":
                raise NotImplementedError("Define lambda!")
            else: # it must be a user-defined symbol
                proc = first_arg.eval(env)
                
                if type(proc) is not Proc:
                    raise Error("Initial list element must be a Proc!")

                new_self = List([proc] + rest_args)
                return new_self.eval(env)

        return None
        

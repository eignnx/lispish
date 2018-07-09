class Atom:
    def __init__(self, val):
        self.val = val    

    def __str__(self):
        return "{}".format(self.val)

    def __repr__(self):
        cls_name = self.__class__.__name__
        return "{name}({val})".format(name=cls_name, val=self.val)

    def eval(self):
        raise NotImplementedError()
    

class Number(Atom):
    def eval(self):
        return self

class Symbol(Atom):
    pass

class List:
    def __init__(self, values):
        self.values = values

    def __str__(self):
        vals = " ".join(str(v) for v in self.values)
        return "({})".format(vals)

    def __repr__(self):
        vals = ", ".join(repr(v) for v in self.values)
        return "List({})".format(vals)
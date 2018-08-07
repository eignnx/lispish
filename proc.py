from env import Env
from typing import Collection

class Proc:
    def __init__(self, formals: Collection[str], body, creation_env: Env):
        self.formals = formals # The names of the formal parameters
        self.body = body # The body AST
        self.creation_env = creation_env # A ref to the env where the proc was defined

    def apply(self, args):
        if len(self.formals) != len(args):
            raise Exception("Wrong number of arguments!")
        local_bindings = dict(zip(self.formals, args))
        env = Env(local=local_bindings, parent=self.creation_env)
        return self.body.eval(env)

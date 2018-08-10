# Lispish
A Lisp clone written in Python.

## Dependencies
This project requires `sly` for Python 3. Install it like this:
```shell
pip3 install --user sly
```

## TODO
### Builtin Functions to Add

* `if`
* `let`
* `list`
    * Does not evaluate its arguments, returns an AST List
* `eval`
    * Accepts an AST, calls Python-level `eval` on it
* `=`/`eq?`
* `map`/`filter`
* `car`/`cdr`/`cons`
* `quote`/`'`

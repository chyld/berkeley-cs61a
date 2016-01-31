from functools import wraps

# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #
# FUNCTION DECORATOR

def debug(f):
    @wraps(f)
    def wrapped(*args, **kwargs): # tuple & dict
        print('***before***:', f.__name__)
        x = f(*args, **kwargs)
        print('---after---')
        return x
    return wrapped

@debug
def area(l, w):
    a = l * w
    return a

# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #
# CLASS DECORATOR

def debugmethods(cls):
    orig_attr = cls.__getattribute__
    def new_get_attr(self, name):
        print('Inside attribute!')
        return orig_attr(self, name)
    cls.__getattribute__ = new_get_attr

    for key, val in cls.__dict__.items():
        print('key:', key, 'val:', val)
        if callable(val):
            setattr(cls, key, debug(val))
    return cls

@debugmethods
class Example:
    pi = 3.14
    def a(self):
        pass
    def b(self):
        pass

# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #

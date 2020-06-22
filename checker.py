from flask import session
# import session
from functools import wraps
# import the wraps module from functools when creating your own decorators.
# wraps itself is a decorator.

# create our own decorator module in 3 steps

# 1) a decorator is just a good ole function.
def check_logged_in(func):
    @wraps(func)
    # 2.a) define a decorated function that accepts another function as...
    #      function object as the decorator's argument. note no "()" in func.
    # 2.b) decorate the wrapper function in wraps, passing in func as argument.
    def wrapper(*args, **kwargs): # going generic here...should be able to accept...
        # any number and any type of arguments, use " *args, **kwargs " to do this.
        # 3) the decorator returns a new function as its return value.
        if 'logged_in' in session: # check if logged_in key is in session dictionary.
            return func(*args, **kwargs)  # invoke the decorated func. The argument in check_logged_in func.
            # the decorated func should have the same...
            # any number and any type of arguments, use " *args, **kwargs " to do this.
        return 'You are NOT logged in'
    return wrapper # return the nested function as function object.

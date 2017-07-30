def something_dangerous():
    """Will cause TypeException"""
    1 + '42'


def something_else():
    """It also cause TypeException"""
    '42' + 1

try:
    something_dangerous()
# There may be a tuple of possible exceptions
except (ValueError, ArithmeticError):
    pass
except TypeError as e:
    pass


exception = None

try:
    something_dangerous()
except Exception as e:
    exception = e
    try:
        something_else()
    # you might place any expression that returns exception type into except statement
    except type(e):     # catch the same exception again
        pass

if exception:
    print('Exception occurred.')

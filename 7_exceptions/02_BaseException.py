print(BaseException.__subclasses__())

# Directly from BaseException inherits only system exceptions
# and exceptions which shutdown interpreter

# Any other built-in exceptions and user-defined exceptions
# must be inherited from the Exception class

# So, to handle any exception enough to type that:
try:
    something_dangerous()
except Exception:
    print('The exception has been handled.')

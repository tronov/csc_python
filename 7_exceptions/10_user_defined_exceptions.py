# The good practice is to declare your own base exception class
# which inherited from Exception class, e.g.:


class CSCException(Exception):
    pass


class TestFailure(CSCException):
    def __str__(self):
        return "lecture test failed"

# So, you will be able to catch all your exception
# separately from built-in exceptions

try:
    raise TestFailure()
except CSCException as e:
    if isinstance(e, TestFailure):
        print("test was failed")

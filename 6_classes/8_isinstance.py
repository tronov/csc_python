class A:
    pass


class B(A):
    pass


class C(B):
    pass


a = A()
b = B()
c = C()

# Never do so
print(type(b) == A)

# Is instance of the class B is an instance of the class A?
print(isinstance(b, A))

# Is instance of the class B is an instance of the class A or the class C?
print(isinstance(b, (A, C)))

class A:
    pass


class B(A):
    pass


class C(B):
    pass

a = A()
b = B()
c = C()


# Is B is subclass of the class A
print(issubclass(B, A))

# Is B is subclass of the class A or the class C
print(issubclass(B, (A, C)))

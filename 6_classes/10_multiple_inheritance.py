class A:
    def f(self):
        print("A.f")


class B:
    def f(self):
        print("B.f")


class C(A, B):
    pass


print(C().f())

# In case of a multiple inheritance python uses C3 linearisation algorithm
# To get a flat inheritance list use the mro() function

print(C.mro())      # print method resolution order

# Better if you avoid to use a multiple inheritance

class SomeClass:
    attribute = 42

    def do_something(self):
        print("Doing something with {}.".format(self.attribute))

print(SomeClass().do_something)     # bounded method (связанный метод)
SomeClass().do_something()

inst = SomeClass()
print(SomeClass.do_something)       # unbounded method = function (несвязанный метод)
SomeClass.do_something(inst)

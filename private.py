class MyClass:
    __privatevar = 27
    def __privatemeth(self):
        print("This is a private method.")
    def hello(self):
        print("Variable Value: ", MyClass.__privatemeth)

foo = MyClass()
foo.hello
foo.__privatemeth()
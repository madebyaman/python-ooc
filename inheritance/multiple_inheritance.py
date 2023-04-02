class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "A"


class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "b"


class C(A, B):
    def __init__(self):
        super().__init__()

    def showAttrs(self):
        print(self.foo)
        print(self.bar)
        # ? Method resolution order. A is inherited first so self.name = "A"
        print(self.name)


c = C()
c.showAttrs()

class A:
    def __init__(self):
        print("A is init")
    def feature1(self):
        print("feature 1-B")
    def feature2(self):
        print("feature2")


class B():
    def __init__(self):
        super().__init__()
        print("B is init")
    def feature1(self):
        print("feature 1-B")
    def feature4(self):
        print("feature4")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("C is init")

    def feat(self):
        super().feature2()


a2=C()
a2.feature1()
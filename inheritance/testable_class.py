class TestableClass(object):
    def method_one(self):
        print("TestableClass, Method One called")

class UsableClass(TestableClass):
    def method_one(self):
        print("UseableClass, Method One called")
        super().method_one()

class FourthClass(object):
    def method_two(self):
        print("Fourth Class")

class ThirdClass(FourthClass, UsableClass):
    def method_one(self):
        print("Third Class, method one")
        super().method_two()
        super().method_one()


# x = TestableClass()
# x.method_one()

# y = UsableClass()
# y.method_one()

z = ThirdClass()
z.method_one()
z.method_two()
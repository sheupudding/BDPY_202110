# ■ Object 屬性
class Course(object):
    pass


c1 = Course()
c2 = Course()
c3 = {}
# print(type(Course), type(c1))  # <class 'type'> <class '__main__.Course'>
# print(c1.__class__, c1.__class__)  # <class '__main__.Course'> <class '__main__.Course'>
# print(c1.__class__, c1.__class__.__bases__)  # <class '__main__.Course'> (<class 'object'>,)
# print(type(c1) == c1.__class__)  # True
# print(type(c1) == type(c2))  # True


# =============================================
# ■ Object 更動

class Car:
    vendor = "Lexus"
    valid = True


c1 = Car()
c2 = Car()
print(c1.vendor, c2.vendor, Car.vendor)  # Lexus Lexus Lexus
Car.valid = False  # 全物件更動
print(c1.valid, c2.valid, Car.valid)  # True True True
c1.valid = True  # 單一物件更動
print(c1.valid, c2.valid, Car.valid)  # True False False
c1.manager = "Richard"
print(c1.manager)
del c1.manager
# print(c1.manager, c1.name)  # AttributeError: 'Car' object has no attribute 'name'


# =============================================
# ■ Class 內部建置

# class Team:
#     member = 7
#
#     def __init__(self):
#         self.member = 8
#         self.day = 7
#
#     # Class method vs Not Class Method(需要先實例) in Python
#     # Class method vs Static method in Python
#     def working_hour(self):  # 需要先實例才可以用
#         return self.day
#
#     def all_working_hour(self):  # 需要先實例才可以用
#         return self.day * self.member
#
#     @classmethod  # 無需實例，可以存取到class內的東西
#     def get_member(cls):
#         return cls.member
#
#     @staticmethod  # 無法存取到class內的東西，放置class相關method以管理使用
#     def calculate(x, y):
#         return 2 * x ** y
#
#
# t1 = Team()
# print(t1.member)
# print(Team.all_working_hour())  # 未實例：all_working_hour() missing 1 required positional argument: 'self'
# print(t1.working_hour())
# print(t1.day)
# print(t1.member, Team.member)
# print("get_member", Team.get_member(), t1.get_member())
# print(t1.calculate(2, 3), Team.calculate(3, 2))

# =============================================
# ■ Class 建置練習

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.counter = 0

    def calculateArea(self):
        return self.width * self.height

    def __iter__(self):  # 對 obj loop 時，會先call iter
        print("called iterator")
        return self

    def __next__(self):  # next(obj)會呼叫，for obj_each in obj 時也是用next
        print("iterate to next")
        while self.counter < 10:  # 設定只能 next 10次
            self.counter += 1
            return 888
        raise StopIteration()  # end iter


r1 = Rectangle(3, 5)
print(r1.width, r1.height, r1.calculateArea())
print([r for r in r1])

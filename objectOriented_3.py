# ■ 父子類別繼承
class Emp:
    pass


class Engineer(Emp):
    pass


class PM(Emp):
    pass


class HR(Emp):
    pass


e1 = Emp()
e2 = Engineer()
e3 = PM()
e4 = HR()
staffs = [(e1, "Employee1"), (e2, "Engineer1"), (e3, "PM1"), (e4, "HR1")]
classes = [Emp, Engineer, PM, HR]

print('★ IsInstance ★')
for staff, name in staffs:
    print('==============================')
    for emp_class in classes:
        isA = isinstance(staff, emp_class)
        message1 = 'is a' if isA else 'is not a'
        print(f"{name} {message1} {emp_class.__name__}")
    print('==============================')

print('★ isSubclass ★')
for c1 in classes:
    print('==============================')
    for c2 in classes:
        isSUBClass = issubclass(c1, c2)
        message = '{0} a subclass of'.format('is' if isSUBClass else 'is not')
        print(f"{c1.__name__} {message} {c2.__name__}")
    print('==============================')
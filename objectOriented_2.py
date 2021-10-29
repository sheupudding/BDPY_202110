# ■ 父子類別繼承實作
class Employee:
    gradeLevel = 6

    def __init__(self):
        self.gradeLevel = 8  # 子類別實例時+無覆蓋，才吃得到

    def startWork(self):
        print('父類別')

    def endWork(self):
        pass


class RD(Employee):

    def __init__(self):
        self.currentGrade = self.gradeLevel  # 子類別實例覆蓋掉父類別=>gradeLevel = 6

    def startWork(self):
        print('rd work with grade', self.currentGrade)

    def endWork(self):
        print("rd ", self.currentGrade, " finish work")


class PM(Employee):

    def startWork(self):
        print('rd work with grade', self.currentGrade)

    def endWork(self):
        print("rd ", self.currentGrade, " finish work")


# print(Employee.gradeLevel, RD.gradeLevel, PM.gradeLevel)  # 6 6 6
# RD.gradeLevel = 7
# print(Employee.gradeLevel, RD.gradeLevel, PM.gradeLevel)  # 6 7 6
# Employee.gradeLevel = 5  # RD已對class的gradeLevel設置7，故父類別Employee的更動不會覆蓋
# print(Employee.gradeLevel, RD.gradeLevel, PM.gradeLevel)  # 5 7 5
rd1 = RD()
# pm1 = PM()
# print(rd1.gradeLevel, pm1.gradeLevel)  # 7 5
rd1.startWork()

import json
from fractions import Fraction
from decimal import Decimal
import collections
from pprint import pprint
from functools import reduce
import itertools

# ■ 　demo1 Obj construct
demoObj = [{'date': "2021-10-25", 'weather': "cloudy", 'mood': "nervous"}, {'date': "2021-10-26", 'weather': "cloudy", 'mood': "tired"}]
# print(json.dumps(demoObj))
# print([obj for obj in demoObj])
# print([obj['date'] for obj in demoObj])

str1 = '123456789'
# subscript 語法 list[n] 0<=ele<n
# print(str1[:5])  # 取得前5字元 12345
# print(str1[:])  # from begin to end
# print(str1[:10])  # from begin to 9 (exclude)
# print(str1[2:6])  # from 2 to 5
# print(str1[20:])  # from 20 to end
# print(str1[-5:])  # last 5 elements

l1 = list('abcde')  # => [a, b ,c ,d, e]
edges = tuple(e for e in l1)

# 確認格式
# 1.if isinstance(obj, tuple):
# 2.type(obj) => <map object at 0x000001E9AAAD0CC8>
# ====================================================================

# ■　demo2 calculate
f2 = Fraction(5, 2)  # 5/2
f3 = Fraction(7, 3)  # 7/3
# print(f2 + f3, f2 - f3)  # 通分 9/6 1/6
f4 = Fraction(250, 70)
# print(f4.denominator)  # 7
# print(f4.numerator)  # 25
# ====================================================================

# ■　demo3 Decimal
x1 = Decimal(123.45)  # 2進位導致誤差 123.4500000000000028421709430404007434844970703125
x2 = Decimal(0.5)  # 2進位值無誤差 0.5
x3 = Decimal('123.45')  # 消除誤差：字串傳入
# ====================================================================

# ■　demo4 add params to string
radius = 2.0
area = radius * radius * 3.14


# print("radius=", radius, "area=", area)
# print("radius=%f, area=%f" % (radius, area))
# print("radius=%.2f, area=%.6f" % (radius, area))
# print("radius=%(r).2f, area=%(a).6f" % {'a': area, 'r': radius})
# print("radius={}, area={}".format(radius, area))
# print("radius={:f}, area={:f}".format(radius, area))
# print("radius={:.2f}, area={:.6f}".format(radius, area))
# print("radius={1:.2f}, area={0:.6f}".format(area, radius))
# print("radius={r:f}, area={a:f}".format(a=area, r=radius))
# print(f"radius={radius:.2f}, area={area:.6f}")
# ====================================================================


# ■　demo4-2 add params to string: setting Course class str, repr
class Course():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"[{self.name}]"

    def __repr__(self):
        return f"課程名稱=%s" % self.name


c1 = Course("BDPY")  # __init__(self, name) =>name參數
# print(c1)  # __str__ >>[BDPY]
# print([c1])  # __repr__ >>[課程名稱=BDPY]
# print("str format :%s, repr format: %r" % (c1, c1))  # str format :[BDPY], repr format: 課程名稱=BDPY
# print("str format :{0!s}, repr format: {0!r}, repr in ascii: {0!a}".format(c1))  # str format :[BDPY], repr format: 課程名稱=BDPY, repr in ascii: \u8ab2\u7a0b\u540d\u7a31=BDPY
# ====================================================================

# ■　demo5 filling string to size 10
str1 = '1234567890apple'
# print("%10sDONE" % str1)  # abcdefg1234567DONE
# print("%10s" % (str1[:5]))  # 12345 +　[5空白]
# print("{:10s}DONE".format(str1[:5]))  # 12345     DONE
# print("{:>10s}DONE".format(str1[:5]))  # [5空白] + 12345DONE
# print("{:^10s}".format(str1[:5]))  # [2空白] + 12345   DONE
# print("{:*^10s}DONE".format(str1[:5]))  # **12345***DONE
# ====================================================================

# ■　demo6 setting object
courses = [{'name': 'poop', 'field': 'python', 'attend': 10, 'remote': False},
           {'name': 'bdpy', 'field': 'python', 'attend': 15, 'remote': True},
           {'name': 'andbiz', 'field': 'android', 'attend': 5, 'remote': False}]  # bad constructing

# better constructing: build a course constructor
course = collections.namedtuple('course', ['name', 'field', 'attendee', 'remote'])  # class
poop = course(name='poop', field="python", attendee=10, remote=False)  # tuple => immutable(can't edit)


# print(poop['name'], poop.attendee, poop.remote, poop.field)


# ====================================================================

# ■　demo7 build function
def willOpen(x):
    return x.attendee >= 10


# ====================================================================

# ■　demo8 convert list to string
listStr = ''.join([str(value) for value in courses])
# ====================================================================

# ■　demo9 convert map to list/tuple
course = collections.namedtuple('course', ['name', 'field', 'attendee', 'remote'])
# all courses
poop = course(name='poop', field="python", attendee=10, remote=False)
bdpy = course(name='bdpy', field="python", attendee=15, remote=True)
andbiz3 = course(name='andbiz', field='android', attendee=18, remote=True)
pykt = course(name='pykt', field="python", attendee=9, remote=True)
aiocv = course(name='aiocv', field="python", attendee=20, remote=False)
courses = (poop, bdpy, andbiz3, pykt, aiocv)

name_and_field = map(lambda x: {'name': x.name, 'field': x.field}, courses)
# pprint(name_and_field)  # <map object at 0x000001E9AAAD0CC8>
# pprint([c for c in name_and_field])
# map 迴圈結束後即會就會被清空 (iterator 指向特性)
# 轉為tuple 才能重複存取
name_and_field = tuple(map(lambda x: {'name': x.name, 'field': x.field}, courses))
# pprint(tuple([c for c in name_and_field]))
# pprint(tuple(name_and_field))  # 效果同上
# ====================================================================

# ■　demo10 calculate data list with reduce
totalIncome = tuple({'name': c.name, 'income': c.attendee * 8000} for c in courses)
# reduce(function, iterable[, initializer], ?default值)
# acc累積值, val現在值
totalAmount = reduce(lambda acc, val: acc + val['income'], totalIncome, 0)
# print(totalAmount)
# print(sum(x['income'] for x in totalIncome))
# ====================================================================

# ★★　demo11 data process with reduce: 歸納資料  ★★
# pickup field
course = collections.namedtuple('course', ['name', 'field', 'attendee', 'remote'])
poop = course(name='poop', field="python", attendee=10, remote=False)
bdpy = course(name='bdpy', field="python", attendee=15, remote=True)
andbiz3 = course(name='andbiz', field='android', attendee=18, remote=True)
pykt = course(name='pykt', field="python", attendee=9, remote=True)
aiocv = course(name='aiocv', field="python", attendee=20, remote=False)
cplus = course(name='cplus', field="c++", attendee=30, remote=True)
courses = (poop, bdpy, andbiz3, pykt, aiocv, cplus)


def reducer1(acc, val):
    acc[val.field].append(val.name)
    return acc


courses_by_category = reduce(reducer1, courses, {'python': [], 'android': [], 'c++': []})  # 寫死的歸納
# pprint(courses_by_category)


def reducer2(acc, val):
    acc.setdefault(val.field, [])  # 先塞入key值，val設為[] list
    acc[val.field].append(val.name)  # add val to list 進key值
    return acc


course_by_category2 = reduce(reducer2, courses, {})  # 動態歸納
# pprint(course_by_category2)

course_by_category3 = reduce(reducer1, courses, collections.defaultdict(list))
# pprint(dict(course_by_category3))

# itertools.groupby為one pass，非連續key值後者會蓋掉前者，故須先sort
courses = sorted(courses, key=lambda x: x.field)
# [c for c in itertools.groupby(courses, lambda x: x.field)] => c = [{field}, {object}]
x1 = {c[0]: list(c[1]) for c in itertools.groupby(courses, lambda x: x.field)}  # 動態歸納
# pprint(x1)
# ====================================================================


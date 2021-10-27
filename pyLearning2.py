import collections
from pprint import pprint
from functools import reduce
from time import sleep, time
import multiprocessing
import os
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor

# 參數設定(承pyLearning demo11)
course = collections.namedtuple('course', ['name', 'field', 'attendee', 'remote'])
poop = course(name='poop', field="python", attendee=10, remote=False)
bdpy = course(name='bdpy', field="python", attendee=15, remote=True)
andbiz3 = course(name='andbiz', field='android', attendee=18, remote=True)
pykt = course(name='pykt', field="python", attendee=9, remote=True)
aiocv = course(name='aiocv', field="python", attendee=20, remote=False)
courses = (poop, bdpy, andbiz3, pykt, aiocv)
# ====================================================================

# ■ demo1 reduce(data loop處理(acc總值, val現值), data, 初始值設定)
# dictionary 組合方式：{**dic1, **dic2} => {dic1 + dic2}
# 初始值若未設定key值(python, android)，data loop處理時遇到acc[val.field]就會噴無此key值
courseByCategory = reduce(lambda acc, val: {**acc, **{val.field: acc[val.field] + [val.name]}},
                          courses,
                          {'python': [], 'android': []})
# print(courseByCategory)


# ====================================================================

# ■ demo2 map(data loop處理, data)
# 字串開始前的引號或連續三個引號前加上 f 或 F，你可以在這個字串中使用 { var } 包夾 Python 的運算式，引用變數或其他字面值 (literal values)

def transform(x):
    print(f"process record:{x.name} using process id:{os.getpid()}")
    sleep(3)  # 睡1秒
    rtnDic = {'name': x.name, 'revenue': x.attendee * 5000}
    print(f"process record:{x.name} done")
    return rtnDic


# 計時處理
# start = time()
# result = tuple(map(transform, courses))
# end = time()
# print(f"total time:{end - start:.2f} seconds")
# pprint(result)
# ====================================================================

# ■ demo3 多執行緒 process
# if __name__ == '__main__':
    # start = time()
    # pool = multiprocessing.Pool()
    # # pool = multiprocessing.Pool(processes=2, maxtasksperchild=1)
    # print(f"now we run with process:{pool._processes}")
    # result = tuple(map(transform, courses))
    # end = time()
    # print(f"total time:{end - start:.2f} seconds")
    # pprint(result)
# ====================================================================

# ■ demo4 多執行緒 process pool
# if __name__ == '__main__':
#     start = time()
#     with ProcessPoolExecutor() as executor:
#         result = tuple(executor.map(transform, courses))E
#         end = time()
#         print(f"total time:{end - start:.2f} seconds")
#         pprint(result)
# ====================================================================

# ■ demo5 多執行緒 thread
if __name__ == '__main__':
    start = time()
    with ThreadPoolExecutor() as executor:
        result = tuple(executor.map(transform, courses))
        end = time()
        print(f"total time:{end - start:.2f} seconds")
        pprint(result)
# ====================================================================

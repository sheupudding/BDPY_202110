import module.common as co
import time
from datetime import datetime
import math
import random

if __name__ == '__main__':
    # print("foo:", co.foo(1, 2))
    # print("bar:", co.bar(3, 4))
    # print("bar_muti:", co.bar_muti(3, 4))
    # print("bar_muti:", co.bar_muti(3, 4, 5))
    # print("bar_muti:", co.bar_muti(3, 4, *[5, 6, 7]))  # *可以拆解collection為多個參數

    # co.print_muti('Will U marry me?', 'YES', 'NO', name='Cindy', sex='female')
    # co.print_muti(fix3='NO', fix1='Will U marry me?', name='Cindy', sex='female', fix2='YES')  # 可以指定參數順序

    # profile = {'name': 'Cindy', 'sex': "female", 'age': 20, 'hobby': "reading"}
    # co.print_muti('Will U marry me?', 'YES', 'NO', **profile)  # **可以拆解collection為key=val之型態

    # =============================================

    now = datetime.now()
    print(now)
    print(repr(now))
    print([now])
    print([str(now)])

    # =============================================

    print(math.pi, math.e, math.sqrt(5))
    # print(math.sqrt(-1))
    print((-1) ** 0.5)
    for _ in range(5):
        print(random.randint(0, 5))

    stores = ['7-11', 'fami', 'ok', 'hi-life']
    for _ in range(5):
        print(random.choice(stores))
    cards = ['A', 'K', 'Q', 'J', '10']
    for _ in range(10):
        print(cards)
        random.shuffle(cards)


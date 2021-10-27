def foo(a, b):
    return f"{a}+{b}={a + b}"


def bar(a, b):
    return f"{a}*{b}={a * b}"


# *視為參數為多個，不限傳入數量
def bar_muti(a, b, *args):
    calStr = ''
    calVal = a*b
    for arg in args:
        calStr = calStr + '*' + str(arg)
        calVal = calVal * arg
    return f"{a}*{b}{calStr}={calVal}"


# **視為參數為多個，不限傳入數量，並且讀為key=val之型態
def print_muti(fix1, fix2, fix3,  **kwargs):
    print(f"{fix1} ANS:{fix2}/{fix3}")
    print("profiles:")
    for k, v in kwargs.items():
        print(f"type={k}, value={v}")


def callback1():
    print("callback1!")


def callback2():
    print("call2 fire!")
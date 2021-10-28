import graphviz as gv
from itertools import combinations, permutations
import functools
import itertools
import pandas as pd
import numpy

# ■ graph: 建立節點node，設置node之間連線edge
# cmd: dot -v 查看支援的檔案類型，ex.pdf, svg, png
# g1 = gv.Graph(format='png')
# ag1 = gv.Digraph(format='png')  # => 連線變箭頭
# l1 = list('orange')
# edges = tuple(e for e in combinations(l1, 2))  # 兩個物件間只有一條連線
# print(edges)
# for n1, n2 in edges:
#     ag1.edge(n1, n2)
# ag1.render('graph/testDigraph')
# ====================================================================

# ■ graph x function editing
# 中文會需要設置中文ttc字型檔，svg向量檔會抓系統字型
graph1 = functools.partial(gv.Graph, format='png', encoding='UTF-8')
digraph1 = functools.partial(gv.Digraph, format='png', encoding='UTF-8')
g1 = graph1()
ag1 = digraph1()


def add_nodes(graph, nodes):
    for n in nodes:
        if isinstance(n, tuple):
            graph.node(n[0], **n[1])
        else:
            graph.node(n)
    return graph


def add_edges(graph, edges):
    for e in edges:
        if isinstance(e[0], tuple):
            graph.edge(*e[0], **e[1])
        else:
            graph.edge(*e)
    return graph


def apply_styles(graph, styles):
    graph.graph_attr.update(('graph' in styles and styles['graph']) or {})  # if else 寫法=> if(styles[graph]
    graph.edge_attr.update(('edges' in styles and styles['edges']) or {})
    graph.node_attr.update(('nodes' in styles and styles['nodes']) or {})
    return graph


node1 = ('A', {'label': "NodeA"})
node2 = ('B', {'label': "NodeB"})
node3 = ('C', {'label': "中文的節點"})
node4 = ('D', {})

e1 = (('A', 'B'), {'label': 'taipei dorm'})
e2 = (('A', 'C'), {'label': 'tokyo'})
e3 = (('B', 'C'), {'label': '北京'})
e4 = (('B', 'D'), {})

styles = {'graph': {'label': '超級範例',
                    'fontsize': '24',
                    'fontcolor': '#C0FFEE',
                    'fontname': 'MSJH',  # 設置中文字體才有中文
                    'bgcolor': '#FF0066',
                    'rankdir': 'RL',
                    },
          'edges': {'color': '#002288',
                    'arrowhead': 'open',
                    'fontname': 'MSJH',  # 設置中文字體才有中文
                    'fontsize': '24',
                    'fontcolor': '#C0FFEE'},
          'nodes': {'shape': 'box',
                    'fontcolor': 'green',
                    'fontname': 'MSJH',  # 設置中文字體才有中文
                    'color': 'blue',
                    'style': 'filled',
                    'fillcolor': '#FFC0EE'}}

g1_nodes = [node1, node2, node3, node4]
g1_edges = [e1, e2, e3, e4]
add_nodes(ag1, g1_nodes)
add_edges(ag1, g1_edges)
# ag1.render('graph/testFuncDigraph')

apply_styles(ag1, styles)


# ag1.render('graph/testStyleDigraph')

# ====================================================================

# ■ yield: 對function 做 next 會依yield 值回覆
# 有點像會有多個return一個一個丟東西出來，可以直接把func67當list使用

def func67():
    a = 1
    b = 2
    yield 'rtn1', a
    a += b
    receiveYield = yield a

    receiveYield2 = yield a + b
    yield 'rtn2', receiveYield
    yield 'rtn3', receiveYield2


# print(func67(), type(func67()))  # <generator object func67 at 0x0000016F2C77AD48> <class 'generator'>
x1 = func67()


# print(next(x1))
# x1.send(500)  # send 會吃掉一個yield，將值傳入
# x1.send(220)  # send 會吃掉一個yield
# print(next(x1))
# print(next(x1))
# print(next(x1))


# y1 = func67()
# for y in y1:
#     print("y=", y)

# z1 = func67()
# print([z for z in z1])

# ====================================================================

# ■ 實作費式數列

def fib(maxCnt):
    prev, current = 0, 1
    count = 0
    while count < maxCnt:
        count += 1
        yield current
        prev, current = current, prev + current


# print([t for t in fib(30)])

# ====================================================================

# ■ panda 會有index: value，預設index=0,1,2...

# s1 = pd.Series([3, 1, 4, 5, 9, -2, 8])
# print(type(s1))  # <class 'pandas.core.series.Series'>
# print(s1)
# print(s1.values)
# print(s1.index)
# s2 = pd.Series([4, 7, -5, 3], index=['nangang', 'taipei', 'banqiao', 'taoyuan'])
# print(type(s2))
# print(s2.values)
# print(s2.index)
# print(s1[2])
# print(s1[[2, 3, 4, 6]])
# print(s1[[2, 3, 6, 4]])
# print(s2['nangang'])
# print(s2[['taipei', 'banqiao', 'nangang']])
# print(s2[s2>0])
# print(s1**2)

# ▼ 缺值 Nan/ 空值 None => 判斷式 (obj.isna()/obj.isnull()) 或 (panda.isna(obj)/panda.isnull(obj))
d1 = {'poop': 35, 'bdpy': 35, 'pykt': 35, 'aiocv': 35, 'linebot': 14, 'testit': 14}
s1 = pd.Series(d1)  # 直接以dictionary建置 index:val
# print('poop' in s1, 'andbiz' in s1)  # True False
l1 = ['testit', 'andbiz', 'linebot', 'aiocv']
s2 = pd.Series(d1, index=l1)  # 以dictionary設置 index:val 對照表，再建置index
# print(s2.isna())  # 以下結果
# testit     False
# andbiz      True
# linebot    False
# aiocv      False
# dtype: bool

d2 = {'poop': 'Mark', 'bdpy': None, 'andbiz': None, 'testit': "Frank"}
s3 = pd.Series(d2, index=l1)
# dtype: bool
# print(s3)  # 以下結果
# testit     Frank
# andbiz      None
# linebot      NaN
# aiocv        NaN
# dtype: object
# print(pd.isna(s3))  # 以下結果
# testit     False
# andbiz      True
# linebot     True
# aiocv       True


# ▼ 資料相加
c1_1 = pd.Series([1000, 800, 500, 300], index=['nangang', 'taipei', 'banqiao', 'taoyuan'])
c1_2 = pd.Series([3200, 1800, 5200, 2300], index=['nangang', 'taipei', 'banqiao', 'taoyuan'])
c2_1 = pd.Series([500, 300, 400], index=['hsinchu', 'taichung', 'chaiyi'])
c2_2 = pd.Series([1500, 3100, 2400], index=['hsinchu', 'taichung', 'chaiyi'])

# print(c1_1 + c1_2)  # 相加需index相同，否則噴錯，會依照val加
# nangang    4200
# taipei     2600
# banqiao    5700
# taoyuan    2600
# dtype: int64

c5 = c1_1.append(c2_1)  # 直接串接，不會合併相同index的值，會導致重複index
# print(c5)
# print("*" * 80)
c5.name = 'sold'
c5.index.name = 'station'
c5.index = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7']
# print(c5)
# ====================================================================

# ■ panda dataFrame
data = {'course': ['poop', 'bdpy', 'pykt', 'aiocv'],
        'year': [2018, 2017, 2019, 2020],
        'slide': [200, 250, 230, 300]}
d1 = pd.DataFrame(data)
# print(d1)
# print(d1.head(n=2))  # 取兩筆

# 以data設置 index:val 對照表，再建置column
# d2 = pd.DataFrame(data, columns=['course', 'slide', 'year', 'instructor'])
# print(d2)
# d3 = pd.DataFrame(data, index=['p1', 'p2', 'p3', 'p4'], columns=['course', 'slide', 'year', 'instructor'])
# print(d3)
# print(type(d3['course']))

# 取得資料
# print(d3['course'])  # 取得欄
# print(d3[['course', 'slide']])  # 取得多欄
# print(d3.loc['p1'])  # 取得資料列
# print(d3.loc[['p1', 'p4']])  # 取得多筆資料列

# 設置欄位，並給予預設值
# d3['year'] = 2022
# print(d3)
# d3['year'] = [2020, 2022, 2020, 2022]  # 設置欄位，並給予個別值，若少給會噴錯
# print(d3)

# 刪除欄
# del df1['slide']
# print(df1)

# ====================================================================
# ■ panda dataFrame 資料處理
df1 = d1

# 設置location欄位
# s1 = pd.Series(['taipei', 'hsinchu', 'taichung', 'kaohsiung'],
#                index=[0, 1, 2, 3])
# df1['location'] = s1
# print(df1)

# 設置method欄位
# df1['method'] = pd.Series(['remote', 'local'], index=[0, 3])
# print(df1)

# 以運算設置heavy欄位
# df1['heavy'] = df1['slide'] >= 250
# print(df1)

# ====================================================================
# ■ panda dataFrame 轉置矩陣，調換來欄/列
df2 = df1.T
# print(df2)

# 取得資料: 二微陣列
# print(df2.values)
# print(df2.values[0, 0])
# df2.values[0, 0] = 'poops'
# print(df2.values[0, 0])

# ====================================================================
# ■ reindex 重新排序資料，沒value會補上NaN
s1 = pd.Series([20, 15, 18, 37, 25], index=['mar', 'jan', 'feb', 'may', 'apr'])
s2 = s1.reindex(['jan', 'feb', 'mar', 'apr', 'may', 'jun'])  # 重新排序資料
# print(s2)
s3 = pd.Series(['L', 'M', 'S'], index=[0, 5, 10])
# print(s3)
# ffill(full fill)向後填滿
# print(s3.reindex(range(15), method='ffill'))

# numpy.arange(16).reshape(4, 4) => 建立0-15的資料，4列4行排序
d1 = pd.DataFrame(numpy.arange(16).reshape(4, 4), index=[1, 2, 3, 4], columns=['Kotlin', 'Swift', 'C++', 'Java'])
# print(d1)
d2 = d1.reindex(columns=['objC', 'Kotlin', 'Swift', 'Java', 'C++', 'Scala'])
# print(d2)


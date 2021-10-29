import pandas as pd
import numpy as np
import pandas_datareader.wb as wb
import matplotlib.pyplot as plt
from matplotlib import animation
from scipy.stats import norm

dict1 = {'station': ['Nangang', 'Taipei', 'Banqiao', 'Taoyuan', 'Hsinchu'],
         'order': [1, 2, 3, 4, 5],
         'backOrder': [5, 4, 3, 2, 1]}

# ====================================================================
# ■ drop 去除資料(非實際刪除)
# 要實際刪除：加入inplace=True
pd1 = pd.DataFrame(dict1)
# print(pd1)
# print(pd1.drop(2))  # 去除index=2
# print(pd1.drop([1, 3]))  # 去除index=1,3
# print(pd1.drop('order', axis=1))
# print(pd1.drop('order', axis='columns'))
# print(pd1.drop(['order', 'backOrder'], axis=1))
# pd1.drop([1, 4], inplace=True)
# print(pd1)

# ▼ iloc 切割資料，依照資料順序
# 橫切
# print(pd1[:3])  # 1到3筆資料
# 縱切：iloc[橫切, 縱切]
# print(pd1.iloc[3:4, :2])

# ▼ loc 切割資料，依照index name (包含)
pd2 = pd.DataFrame(dict1, ['A', 'B', 'C', 'D', 'E'])
# print(pd2.loc[:'C'])

# ====================================================================
# ■ 運算資料產出
# 設置亂數2維資料：np.random.randn(6, 7)：隨機高斯數 /randint(2, size=10)：隨機整數
df1 = pd.DataFrame(np.random.randint(50, size=(6, 7)),
                   index=list(range(0, 12, 2)),
                   columns=list(range(0, 7, 1)))

# print(df1)
func1 = lambda x: x.max() - x.min()
# print(df1.apply(func1))
# print(df1.apply(func1, axis=1))
func2 = lambda x: pd.Series([x.min(), x.max()], index=['min', 'max'])
# print(df1.apply(func2))
# print(df1.apply(func2, axis=1))

# ▼ 設置到column/row 的 name ，再以sort_index重新排序
# df1.index = df1.iloc[:, 1]
# print(df1)
# print(df1.sort_index())

# df1.columns = df1.iloc[2, :]
# print(df1)
# print(df1.sort_index(axis=1))

# ▼ 設置到column/row 的 name ，再以sort_index重新排序
# print(df1.sort_values(by=2))  # 依欄位2值去排序資料
# print(df1.sort_values(by=6))

s1 = pd.Series([4, -15, 7, 7, 2, 2, 0, 0, 4])
# print(s1.rank())  # 自動給予分數
# print(s1.rank(method='first'))  # 給予1分開始的分數，同分會依照讀取順序給排序
# print(s1.rank(method='min'))  # 給予1分開始的分數，同分會同序
# print(s1.rank(method='max'))

# ▼ 設置NaN值，運算會忽略
df1.iloc[2, 3] = np.NaN
# print(df1)
# print(df1.sum())
# print(df1.sum(axis='columns'))  #　對欄位值(縱向)

# 加入 skipna 取消忽略NaN
# print(df1.sum(skipna=False))
# print(df1.sum(axis='columns', skipna=False))  #　對欄位值(縱向)

# ▼ idxmax, idxmin 回傳極值
# print(df1.idxmax())  # 取得最大之欄位
# print(df1.idxmin())  # 取得最小之欄位
# print(df1.idxmax(axis=1))  # 對每筆資料(同上)，取得最大之欄位
# print(df1.idxmin(axis="columns"))  # 對欄位值(縱向)，取得最小之欄位

# ▼ cumsum, cumprod, cummax, cummin 累積運算
# print(df1.cumsum())  # 累加
# print(df1.cumprod())  # 累乘(不確定)
# print(df1.cummax())  # 覆蓋目前最大值
# print(df1.cummin())
# print(df1.describe())

# ====================================================================
# ■ 向wb: data.worldbank.org (world bank 開放資料)取得資料
# data = wb.search(string='SE.PRM.TENR', field='id')
data = wb.download(indicator='SE.PRM.TENR',
                   country=['all'],
                   start=2002,
                   end=2016)
# print(data)
# for i in range(4):
#     print(data.iloc[i, 1])
# print(data.shape)  # (3990, 1) ：表示[3990 rows x 1 columns] 是被包裝起來的
data2 = data.reset_index()  # 把column index解開 => [3990 rows x 3 columns]

# print(data2.head())  # head() 取出頭幾筆
# print(data2.country.unique())  # 取出country & group by county
# print(data2[data2.country == 'New Zealand'])

# ▼ 取出每個國家最高上網%數的年份資料
temp1 = data2.groupby(['country'])['SE.PRM.TENR'].transform(max)  # 以country group取出SE.PRM.TENR，覆蓋至目前最大值
# print(temp1.head(40))
maxIndex = temp1 == data2['SE.PRM.TENR']  # loop每筆，讓maxIndex = 最大值 => 去對data2取出每個國家最大值資料
data3 = data2[maxIndex]
# print(data3.head(40))  # 完成

# ▼ pct_change() 計算出資料變化幅度(%)
france1 = data2[data2.country == 'France']
germany1 = data2[data2.country == 'Germany']
france1.index = france1['year']
germany1.index = germany1['year']
# print(france1)
# print(france1['SE.PRM.TENR'].pct_change())
# print(germany1)

# ▼ corr() 交叉比較資料變化幅度(%)
df1 = pd.DataFrame({'fr': france1['SE.PRM.TENR'], 'de': germany1['SE.PRM.TENR']})
# print(df1)
# print(df1['fr'].corr(df1['de']))
# print(df1['fr'].cov(df1['de']))
# print(df1.corr())
# print(data2.country.value_counts())  # 沒聽到
# print(pd.value_counts(data2.country))

# ▼ value_counts() 交叉比較資料變化幅度(%)
mask1 = data2.country.isin(['France', 'Germany'])  # isin 取出包含值資料
# print(data2[mask1])
unique_country = data2.country.unique()
result = pd.Index(unique_country).get_indexer(data2.country)
print(result)

# ▼ value_counts() 交叉比較資料變化幅度(%)
data3 = pd.DataFrame({'FR': [1, 3, 4, 1, 4], 'DE': [2, 3, 1, 1, 4], 'JP': [3, 1, 2, 3, 4]})
# print(data3)
# result = data3.apply(pd.value_counts)
# print(result)
# result2 = data3.apply(pd.value_counts).fillna(0)  # NaN轉為0，若有NaN轉換等會將資料轉換為浮點數
# print(result2)

# ====================================================================
# ■ matplotlib 繪製視覺圖
x = range(10)
# '.', '^', '*','o','o-','o--', 'r+', 'b-' (-實線、--虛線、r紅色、b藍色)
# plt.plot(x, 'o--')
# plt.show()
ax = np.array(x)
ay = ax ** 2
# plt.plot(ax, ay, 'r*')
# plt.axis([-10, 10, 0, 100])  # 設置圖的x, y座標極值
# plt.show()

t = np.arange(0, 2, 0.1)
# plt.plot(t, t, 'r+', t, t ** 2, 'g-', t, t ** 3, 'b*')
# plt.show()

# ▼ 結合運算並繪製視覺圖
# sequence1 = pd.DataFrame(np.random.normal(1.0, 0.08, (100, 8)))
# print(sequence1.head())
# accumulate = sequence1.cumprod()
# plt.plot(accumulate)
# plt.show()

# ▼ 動態圖
# fig, ax = plt.subplots()
# x = np.arange(0, 2 * np.pi, 0.01)
# line, = ax.plot(x, np.sin(x))
#
#
# def animate(i):
#     line.set_ydata(np.sin(x + i / 5.0))
#     return line,
#
#
# def init():
#     line.set_ydata(np.ma.array(x, mask=True))
#     return line,
#
#
# ani = animation.FuncAnimation(fig, animate, np.arange(1, 400, 0.1),
#                               init_func=init, interval=5, blit=True)
# plt.show()

# ▼ 高斯分布 + pdf機率計算
mu = 80
sigma = 8
x = mu + sigma * np.random.randn(1000)  # 少量資料
# x = mu + sigma * np.random.randn(1000000)  # 大量資料 => 趨近常態分佈(高斯分布)
num_bins = 50
n, bins, patches = plt.hist(x, num_bins, density=1, facecolor='blue')
# print(bins, mu, sigma)
y = norm.pdf(bins, mu, sigma)  # 計算該處平均值
plt.plot(bins, y, 'r*-')
# plt.show()

# ====================================================================
# ■ 讀取csv檔，取出資料
df1 = pd.read_csv("./others/公布-違法名單總表.csv")
# print(df1.shape)
# print(df1.head())
# print(df1.columns)
# print(df1.info())

# 取出 處分字號 前10筆 違反事項
df4 = df1[['處分字號', '違反勞動基準法條款', '違反法規內容']].groupby(['違反勞動基準法條款', '違反法規內容']).count()
# print(df4.head(n=10))
df5 = df4.sort_values('處分字號', ascending=False)
print(df5.head(n=10))

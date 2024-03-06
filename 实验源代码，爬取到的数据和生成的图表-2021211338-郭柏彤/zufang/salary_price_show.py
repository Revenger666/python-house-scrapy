#由于之前写好的程序中有展示各个城市单位面积均价，直接在这里存入列表中。
#单位面积均价： 北京：103.2元/平米/月
#             广州：63.9元/平米/月
#             上海：103.5元/平米/月
#             深圳：88.5元/平米/月
#             西安：36.0元/平米/月
#查询百度各个城市的人均工资可知：
#人均工资： 北京：13567元/月  广州：11300元/月 上海：12183元/月  深圳：12300元/月 西安9011元/月

import matplotlib.pyplot as plt

space_price = [103.2, 63.9, 103.5, 88.5, 36.0]
salary = [135.67, 113.00, 121.83, 123.00, 90.11]  # 单位为百元，这样好计算一点
count = []
# 计算比值
for i in range(0,5):
    count.append(space_price[i]/salary[i])  # 用比值来表示，比值越低说明房租占工资占比小，生活成本相对低一点

# 绘图过程
city_name = ['北京', '广州', '上海', '深圳', '西安']
plt.figure(figsize=(20, 10), dpi=70)
# 消除中文乱码用的
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# 绘制直方图
plt.subplot(121)
plt.title("单位面积价格与平均月薪的比值直方图",fontsize=20)
plt.bar(city_name, count,width=0.4)
plt.ylabel("单位面积价格/人均月薪（百元）",fontsize=15)
# 绘制散点图，由于要用不同的点的颜色来表示，因此分开绘制五个点
plt.subplot(122)
plt.scatter(salary[0],space_price[0],s=60, label='北京', color='steelblue')
plt.scatter(salary[1],space_price[1],s=60, label='广州', color='brown')
plt.scatter(salary[2],space_price[2],s=60, label='上海',color='green')
plt.scatter(salary[3],space_price[3],s=60, label='深圳',color='darkorange')
plt.scatter(salary[4],space_price[4],s=60, label='西安',color='skyblue')
plt.title("人均月薪-单位面积均价散点图",fontsize=20)
plt.xlabel("人均月薪 单位：百元",fontsize=15)
plt.ylabel("单位面积均价 单位：平方米/元/月",fontsize=15)
plt.legend(fontsize=15)

plt.show()

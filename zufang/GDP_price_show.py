#由于之前写好的程序中有展示各个城市单位面积均价，直接在这里存入列表中。
#单位面积均价： 北京：103.2元/平米/月
#             广州：63.9元/平米/月
#             上海：103.5元/平米/月
#             深圳：88.5元/平米/月
#             西安：36.0元/平米/月
#通过百度查询各个城市的人均GDP可知：
#人均GDP：北京：19.03万元/人  广州：15.36万元/人  上海：17.99万元/人 深圳：18.33万元/人 西安:8.88万元/人
#采用比值的形式来展示单位面积均价/GDP ，比值越小越好，因为对于同样的单位面积，GDP越大越好

import matplotlib.pyplot as plt

GDP = [19.03, 15.36, 17.99, 18.33, 8.88]
space_price = [103.2, 63.9, 103.5, 88.5, 36.0]
count = []
# 求比值
for i in range(0,5):
    count.append(space_price[i]/GDP[i])

city_name = ['北京', '广州', '上海', '深圳', '西安']
plt.figure(figsize=(20, 10), dpi=70)
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

# 绘制直方图
plt.subplot(121)
plt.title("单位面积价格与GDP的比值直方图",fontsize=20)
plt.bar(city_name, count,width=0.4)
plt.ylabel("单位面积价格/人均GDP（万元）",fontsize=15)

# 绘制散点图
plt.subplot(122)
plt.scatter(GDP[0],space_price[0],s=60, label='北京', color='steelblue')
plt.scatter(GDP[1],space_price[1],s=60, label='广州', color='brown')
plt.scatter(GDP[2],space_price[2],s=60, label='上海',color='green')
plt.scatter(GDP[3],space_price[3],s=60, label='深圳',color='darkorange')
plt.scatter(GDP[4],space_price[4],s=60, label='西安',color='skyblue')
plt.title("GDP-单位面积均价散点图",fontsize=20)
plt.xlabel("GDP 单位：万元",fontsize=15)
plt.ylabel("单位面积均价 单位：平方米/元/月",fontsize=15)
plt.legend(fontsize=15)

plt.show()

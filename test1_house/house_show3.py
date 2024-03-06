# 该代码实现总价-直方图的绘制
import matplotlib
import matplotlib.pyplot as plt
import csv

filename = 'house_output.csv'
with open(filename,"r",encoding='utf-8') as f:  # 注意这里一定记得用utf-8打开
    data = csv.reader(f)
    total_price = []
    pos = []  # 行政区
    house_num = []  # 楼盘数量
    price_sum = []  # 平均单价的和
    test_f = 1
    for i in data:
        if test_f == 1:
            test_f = 0
        else:
            total_price.append(int(i[8]))
            pos.append(str(i[3]))
    for i in range(0,10):
        house_num.append(int(0))
        price_sum.append(int(0))

    for i in range(len(pos)):
        if pos[i] == '朝阳':
            house_num[0] = house_num[0] + 1
            price_sum[0] = price_sum[0] + total_price[i]
        if pos[i] == '丰台':
            house_num[1] = house_num[1] + 1
            price_sum[1] = price_sum[1] + total_price[i]
        if pos[i] == '顺义':
            house_num[2] = house_num[2] + 1
            price_sum[2] = price_sum[2] + total_price[i]
        if pos[i] == '通州':
            house_num[3] = house_num[3] + 1
            price_sum[3] = price_sum[3] + total_price[i]
        if pos[i] == '大兴':
            house_num[4] = house_num[4] + 1
            price_sum[4] = price_sum[4] + total_price[i]
        if pos[i] == '昌平':
            house_num[5] = house_num[5] + 1
            price_sum[5] = price_sum[5] + total_price[i]
        if pos[i] == '门头沟':
            house_num[6] = house_num[6] + 1
            price_sum[6] = price_sum[6] + total_price[i]
        if pos[i] == '房山':
            house_num[7] = house_num[7] + 1
            price_sum[7] = price_sum[7] + total_price[i]
        if pos[i] == '密云':
            house_num[8] = house_num[8] + 1
            price_sum[8] = price_sum[8] + total_price[i]
        if pos[i] == '平谷':
            house_num[9] = house_num[9] + 1
            price_sum[9] = price_sum[9] + total_price[i]
    print(house_num)
    bins_num = []
    count = 3
    for i in range(0, 11):
        if i != 0:
            price_sum[i-1] = price_sum[i-1] / house_num[i-1]  # 计算出平均单价
            count = count + house_num[i-1]
        bins_num.append(count)


    position_qu = ['chaoyang', 'fengtai', 'shunyi', 'tongzhou', 'daxing', 'changping', 'mentougou', 'fangshan', 'miyun', 'pinggu']
    print(bins_num)
    print(price_sum)
    plt.figure(figsize=(30, 10), dpi=70)
    plt.title('total_price_show', fontsize=30)
    plt.xlabel('position', fontsize=15)
    plt.ylabel('avg_unit_price/10000 yuan', fontsize=15)
    for i in range(0,10):
        plt.bar(position_qu[i], price_sum[i], width=(house_num[i]/15))
    for x,y in zip(position_qu,price_sum):
        plt.text(x,y,'%d' % y, ha='center', va='bottom', fontsize=15)
    plt.show()



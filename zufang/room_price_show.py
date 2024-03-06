#  按照居室展示，几居即几室

import json
import codecs
import matplotlib.pyplot as plt
import numpy as np

avg_price = [[]for _ in range(3)] # 均价
high_price = [[]for _ in range(3)]# 最高价
mid_price = [[]for _ in range(3)]# 中位数
low_price = [[]for _ in range(3)]# 最低价

class Read_Json_and_show():
    def reads(self,filename,city, avg_price, high_price, mid_price, low_price):       # 读取城市数据，并分别存储到需要的数组中
        temp_price = []  # 临时用的总价
        temp_high_price = []  # 临时用的最高价
        temp_low_price = []  # 临时用的最低价
        temp_mid_price_count = [[]for _ in range(3)]
        house_type = 0  # 1表示1居 2表示2居 3表示3居
        count = []  # 居室个数计数器
        for i in range(0, 3):   # 给初值
            count.append(0)
            temp_price.append(0)
            temp_low_price.append(99999999)
            temp_high_price.append(0)

        with codecs.open(filename, 'r', encoding='utf-8') as f:
            read = f.readlines()
        for index, info in enumerate(read):
                data = json.loads(info)
                value = list(data.values())
                # value保存了每一行的数据的值，以列表形式。
                # 数据处理，拆分出价格
                temp_price_read = value[1].split('-')
                price = temp_price_read[0]
                price = int(price)
                # 数据处理，拆分出居室情况
                temp_house_type = value[5].split('室')
                temp_house_type = temp_house_type[0].split('/ ')
                if temp_house_type[len(temp_house_type)-1] == '1':
                    house_type = 1
                if temp_house_type[len(temp_house_type)-1] == '2':
                    house_type = 2
                if temp_house_type[len(temp_house_type)-1] == '3':
                    house_type = 3
                # print(house_type)

                if house_type == 1:  # 1室的情况
                    count[0] += 1
                    if price > temp_high_price[0]:  # 最高价
                        temp_high_price[0] = price
                    if price < temp_low_price[0]:  # 最低价
                        temp_low_price[0] = price
                    temp_price[0] += price
                    temp_mid_price_count[0].append(price)

                if house_type == 2:  # 2室的情况
                    count[1] += 1
                    if price > temp_high_price[1]:  # 最高价
                        temp_high_price[1] = price
                    if price < temp_low_price[1]:  # 最低价
                        temp_low_price[1] = price

                    temp_price[1] += price
                    temp_mid_price_count[1].append(price)

                if house_type == 3:  # 3室的情况
                    count[2] += 1
                    if price > temp_high_price[2]:  # 最高价
                        temp_high_price[2] = price
                    if price < temp_low_price[2]:  # 最低价
                        temp_low_price[2] = price
                    temp_price[2] += price
                    temp_mid_price_count[2].append(price)

        for i in range(0, 3):
            # 将处理完毕的数据放入列表中
            temp_price[i] = float(temp_price[i]/count[i]) # 均价
            avg_price[i][city] = temp_price[i]
            high_price[i][city] = temp_high_price[i]
            low_price[i][city] = temp_low_price[i]
            temp_mid_price_count[i].sort()
            mid_price[i][city] = temp_mid_price_count[i][int(len(temp_mid_price_count[i])/2)]


if __name__ == '__main__':
    read_json = Read_Json_and_show()
    #  读文件并按照路径依次处理数据
    path1 = 'scrapy-beijing-zufang.json'
    path2 = 'scrapy-guangzhou-zufang.json'
    path3 = 'scrapy-shanghai-zufang.json'
    path4 = 'scrapy-shenzhen-zufang.json'
    path5 = 'scrapy-xian-zufang.json'
    # 给嵌套列表一个初值，这样方便后续数据处理
    for i in range(0, 3):
        for j in range(0, 5):
            avg_price[i].append(0)
            high_price[i].append(0)
            low_price[i].append(0)
            mid_price[i].append(0)

    # 读取并处理数据
    read_json.reads(path1, 0, avg_price, high_price, mid_price, low_price)
    read_json.reads(path2, 1, avg_price, high_price, mid_price, low_price)
    read_json.reads(path3, 2, avg_price, high_price, mid_price, low_price)
    read_json.reads(path4, 3, avg_price, high_price, mid_price, low_price)
    read_json.reads(path5, 4, avg_price, high_price, mid_price, low_price)

    print(avg_price)
    print(high_price)
    print(low_price)
    print(mid_price)

    # 绘图步骤
    city_name = ['北京', '广州', '上海', '深圳', '西安']
    plt.figure(figsize=(30, 30), dpi=70)
    bar_width = 0.23
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

    # 均价
    plt.subplot(221)
    plt.title('平均价格 ', fontsize=25)
    # 绘制成一个X坐标对应多个直方图的，这样方便数据的对比和展示观看
    plt.bar(x=np.arange(len(city_name)), height=avg_price[0], width=bar_width,label='1居',color='steelblue')
    plt.bar(x=np.arange(len(city_name))+bar_width, height=avg_price[1],width=bar_width, label='2居',color='brown')
    plt.bar(x=np.arange(len(city_name))+bar_width*2, height=avg_price[2], width=bar_width, label='3居',color='darkorange')
    plt.xticks(np.arange(5)+0.2,city_name,fontsize=15)
    plt.ylabel('价格：元/月')
    # 绘制图例
    plt.legend()
    # 给图像上端增添数据显示
    for x, y in enumerate(avg_price[0]):
        plt.text(x, y + 0.2, "%s" % round(y, 1), ha='center')
    for x, y in enumerate(avg_price[1]):
        plt.text(x+bar_width, y + 0.2, "%s" % round(y, 1), ha='center')
    for x, y in enumerate(avg_price[2]):
        plt.text(x+bar_width*2, y + 0.2, "%s" % round(y, 1), ha='center')

    # 最高价

    plt.subplot(222)
    plt.title('最高价格 ', fontsize=25)
    # 绘制成一个X坐标对应多个直方图的，这样方便数据的对比和展示观看
    plt.bar(x=np.arange(len(city_name)), height=high_price[0], width=bar_width, label='1居', color='steelblue')
    plt.bar(x=np.arange(len(city_name)) + bar_width, height=high_price[1], width=bar_width, label='2居', color='brown')
    plt.bar(x=np.arange(len(city_name)) + bar_width * 2, height=high_price[2], width=bar_width, label='3居',
            color='darkorange')
    plt.xticks(np.arange(5) + 0.2, city_name, fontsize=15)
    plt.ylabel('价格：元/月')
    plt.legend()
    # 给图像上端增添数据显示
    for x, y in enumerate(high_price[0]):
        plt.text(x, y + 0.2, "%s" % round(y, 1), ha='center')
    for x, y in enumerate(high_price[1]):
        plt.text(x + bar_width, y + 0.2, "%s" % round(y, 1), ha='center')
    for x, y in enumerate(high_price[2]):
        plt.text(x + bar_width * 2, y + 0.2, "%s" % round(y, 1), ha='center')

    # 最低价
    plt.subplot(223)
    plt.title('最低价格 ', fontsize=25)
    # 绘制成一个X坐标对应多个直方图的，这样方便数据的对比和展示观看
    plt.bar(x=np.arange(len(city_name)), height=low_price[0], width=bar_width, label='1居', color='steelblue')
    plt.bar(x=np.arange(len(city_name)) + bar_width, height=low_price[1], width=bar_width, label='2居', color='brown')
    plt.bar(x=np.arange(len(city_name)) + bar_width * 2, height=low_price[2], width=bar_width, label='3居',
            color='darkorange')
    plt.xticks(np.arange(5) + 0.2, city_name, fontsize=15)
    plt.ylabel('价格：元/月')
    plt.legend()
    # 给图像上端增添数据显示
    for x, y in enumerate(low_price[0]):
        plt.text(x, y + 0.2, "%s" % round(y, 1), ha='center')
    for x, y in enumerate(low_price[1]):
        plt.text(x + bar_width, y + 0.2, "%s" % round(y, 1), ha='center')
    for x, y in enumerate(low_price[2]):
        plt.text(x + bar_width * 2, y + 0.2, "%s" % round(y, 1), ha='center')

    # 中位数
    plt.subplot(224)
    plt.title('中位数价格 ', fontsize=25)
    plt.bar(x=np.arange(len(city_name)), height=mid_price[0], width=bar_width, label='1居', color='steelblue')
    plt.bar(x=np.arange(len(city_name)) + bar_width, height=mid_price[1], width=bar_width, label='2居', color='brown')
    plt.bar(x=np.arange(len(city_name)) + bar_width * 2, height=mid_price[2], width=bar_width, label='3居',
            color='darkorange')
    plt.xticks(np.arange(5) + 0.2, city_name, fontsize=15)
    plt.ylabel('价格：元/月')
    plt.legend()
    # 给图像上端增添数据显示
    for x, y in enumerate(mid_price[0]):
        plt.text(x, y + 0.2, "%s" % round(y, 1), ha='center')
    for x, y in enumerate(mid_price[1]):
        plt.text(x + bar_width, y + 0.2, "%s" % round(y, 1), ha='center')
    for x, y in enumerate(mid_price[2]):
        plt.text(x + bar_width * 2, y + 0.2, "%s" % round(y, 1), ha='center')

    plt.show()

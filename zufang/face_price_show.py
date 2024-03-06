#  该文件实现了对五个不同城市按照房屋面向来进行均价的比较

import json
import codecs
import matplotlib.pyplot as plt
import numpy as np

avg_price = [] # 均价
count_list = [] # 各种面向的数量

class Read_Json_and_show():
    def reads(self,filename,city, avg_price,count_list):       # 读取城市数据，并分别存储到需要的数组中
        temp_price = []  # 临时用存储价格的列表
        count = []  # 临时用存储各个面向计数的列表
        for i in range(0,4): # 0123分别表示东南西北
            count.append(0)
            temp_price.append(0)

        with codecs.open(filename, 'r', encoding='utf-8') as f:
            read = f.readlines()
        # 打开文件并逐行读取
        for index, info in enumerate(read):
            data = json.loads(info)
            value = list(data.values())
            # value保存了每一行的数据的值，以列表形式。

            # 不断拆分，最后拆出来需要的面向
            temp_price_read = value[1].split('-')
            price = temp_price_read[0]
            price = int(price)
            temp_face_read = value[5].split('㎡ /')
            temp_face_read = temp_face_read[1].split(' / ')
            temp_face_read = temp_face_read[0].split('在')

            if len(temp_face_read) == 1:
                temp_face_read = temp_face_read[0].split('室')
                if len(temp_face_read) == 1:
                    temp_face_read = temp_face_read[0].split(' ')
                    # 由于同时一组数据可能有多个面向，故如面向东 南，则东，南均各统计一次。
                    for face in temp_face_read:
                        if face == '东':
                            temp_price[0] += price
                            count[0] += 1
                        if face == '南':
                            temp_price[1] += price
                            count[1] += 1
                        if face == '西':
                            temp_price[2] += price
                            count[2] += 1
                        if face == '北':
                            temp_price[3] += price
                            count[3] += 1
        # 计算平均价格
        for i in range(len(count)):
            temp_price[i] = temp_price[i]/count[i]

        # 将价格放入列表中
        avg_price.append(temp_price)
        count_list.append(count)


if __name__ == '__main__':
    read_json = Read_Json_and_show()
    # 存储路径
    path1 = 'scrapy-beijing-zufang.json'
    path2 = 'scrapy-guangzhou-zufang.json'
    path3 = 'scrapy-shanghai-zufang.json'
    path4 = 'scrapy-shenzhen-zufang.json'
    path5 = 'scrapy-xian-zufang.json'
    # 分别对五个城市进行读取和分析的操作
    read_json.reads(path1, 0, avg_price, count_list)
    read_json.reads(path2, 1, avg_price, count_list)
    read_json.reads(path3, 2, avg_price, count_list)
    read_json.reads(path4, 3, avg_price, count_list)
    read_json.reads(path5, 4, avg_price, count_list)
    # 查看分析结果
    print(avg_price)
    print(count_list)
    # 绘图，分别将五个城市的直方图进行绘制
    face_name = ['东','南','西','北']
    plt.figure(figsize=(30, 30), dpi=70)
    bar_width = 0.1   # 条宽偏移
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

    #  通过偏移来绘制直方图，以达到一个横坐标能显示多个直方图的效果，同时便于区分颜色和图例
    plt.title('各城市面向以及价格比较', fontsize=25)
    plt.bar(x=np.arange(len(face_name)), height=avg_price[0], width=bar_width, label='北京', color='steelblue')
    plt.bar(x=np.arange(len(face_name)) + bar_width, height=avg_price[1], width=bar_width, label='广州', color='brown')
    plt.bar(x=np.arange(len(face_name)) + bar_width * 2, height=avg_price[2], width=bar_width, label='上海',color='greenyellow')
    plt.bar(x=np.arange(len(face_name)) + bar_width * 3, height=avg_price[3], width=bar_width, label='深圳',color='darkorange')
    plt.bar(x=np.arange(len(face_name)) + bar_width * 4, height=avg_price[4], width=bar_width, label='西安',color='skyblue')
    plt.xticks(np.arange(4) + 0.2, face_name,fontsize=20)
    plt.ylabel('价格：元/月',fontsize=20)
    # 显示图例
    plt.legend(fontsize=10)
    # 为柱状图在顶部添加数据信息
    for x, y in enumerate(avg_price[0]):
        plt.text(x, y + 0.2, "%s" % round(y, 1), ha='center')
    for x, y in enumerate(avg_price[1]):
        plt.text(x + bar_width, y + 0.2, "%s" % round(y, 1), ha='center')
    for x, y in enumerate(avg_price[2]):
        plt.text(x + bar_width * 2, y + 0.2, "%s" % round(y, 1), ha='center')
    for x, y in enumerate(avg_price[3]):
        plt.text(x + bar_width * 3, y + 0.2, "%s" % round(y, 1), ha='center')
    for x, y in enumerate(avg_price[4]):
        plt.text(x + bar_width * 4, y + 0.2, "%s" % round(y, 1), ha='center')

    plt.show()

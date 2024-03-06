#  该文件实现了按照板块来展示不同城市不同板块的均价

import json
import codecs
import matplotlib.pyplot as plt

avg_price = []   # 均价
pos_list = []    # 板块名
count_list = []     # 板块数量

class Read_Json_and_show():
    def reads(self,filename,city, avg_price, pos_list,count_list):       # 读取城市数据，并分别存储到需要的数组中
        temp_price = []
        pos_name = []
        count = []
        for i in range(0,3000):
            pos_name.append("")
            count.append(0)
            temp_price.append(0)

        with codecs.open(filename, 'r', encoding='utf-8') as f:
            read = f.readlines()
        for index, info in enumerate(read):
            data = json.loads(info)
            value = list(data.values())
            # value保存了每一行的数据的值，以列表形式。
            # 划分出价格
            temp_price_read = value[1].split('-')
            price = temp_price_read[0]
            price = int(price)
            # 划分出板块
            temp_pos_read = value[5].split('-')
            if len(temp_pos_read) > 1:   # 先确定板块的位置，再将干扰的数据剔除
                temp_pos_read = temp_pos_read[1].split('㎡')
                if len(temp_pos_read) == 1:
                    pos = str(temp_pos_read[0])
                    # 通过遍历的方式来检查已经建立的板块名列表，重复则数量加一，无重复则将这个板块名加入板块列表
                    flag = -1
                    for j in range(len(pos_name)):
                        if pos_name[j] == pos or pos_name[j] == "":
                            flag = j
                            break

                    pos_name[flag] = pos
                    count[flag] += 1
                    temp_price[flag] += price
        # 将之前预设的列表里多余的空项去除掉
        while temp_price[-1] == 0:
            temp_price.pop()
        while pos_name[-1] == "":
            pos_name.pop()
        while count[-1] == 0:
            count.pop()
        for i in range(len(count)):
            temp_price[i] = temp_price[i]/count[i]
        # 将最后得到的列表写入总列表中
        avg_price.append(temp_price)
        pos_list.append(pos_name)
        count_list.append(len(temp_price))


if __name__ == '__main__':
    read_json = Read_Json_and_show()
    path1 = 'scrapy-beijing-zufang.json'
    path2 = 'scrapy-guangzhou-zufang.json'
    path3 = 'scrapy-shanghai-zufang.json'
    path4 = 'scrapy-shenzhen-zufang.json'
    path5 = 'scrapy-xian-zufang.json'
    # 按照不同城市进行数据的读取和存储操作
    read_json.reads(path1, 0, avg_price, pos_list, count_list)
    read_json.reads(path2, 1, avg_price, pos_list, count_list)
    read_json.reads(path3, 2, avg_price, pos_list, count_list)
    read_json.reads(path4, 3, avg_price, pos_list, count_list)
    read_json.reads(path5, 4, avg_price, pos_list, count_list)
    # 输出读取结果进行观察
    print(avg_price)
    print(pos_list)
    print(count_list)

    # 数据太多了，只保留一部分 ，这里只保留15个板块的数据
    for i in range(5):
        while len(avg_price[i]) > 15:
            avg_price[i].pop()
        while len(pos_list[i]) > 15:
            pos_list[i].pop()

    city_name = ['北京', '广州', '上海', '深圳', '西安']
    # 一些预设参数
    plt.figure(figsize=(50, 50), dpi=70)
    bar_width = 0.23
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

    # 分开画不同城市的不同板块的展示图
    # 北京
    plt.subplot(321)
    plt.bar(pos_list[0],avg_price[0])
    plt.title("北京不同板块均价展示图")
    plt.ylabel("价格：元/月")
    # 广州
    plt.subplot(322)
    plt.bar(pos_list[1], avg_price[1])
    plt.title("广州不同板块均价展示图")
    plt.ylabel("价格：元/月")
    # 上海
    plt.subplot(323)
    plt.bar(pos_list[2], avg_price[2])
    plt.title("上海不同板块均价展示图")
    plt.ylabel("价格：元/月")
    # 深圳
    plt.subplot(324)
    plt.bar(pos_list[3], avg_price[3])
    plt.title("深圳不同板块均价展示图")
    plt.ylabel("价格：元/月")
    # 西安
    plt.subplot(325)
    plt.bar(pos_list[4], avg_price[4])
    plt.title("西安不同板块均价展示图")
    plt.ylabel("价格：元/月")

    plt.show()
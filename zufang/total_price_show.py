# 该文件实现了对五个城市的租房价格的均价，中位数，最高价，最低价和单位面积的均价，中位数，最高价，最低价的比较分析和图表绘制
import json
import codecs
import re
import matplotlib.pyplot as plt


total_avg_price = []  # 均价
total_high_price = []  # 最高价
total_mid_price = []  # 中位数
total_low_price = []  # 最低价
space_avg_price = []  # 均价（单位面积）
space_high_price = []  # 最高价（单位面积）
space_low_price = []  # 最低价（单位面积）
space_mid_price = []  # 中位数 （单位面积）

class Read_Json_and_show():
    def reads(self,filename,city, total_avg_price, total_high_price, total_mid_price, total_low_price, space_avg_price,
              space_high_price, space_low_price, space_mid_price):       # 读取城市数据，并分别存储到需要的数组中
        temp_total_price = 0
        temp_space_price = 0
        temp_space_high_price = 0
        temp_space_low_price = 9999999
        temp_total_high_price = 0
        temp_total_low_price = 9999999
        with codecs.open(filename,'r',encoding='utf-8') as f:
            # 打开并读取文件
            read = f.readlines()
            total_mid_price_count = []
            space_mid_price_count = []
            for index, info in enumerate(read):  # 逐行读取
                data = json.loads(info)
                value = list(data.values())
                # value保存了每一行的数据的值，以列表形式。

                number = re.compile(r'^[-+]?[0-9]+\.[0-9]+$')  # 正则式判断是否是小数
                # 划分出价格
                temp_price = value[1].split('-')
                price = temp_price[0]
                price = int(price)
                # 划分出面积
                temp_space = value[5].split("㎡")
                temp_space = temp_space[0].split("/ ")
                if len(temp_space) == 1:
                    temp_space = temp_space[0].split("-")
                    space = temp_space[0]
                    space = float(space)
                else:
                    temp_space2 = temp_space[1].split("-")
                    # 判断这个数是否为小数，是则说明是面积，这里保留了最小面积作为参考（否则就是异常数据，需要被忽略）
                    result = number.match(temp_space2[0])
                    if result:
                        space = temp_space2[0]
                        space = float(space)
                    else:  # 保留最小的面积（如20-25㎡则将space看做20）
                        temp_space = temp_space[2].split("-")
                        space = temp_space[0]
                        space = float(space)
                # print(space)
                if price > temp_total_high_price:    # 最高价
                    temp_total_high_price = price
                if price < temp_total_low_price:     # 最低价
                    temp_total_low_price = price
                temp_total_price += price      # 总价,均价出循环了计算
                total_mid_price_count.append(price)  # 中位数，同样出循环了计算

                space_price = float(price/space)
                if space_price > temp_space_high_price:  # 最高价（单位面积）
                    temp_space_high_price = space_price
                if space_price < temp_space_low_price:  # 最低价（单位面积）
                    temp_space_low_price = space_price
                temp_space_price += space_price  # 总价 （单位面积）
                space_mid_price_count.append(space_price)   # 中位数（单位面积）

            #  均价
            total_avg_price.append(float(temp_total_price/3000))
            space_avg_price.append(float(temp_space_price/3000))
            #  最高价
            total_high_price.append(float(temp_total_high_price))
            space_high_price.append(float(temp_space_high_price))
            #  最低价
            total_low_price.append(float(temp_total_low_price))
            space_low_price.append(float(temp_space_low_price))
            #  中位数
            total_mid_price_count.sort()
            space_mid_price_count.sort()
            total_mid_price.append(float(total_mid_price_count[1499]))
            space_mid_price.append(float(space_mid_price_count[1499]))


if __name__ == '__main__':
    read_json = Read_Json_and_show()
    path1 = 'scrapy-beijing-zufang.json'
    path2 = 'scrapy-guangzhou-zufang.json'
    path3 = 'scrapy-shanghai-zufang.json'
    path4 = 'scrapy-shenzhen-zufang.json'
    path5 = 'scrapy-xian-zufang.json'
    # 读取并处理数据
    read_json.reads(path1, 1, total_avg_price, total_high_price, total_mid_price, total_low_price, space_avg_price,
                   space_high_price, space_low_price, space_mid_price)
    read_json.reads(path2, 2, total_avg_price, total_high_price, total_mid_price, total_low_price, space_avg_price,
                   space_high_price, space_low_price, space_mid_price)
    read_json.reads(path3, 3, total_avg_price, total_high_price, total_mid_price, total_low_price, space_avg_price,
                   space_high_price, space_low_price, space_mid_price)
    read_json.reads(path4, 4, total_avg_price, total_high_price, total_mid_price, total_low_price, space_avg_price,
                   space_high_price, space_low_price, space_mid_price)
    read_json.reads(path5, 5, total_avg_price, total_high_price, total_mid_price, total_low_price, space_avg_price,
                   space_high_price, space_low_price, space_mid_price)

    # 输出展示处理结果
    print(total_avg_price)
    print(total_high_price)
    print(total_low_price)
    print(total_mid_price)
    print(space_avg_price)
    print(space_high_price)
    print(space_low_price)
    print(space_mid_price)

    # 绘直方图图
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    city_name = ['北京', '广州', '上海', '深圳', '西安']
    plt.figure(figsize=(30, 30), dpi=70)
    bar_width = 0.4

    # 总平均租金展示图的绘制，共八个子图
    plt.subplot(241)
    plt.title('总价平均价格', fontsize=25)
    plt.bar(city_name,total_avg_price)
    plt.ylabel('价格：元/月')
    for x, y in enumerate(total_avg_price):
        plt.text(x, y + 0.1, "%s" % round(y, 1), ha='center')
    # 总最高租金
    plt.subplot(242)
    plt.title('总价最高价格', fontsize=25)
    plt.bar(city_name, total_high_price)
    plt.ylabel('价格：元/月')
    for x, y in enumerate(total_high_price):
        plt.text(x, y + 0.1, "%s" % round(y, 1), ha='center')
    # 总最低租金
    plt.subplot(243)
    plt.title('总价最低价格', fontsize=25)
    plt.bar(city_name, total_low_price)
    plt.ylabel('价格：元/月')
    for x, y in enumerate(total_low_price):
        plt.text(x, y + 0.1, "%s" % round(y, 1), ha='center')
    # 总中位数租金
    plt.subplot(244)
    plt.title('总价中位数价格', fontsize=25)
    plt.bar(city_name, total_mid_price)
    plt.ylabel('价格：元/月')
    for x, y in enumerate(total_mid_price):
        plt.text(x, y + 0.1, "%s" % round(y, 1), ha='center')
    # 单位面积平均租金展示图的绘制
    plt.subplot(245)
    plt.title('单位面积均价', fontsize=25)
    plt.bar(city_name, space_avg_price)
    plt.ylabel('价格：元/月')
    for x, y in enumerate(space_avg_price):
        plt.text(x, y + 0.1, "%s" % round(y, 1), ha='center')
    # 单位面积最高租金
    plt.subplot(246)
    plt.title('单位面积最高价格', fontsize=25)
    plt.bar(city_name, space_high_price)
    plt.ylabel('价格：元/月')
    for x, y in enumerate(space_high_price):
        plt.text(x, y + 0.1, "%s" % round(y, 1), ha='center')
    # 单位面积最低租金
    plt.subplot(247)
    plt.title('单位面积最低价格', fontsize=25)
    plt.bar(city_name, space_low_price)
    plt.ylabel('价格：元/月')
    for x, y in enumerate(space_low_price):
        plt.text(x, y + 0.1, "%s" % round(y, 1), ha='center')
    # 单位面积中位数租金
    plt.subplot(248)
    plt.title('单位面积中位数价格', fontsize=25)
    plt.bar(city_name, space_mid_price)
    plt.ylabel('价格：元/月')
    for x, y in enumerate(space_mid_price):
        plt.text(x, y + 0.1, "%s" % round(y, 1), ha='center')

    plt.show()

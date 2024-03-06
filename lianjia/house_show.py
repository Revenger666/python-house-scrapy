#本代码实现了对csv文件的新房数据可视化处理，转换为散点图展示单价与总价的关系

import matplotlib
import matplotlib.pyplot as plt
import csv

filename = 'house_output.csv'
with open(filename,"r",encoding='utf-8') as f:  #注意这里一定记得用utf-8打开
    data = csv.reader(f)
    unit_price = []
    total_price = []
    house_type = []
    test_f = 1
    for i in data:
        if test_f == 1:
            test_f = 0
        else:
            unit_price.append(int(i[7]))
            total_price.append(int(i[8]))
            house_type.append(i[1])
    up1 = []
    up2 = []
    up3 = []
    tp1 = []
    tp2 = []
    tp3 = []
    for i in range(len(unit_price)):
        if house_type[i] == '住宅':
            up1.append(int(unit_price[i]))
            tp1.append(int(total_price[i]))
        if house_type[i] == '别墅':
            up2.append(int(unit_price[i]))
            tp2.append(int(total_price[i]))
        if house_type[i] == '商业':
            up3.append(int(unit_price[i]))
            tp3.append(int(total_price[i]))

    for i in range(len(tp1)):
        cur_index = i
        while tp1[cur_index - 1] > tp1[cur_index] and cur_index - 1 >= 0:
            tp1[cur_index], tp1[cur_index - 1] = tp1[cur_index - 1], tp1[cur_index]
            up1[cur_index], up1[cur_index - 1] = up1[cur_index - 1], up1[cur_index]
            cur_index -= 1
    for i in range(len(tp2)):
        cur_index = i
        while tp2[cur_index - 1] > tp2[cur_index] and cur_index - 1 >= 0:
            tp2[cur_index], tp2[cur_index - 1] = tp2[cur_index - 1], tp2[cur_index]
            up2[cur_index], up2[cur_index - 1] = up2[cur_index - 1], up2[cur_index]
            cur_index -= 1
    for i in range(len(tp3)):
        cur_index = i
        while tp3[cur_index - 1] > tp3[cur_index] and cur_index - 1 >= 0:
            tp3[cur_index], tp3[cur_index - 1] = tp3[cur_index - 1], tp3[cur_index]
            up3[cur_index], up3[cur_index - 1] = up3[cur_index - 1], up3[cur_index]
            cur_index -= 1
    #print(unit_price)
    #print(total_price)
    #print(house_type)

    color_list = ['#FF8C00', '#00FF00', '#0000FF']  #住宅，别墅，商业
    types = ['residence', 'villa', 'commercial']

    plt.figure(figsize=(30, 10), dpi=70)
    plt.title('total_price and unit_price for different type house')
    plt.scatter(tp1, up1, s=30, c=color_list[0])
    plt.scatter(tp2, up2, s=30, c=color_list[1])
    plt.scatter(tp3, up3, s=30, c=color_list[2])
    plt.xlabel('total_price/10000 yuan')
    plt.ylabel('unit_price/yuan')
    plt.legend(loc='lower right',title='house_type',labels=types)
    plt.show()

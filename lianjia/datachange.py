import csv
import json
import codecs

'''
将json文件格式转为csv文件格式并保存。
'''

class Json_Csv():

    # 初始化方法，创建csv文件。
    def __init__(self):
        self.save_csv = open('house_output.csv', 'w', encoding='utf-8', newline='')

        self.write_csv = csv.writer(self.save_csv, delimiter=',')  # 以，为分隔符
    def trans(self, filename):
        with codecs.open(filename, 'r', encoding='utf-8') as f:  #读取json文件
            read = f.readlines()
            flag = True
            for index, info in enumerate(read):
                data = json.loads(info)
                if flag:  # 第一行当做head
                    keys = list(data.keys())  # 将得到的keys用列表的形式封装好，才能写入csv
                    self.write_csv.writerow(keys)#以,为分隔符将表头写入csv中
                    flag = False  # 释放
                value = list(data.values())  # 写入values，也要是列表形式

                temp = value[6]#将面积只保留最小面积，并转换为int形
                if type(temp) == str:
                    list_temp = temp.split(' ')
                    list_temp = list_temp[1].split('-')
                    list_temp = list_temp[0].split('㎡')
                    value[6] = int(list_temp[0])

                value[7] = int(value[7])#将单价转换为Int形式，单位为元

                temp = value[8]#将总价只保留最小的，转换为int型，单位为万元
                if type(temp) == str:
                    list_temp = temp.split('价')
                    list_temp = list_temp[1].split('-')
                    list_temp = list_temp[0].split('(')
                    value[8] = int(list_temp[0])

                self.write_csv.writerow(value)#以,为分隔符将数据写入表格中
            self.save_csv.close()  # 写完就关闭


if __name__ == '__main__':
    json_csv = Json_Csv()
    path = 'scrapy-test-firsthand.json'
    json_csv.trans(path)
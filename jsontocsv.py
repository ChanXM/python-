import csv
import json
import sys
import re
# sys.setdefaultencoding('utf8')
import codecs
import jieba.analyse
import pandas as pd
from pandas import DataFrame as df



def json_to_csv():
    json_file=open('D:/2019/python/DANGDANG_DATA/DANGDANGdata.json', 'r',encoding='utf-8')
    csv_file = open('D:/2019/python/DANGDANG_DATA/DANGDANGdata.csv', 'w',newline='')
    flag = True
    writer = csv.writer(csv_file, dialect='excel', quoting=csv.QUOTE_ALL)
    for line in json_file:
        dic = json.loads(line[0:-1])
        if flag:
            # 获取属性列表
            keys = list(dic.keys())
            # print(keys)
            writer.writerow(keys)  # 将属性列表写入csv中
            flag = False
        # 读取json数据的每一行，将values数据一次一行的写入csv中
        writer.writerow(list(dic.values()))

    df=pd.read_csv('D:/2019/python/DANGDANG_DATA/DANGDANGdata.csv',encoding='gb18030').sort_values(by='comment',ascending=False)
    df.to_csv('sorted.csv',index=False,encoding='gb18030')



    csv_file.close()
    json_file.close()


def brand_data():
    csv_file = open('D:/2019/python/DANGDANG_DATA/sorted.csv', 'r')
    outfile = open('D:/2019/python/DANGDANG_DATA/result.csv', 'w')
    for row in csv_file.readlines():

        a = re.sub(u"\\【.*?】|\\s{1}.*?手机\\n", "", row)

        outfile.write(a)

    csv_file.close()
    # with open('D:/2019/python/DANGDANG_DATA/sorted.csv', 'r') as file:
    #     reader = csv.DictReader(file)
    #     column = [row['name'] for row in reader]
    #     for mobile in column:
    #         if mobile[0] == "【":
    #             mobile = mobile[6:]
    #         title_split = mobile.split(" ")
    #         for i in range(1, len(title_split)):
    #             if 'GB' in title_split[i]:
    #                 title_extract = title_split[:i]
    #                 break
    #             elif 'Hz' in title_split[i]:
    #                 title_extract = title_split[:i]
    #                 break
    #             elif '万' in title_split[i]:
    #                 title_extract = title_split[:i]
    #                 break
    #             elif 'mAh' in title_split[i]:
    #                 title_extract = title_split[:i]
    #                 break
    #             elif '版' in title_split[i]:
    #                 title_extract = title_split[:(i + 1)]
    #                 break
                #        elif title_split[i].decode("utf-8")  >= u'\u4e00' and title_split[i].decode("utf-8")  <= u'\u9fa5':    #判断以汉字开头
                # elif is_chinese(title_split[i]):
                #     title_extract = title_split[:i]
                #     break
            #     else:
            #         title_extract = title_split[:5]
            # mobile = " ".join(title_extract)
            # outfile.write(mobile)
            # outfile.write()
    csv_file.close()
    outfile.close()



    # for row in csv_file.readlines():
    #
    #     a = re.sub(u"\\【.*?】", "", row)
    #
    #     outfile.write(a)

    # csv_file.close()
    outfile.close()
        # fileout.write(line.replace('【当当自营】', ''))
        # line=line.strip(' ')
        # n = 2
        # for ch[n] in line:
        #     if u'\u4e00'<= ch[n][0]<=u'\u9fff':
        #         ch = ch[0:n]
        #         fileout.write(line.replace(line,ch))
        #     else:
        #         n = n+1














def is_chinese(string):
    for ch in string:
        if ch == "畅":  # 考虑到华为畅享系列
            return False
        elif u'\u4e00' <= ch <= u'\u9fff':
            return True

    return False




if __name__ == '__main__':

    json_to_csv()
    brand_data()
    # data_deal()
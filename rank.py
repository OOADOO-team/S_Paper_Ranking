import bean.Paper as p
from openpyxl import load_workbook
import bean.Paper as p
import os
import re


def rank_simple(paperlist, alpha):
    # 读取publish的name和对应的IF值
    pe = load_workbook("dao\publish.xlsx")  # 默认可读写，若有需要可以指定write_only和read_only为True
    sheet = pe.worksheets[0]
    print("load database is correct")
    length = len(sheet["B"])
    publish_name = []
    publish_if = []
    for i in range(1, length + 1):  # range默认从0开始，到后面参数的-1结束，而openpyxl都是从第一行第一列开始的，所以参数为1，maxC+1；意思就是遍历第一列到最后一列，
        publish_name.append(str(sheet.cell(i, 1).value).upper())
        # print(sheet.cell(i, 2).value)
        publish_if.append(float(sheet.cell(i, 2).value))

    print("read publish is correct")
    # ==== 读取paper的citation的值，找到对应的publish并赋值。最后加权排序 =====

    total_list = []

    # 根据10/79.258得到的publish_value应该乘的weight
    weight = 0.12617
    for paper in paperlist:
        # print("跑paperlist呢")
        citation = paper.citations_number
        publish = paper.published_in
        valuep = 0
        valuec = find_citation_value(citation)
        flag = False

        # 找publish
        for i in range(length):
            if str(publish)[0] == "《":
                publish = str(publish)[1:-1]
            judge = re.search(publish_name[i],publish.upper())
            if judge is not None:
                valuep = publish_if[i] * weight
                # print(publish)
                flag = True
                break
        if flag==False:
            valuep = 0.189255
        alpha = int(alpha)
        total_value = valuep * alpha + (100 - alpha) * valuec
        total_list.append((paper, total_value))

    # 根据total_value对paper进行排序
    _list = sorted(total_list, key=lambda x: x[1])
    return_list = [item[0] for item in _list]
    for item in _list:
        print(item[0].title,item[1])
    return return_list


def find_citation_value(citation):
    if citation > 1000:
        return 10
    elif citation > 900:
        return 9
    elif citation > 800:
        return 8
    elif citation > 700:
        return 7
    elif citation > 600:
        return 6
    elif citation > 500:
        return 5
    elif citation > 400:
        return 4
    elif citation > 300:
        return 3
    elif citation > 200:
        return 2
    else:
        return 1

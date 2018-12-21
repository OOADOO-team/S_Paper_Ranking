from openpyxl import load_workbook
from bean.Paper import PaperBean
import re


# ================================================================
def get_infomation(keyword):
    """
        通过获取用户输入于界面的keyword,搜索数据库中author和title是否有吻合的关键词
        如果有吻合的关键词，则利用PaperBean构造出paper
        将paper加入result中，最后返回result list

        :param keyword: 用户输入于界面的keyword
        :return result： paper list

    """
    wb = load_workbook("database.xlsx")
    sheet = wb.worksheets[0]
    length = len(sheet["B"])
    result = []
    # get each line of xlsx
    for i in range(length):
        # get the value of B0 to Bn
        value_of_blockBn = str(sheet.cell(row=i, column=2).value).upper()
        value_of_blockCn = str(sheet.cell(row=i, column=3).value).upper()
        data_U = keyword.upper()
        # remove the useless word
        judge1 = re.search(data_U, value_of_blockBn)
        judge2 = re.search(data_U, value_of_blockCn)
        if judge1 is not None or judge2 is not None:
            paper = PaperBean(number=i,
                              title=str(sheet.cell(row=i, column=2).value),
                              authors=str(sheet.cell(row=i, column=3).value),
                              published_in=str(sheet.cell(row=i, column=4).value),
                              url=str(sheet.cell(row=i, column=6).value),
                              abstract=str(sheet.cell(row=i, column=7).value),
                              citations=sheet.cell(row=i, column=8).value,
                              references=sheet.cell(row=i, column=9).value)
            result.append(paper)
    return result


def get_refer_and_cita(citation_list):
    """
        通过键入citation_list（对应paper的编号）
        找寻对应citation_list中的paper
        将paper加入result中，最后返回result list

        :param citation_list: paper的编号
        :return result： paper list

    """
    wb = load_workbook("E:\ChormeDownload\S_Paper_Ranking\database.xlsx")
    sheet = wb.worksheets[0]
    length = len(citation_list)
    result = []
    # get each line of xlsx
    for i in range(length):
        # 取得reference的编号，从而得到整篇paper
        row_num = citation_list[i]
        print(sheet.cell(row=row_num, column=1).value)
        paper = PaperBean(number=sheet.cell(row=row_num, column=1).value,
                          title=str(sheet.cell(row=row_num, column=2).value),
                          authors=str(sheet.cell(row=row_num, column=3).value),
                          published_in=str(sheet.cell(row=row_num, column=4).value),
                          url=str(sheet.cell(row=row_num, column=6).value),
                          abstract=str(sheet.cell(row=row_num, column=7).value),
                          citations=sheet.cell(row=row_num, column=8).value,
                          references=sheet.cell(row=row_num, column=9).value)
        result.append(paper)
    return result
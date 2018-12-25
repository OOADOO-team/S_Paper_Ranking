from openpyxl import load_workbook
import bean.Paper as p
import re
import rank as r


# ================================================================
def get_infomation(keyword,alpha):
    """
        通过获取用户输入于界面的keyword,搜索数据库中author和title是否有吻合的关键词
        如果有吻合的关键词，则利用PaperBean构造出paper
        将paper加入result中，最后返回result list
        支持模糊搜索

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
            paper = p.PaperBean(number=i,
                             title=str(sheet.cell(row=i+1, column=2).value),
                             authors=str(sheet.cell(row=i+1, column=3).value),
                            published_in=str(sheet.cell(row=i+1, column=4).value),
                             url=str(sheet.cell(row=i+1, column=5).value),
                             abstract=str(sheet.cell(row=i+1, column=6).value),
                            citations_name=sheet.cell(row=i+1, column=7).value,
                            citations_url=sheet.cell(row=i + 1, column=8).value,
                             references_name=sheet.cell(row=i+1, column=9).value,
                            reference_url = sheet.cell(row=i + 1, column=10).value,
                            citation_number = sheet.cell(row=i + 1, column=11).value
                              )
            result.append(paper)
        result = r.rank_simple(result,alpha)
        length = len(result)
        final_result = zip(range(1,length+1),result)

    return final_result
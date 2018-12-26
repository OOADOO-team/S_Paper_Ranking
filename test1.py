import re
a = "Statistical methods for meta-analysis http://xueshu.baidu.com/usercenter/paper/show?paperid=746363d4a61cd593cbb3b4e915f450f84"
index_ = a.index("http:")
name = a[:index_]
url = a[index_:]
dict = {}
dict.update({name:url})
b = "Model-driven data acquisition in sensor networks http://xueshu.baidu.com/usercenter/paper/show?paperid=7730a14c1780893cd4025fdd3bc06ea9d"
index_ = b.index("http:")
name = b[:index_]
url = b[index_:]
dict.update({name:url})
# # print(dict)
# print(a[0:-1])
dict = str(dict)[1:-1]
# print(dict)
a= dict.split(",")
print(a)
# temp = ""
# for i in text:
#     temp += i
# print(temp)
#
c = ["a","b","c"]
d = [1,3,3]
e=zip(c,d)
print(list(e))
for item in e:
    print(item[0],item[1])
# print(10/79.258 * 1.5)
#
# myList = [('dungeon',7),('winterfell',4),('bran',9),('meelo',6)]
# final_result = zip(myList,range(1,5))
# final_result = dict(final_result)
# print(final_result)
# a = "approaches".upper()
# b = "Successful approaches in the TREC video retrieval evaluations ".upper()
# print(re.search(a,b))

# for item in final_result:
#     print(item[0],item[1])
# _list = sorted(myList, key=lambda x:x[1])
# print(_list)
# return_list = [item[0] for item in _list]
# print(return_list)
a = ""
print(a is "")
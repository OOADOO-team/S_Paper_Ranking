








# 获取 模糊搜索的结果
#存储 部分补一下


#提供 搜索总数 num 和 详细的 get dict
#get [0] -[num-1] 存详细信息 dict 存 dict 0-（num-1） 都是 dict
from builtins import *

get=dict()#给每个论文信息
cite_tol=100#总被引用量

#获取拉条值
cite=1#被引用量占比



def rank(cite,cite_tol,get,num):
    rank=dict()
    end_result=dict()
    for i in range(num):
        rank[i]=get[i]["cite"]/cite_tol*cite/100+get[i]["publish"]*(1-cite/100)
    rank=sorted(rank.items(), key=lambda d: d[1], reverse=True)

    for i in range(1,num+1):
        end_result[i]=get[rank[i-1][0]]
    return end_result
#返回 排序 以及 dict 的数据


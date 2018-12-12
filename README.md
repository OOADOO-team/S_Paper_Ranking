# S_Paper_Ranking
SUSTech CSE 2018 fall OOAD project  

Team Member: 宁文韬 林恺 叶梓元 卢致睿 韦青茂
## Updates:
* 0.0.1 将架构更改为mvc(mtv)架构，比如:![structrue](https://images2015.cnblogs.com/blog/877318/201611/877318-20161120225842607-1712687818.png)  
        Projet/
            __init__.py
            static/
            templates/
                home/
                control_panel/
            views/
                __init__.py
                home.py
                control_panel.py
                admin.py
            models.py

## 如何在pycharm中连接github

* 安装git和在pycharm中绑定github账号：https://www.cnblogs.com/zhaoyingjie/p/6266011.html
* 在pycharm中打开该仓库 ![help](https://github.com/TsingWei/S_Paper_Ranking/blob/master/static/img/help.png)

## 本地版本管理，从远程仓库更新 和 上传到仓库

### 本地版本管理： 略
### 对远程仓库的更新
两种方式
* （建议）新的pull request，团队讨论确认后merge。
* （也可以）直接push。有可能会覆盖掉别人修改的东西。所以使用这种方式的时候要确认你本地代码和仓库中最新的一致。也就是在push之前备份好你做的updates然后pull再把updates加进来然后push

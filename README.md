# S_Paper_Ranking
SUSTech CSE 2018 fall OOAD project  
Github: <https://github.com/OOADOO-team/S_Paper_Ranking>  
Team Member: 宁文韬 林恺 叶梓元 卢致睿 韦青茂
## Updates:
### 1.0 完成(数据库已关闭)
#### 最终效果展示
##### 首页
![首页图片](https://github.com/OOADOO-team/S_Paper_Ranking/blob/master/static/img/nindex.png)
##### 搜索结果页
![搜索页](https://github.com/OOADOO-team/S_Paper_Ranking/blob/master/static/img/nresults.png)
##### 论文详情页
![论文详情页](https://github.com/OOADOO-team/S_Paper_Ranking/blob/master/static/img/ndetails.png)
#### 概述

##### 人员分工:
* 后端:
   * 打分排序算法: 叶梓元 林恺
   * 数据库: 韦青茂 叶梓元
   * 论文爬虫: 卢致睿
* 前端: 韦青茂 宁文韬
* 项目管理: 韦青茂
##### 项目结构:
        Project/
            view.py  // 程序主入口
            bean/   //实体类
            dao/    //数据库访问类
            static/  // 静态资源
                img/
                css/
                js/
                ...
            templates/  // Flask-jinja2模板
                index.html
                results.html
                ...
##### 工具:
* IDE: Pycharm (Python36/37)
* 版本管理: Git & Github
* 应用框架: Flask
* 服务器: Nginx(不包含)
* 前端框架: Bootstrap4
* 前端UI套件: Material Bootstrap Design
* 数据库: MySQL+SQLAlchemy
##### 需要的Python第三方模块
* Flask
* Flask-Bootstrap
* Flask-Bootstrap4
* mysql-connector-python
* SQLalchemy
### 0.0.3 完成details页面
![details](https://github.com/OOADOO-team/S_Paper_Ranking/blob/master/static/img/details.png)
### 0.0.2 更改bean层的类方法getter和setter，将其修饰为property
外部调用getter和setter时不再需要使用paper.getXX()和paper.setXX(),直接使用属性名即可  
> print(paper.title)  
> [Out]'Title'
>
> paper.title = 'IMP'  
> print(paper.title)  
> [Out]'IMP'
### 0.0.1 将架构更改为mvc(mtv)架构，比如:![structrue](https://images2015.cnblogs.com/blog/877318/201611/877318-20161120225842607-1712687818.png)  
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

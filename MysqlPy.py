# from pymysql import connect
from bean.Paper import PaperBean
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

localhost = "10.21.92.180"

engine = create_engine("mysql+mysqlconnector://user:user@10.21.92.180:3306/sys", echo=True)

metadata = MetaData(engine)

PaperTable = Table('paper', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('title', String(1000)),
                   Column('authors', String(100)),
                   Column('published_in', TEXT),
                   Column('url', TEXT),
                   Column('abstract', TEXT),
                   Column('citations_number', Integer),
                   Column('citations_name', TEXT),
                   Column('citations_url', TEXT),
                   Column('references_name', TEXT),
                   Column('references_url', TEXT),
                   )

Base = declarative_base()


class Paper(Base):
    __tablename__ = 'paper'
    id = Column(Integer, primary_key=True)
    title = Column(String(1000))
    authors = Column(String(100))
    published_in = Column(TEXT)
    url = Column(TEXT)
    abstract = Column(TEXT)
    citations_number = Column(Integer)
    citations_name = Column(TEXT)
    citations_url = Column(TEXT)
    references_name = Column(TEXT)
    references_url = Column(TEXT)


metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)


# 插入一条
def insert_DB(paper=PaperBean()):
    session = DBSession()
    # 创建新User对象: id自增
    if len(paper.title)<400 and len(paper.authors)<99 :
        new_paper = Paper(
            title=paper.title,
            authors=paper.authors,
            published_in=paper.published_in,
            url=paper.url,
            abstract=paper.abstract,
            citations_number=paper.citations_number,
            citations_name=str(paper.citations_name)[1:-1],
            citations_url=str(paper.citations_url)[1:-1],
            references_name=str(paper.references_name)[1:-1],
            references_url=str(paper.references_url)[1:-1]
        )
        # 添加到session:
        session.add(new_paper)
        # 提交即保存到数据库:
        session.commit()
        # 关闭session:
        session.close()


def read_DB(keyword):
    session = DBSession()
    keyword = '%'+keyword+'%'
    ret = list()
    ret = session.query(Paper).filter(or_(Paper.title.like(keyword),Paper.authors.like(keyword))).all()

    return ret


conn = engine.connect()
print(conn)

print('title' in metadata.tables)

if __name__ == '__main__':
    p1 = PaperBean(number=1, title="paper1", authors='Wentao1', published_in='Sustech1', url='localhost',
                   abstract="hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh",
                   citations_name=[1, 2, 3], citations_url=[4, 5, 6], references_name=[7, 8, 9],
                   references_url=[9, 8, 7],
                   citations_number=5)
    # insert_DB(p1)

    for p in read_DB('carp'):
        print(p.title,p.id)

# 打开数据库连接
# db = connect(host=localhost, port=3306, user='user', passwd='user', db='sys')

# 使用cursor()方法获取操作游标
# cursor = db.cursor()


# def insert_DB(pa):
#     sql = "INSERT INTO paper(ID, title, authors, published_in, \
#     url, abstract, citations_name, citations_url,  references_name,\
#     references_url, citations_number)\
#              VALUES (%d,\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',%d)" % \
#           (pa.number,
#            pa.title,
#            pa.authors,
#            pa.published_in,
#            pa.url,
#            pa.abstract,
#            str(pa.citations_name)[1:-1],
#            str(pa.citations_url)[1:-1],
#            str(pa.references_name)[1:-1],
#            str(pa.references_url)[1:-1],
#            pa.citations_number)
#     try:
#         # 执行sql语句
#         cursor.execute(sql)
#         # 提交到数据库执行
#         db.commit()
#
#     except Exception as e:
#         print(e)
#     #     # 如果发生错误则回滚
#         db.rollback()
#
#     # 关闭数据库连接
#     db.close()


# def read_DB(keyword):
#     sql = " SELECT * FROM paper WHERE title LIKE '%{}%' or '%{}' or '{}%' OR authors LIKE '%{}%' or '%{}' or '{}%'".\
#         format(keyword, keyword, keyword, keyword, keyword, keyword)
#
#     try:
#         # 执行SQL语句
#         cursor.execute(sql)
#         # 获取所有记录列表
#         result_list = []
#         results_DB = cursor.fetchall()
#         for row in results_DB:
#             number = row[0]
#             title = row[1]
#             authors = row[2]
#             published_in = row[3]
#             url = row[4]
#             abstract = row[5]
#             citations_name = row[6]
#             citations_url = row[7]
#             references_name = row[8]
#             references_url = row[9]
#             citations_number = row[10]
#             result_list.append(PaperBean(number=number,
#                                            title=title,
#                                            authors=authors,
#                                            published_in=published_in,
#                                            url=url,
#                                            abstract=abstract,
#                                            citations_name=citations_name,
#                                            citations_url=citations_url,
#                                            references_name=references_name,
#                                            reference_url=references_url,
#                                            citation_number=citations_number))
#         return result_list
#     except Exception as e:
#         print(e)


# if __name__ == '__main__':
#     p1 = PaperBean(number=1, title="paper1", authors='Wentao1', published_in='Sustech1', url='localhost',
#                    abstract="hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh",
#                    citations_name=[1, 2, 3], citations_url=[4, 5, 6], references_name=[7, 8, 9],
#                    references_url=[9, 8, 7],
#                    citations_number=5)
#     insert_DB(p1)

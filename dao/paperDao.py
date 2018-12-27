# from pymysql import connect
from bean.Paper import PaperBean
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

localhost = "10.21.92.180"

engine = create_engine("mysql+mysqlconnector://user:user@10.21.92.180:3306/sys", echo=False)

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
    ret = list()
    if keyword:
        keyword = '%'+keyword+'%'
        ret = session.query(Paper).filter(or_(Paper.title.like(keyword),Paper.authors.like(keyword))).all()
    else:
        ret = session.query(Paper).all()
    result = []
    for item in ret:
        new_paper = Paper(
            title=item.title,
            authors=item.authors,
            published_in=item.published_in,
            url=item.url,
            abstract=item.abstract,
            citations_number=item.citations_number,
            citations_name=item.citations_name.split("', '"),
            citations_url=item.citations_url.replace("'", "").replace(",", "").replace("\\n", "").split(),
            references_name=item.references_name.split("', '"),
            references_url=item.references_url.replace("'", "").replace(",", "").replace("\\n", "").split()
        )
        result.append(new_paper)
    return result

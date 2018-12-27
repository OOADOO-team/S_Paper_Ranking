from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from bean.publishedBean import *

localhost = "10.21.92.180"

engine = create_engine("mysql+mysqlconnector://user:user@10.21.92.180:3306/sys", echo=True)

metadata = MetaData(engine)


Base = declarative_base()


class Published(Base):
    __tablename__ = 'published'
    id = Column(Integer, primary_key=True)
    published_name = Column(String(1000))
    IF_value = Column(FLOAT)


metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)

# session = DBSession()
# 插入一条
def insert_DB(pb=publishedBean()):
    session = DBSession()
    # 创建新User对象: id自增

    new_p = Published(
        published_name=pb.published_name,
        IF_value=pb.IF_value
    )
    # 添加到session:
    session.add(new_p)
    # 提交即保存到数据库:
    session.commit()
    # # 关闭session:
    session.close()


def read_DB(keyword):
    session = DBSession()
    keyword = '%'+keyword+'%'
    try:
        ret = session.query(Published).filter(Published.published_name.like(keyword)).one()
    except:
        return None

    # IF_value=ret.IF_value

    return ret.IF_value



if __name__ =="__main__":
    pass
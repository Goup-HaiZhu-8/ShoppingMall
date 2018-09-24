from  app import db
from sqlalchemy  import Table,create_engine,MetaData

class Customer(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    user_name = db.Column(db.String(64),index=True,unique=True)
    password = db.Column(db.String(64))
    email = db.Column(db.Unicode(128),index=True,unique=True)
    nickname= db.Column(db.String(64),index=True,unique=True)

    # 打印格式
    def __repr__(self):
          return '<User %r>'%(self.nickname)



#数据库表还没创建的情况下，需要创建表
# class Goods(db.Model):
#     __tablename__ = 'Goods'
#
#     gid = db.Column(db.Integer,primary_key=True,nullable=False)
#     gname = db.Column(db.String(30))
#     screen_size = db.Column(db.Float(3,2))
#     camera = db.Column(db.Integer)
#     ROM = db.Column(db.Integer)
#     RAM = db.Column(db.Integer)
#     price = db.Column(db.Float(7,2))
#     color = db.Column(db.String(45))

    # def __init__(self,gname,screen_size,camera,ROM,RAM,price,color):
    #     self.gname = gname
    #     self.screen_size = screen_size
    #     self.camera = camera
    #     self.ROM = ROM
    #     self.RAM = RAM
    #     self.price = price
    #     self.color = color
#

    # def __repr__(self):
    #     return '<Good %r>'%(self.gname)

#已经存在的情况下，直接导入
class Goods():
    def __init__(self):
        self._uri = 'mysql+pymysql://root:1357928tyl@localhost:3306/HUAWEI'
        self.engine = create_engine(self._uri, echo=False)  #创建引擎
        self.metadata = MetaData(self.engine)
        self.apply_table = Table('Goods', self.metadata, autoload=True)

    def __repr__(self):
        return '<Good>'

# class  shopCar(db.Model):
#     id = db.Column(db.Integer,primary_key=True,nullable=False)
#     img_url = db.Column(db.String(100))




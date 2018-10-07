from  website_flask.app import db
from sqlalchemy  import Table,create_engine,MetaData


# class Shoppingcar():
#      __tablename__ = 'Shoppingcar'
#      __table_args__ = {"useexisting": True}
#
#      _url = 'mysql+pymysql://root:1357928tyl@localhost:3306/HUAWEI'
#      engine = create_engine(_url,echo=False)
#      metadata = MetaData(engine)
#      apply_table = Table('Shoppingcar',metadata,autoload=True)
#
#      def __repr__(self):
#         return '<ShoppigCar>'

cus_shop = db.Table('cus_shop',
                       db.Column('c_id',db.Integer,db.ForeignKey('customer.id')),
                       db.Column('s_id',db.Integer,db.ForeignKey('shoppingcar.id')),
                       )


class Customer(db.Model):
    # __table_args__ = {"useexisting": True}
    # def __init__(self):
    __tablename__ = 'customer'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_name = db.Column(db.String(64),index=True,unique=True)
    password = db.Column(db.String(64))
    email = db.Column(db.Unicode(128),index=True,unique=True)
    nickname= db.Column(db.String(64),index=True,unique=True)
    shopCar = db.relationship(
        'Shoppingcar',
        secondary=cus_shop,
        backref=db.backref('customer',lazy='dynamic')
    )


    # 打印格式
    def __repr__(self):
          return '<User %r>'%(self.nickname)


# 已经存在的情况下，直接导入
# class Goods():
#     __table_args__ = {"useexisting": True}
#
#     def __init__(self):
#         self._uri = 'mysql+pymysql://root:1357928tyl@localhost:3306/HUAWEI'
#         self.engine = create_engine(self._uri, echo=False)  # 创建引擎
#         self.metadata = MetaData(self.engine)
#         self.apply_table = Table('Goods', self.metadata, autoload=True)
#
#     def __repr__(self):
#         return '<Good>'


class Shoppingcar(db.Model):
    __tablename__='shoppingcar'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    uid = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    goods_id = db.Column(db.Integer,db.ForeignKey('goods.gid'))


#数据库表还没创建的情况下，需要创建表
class Goods(db.Model):
    __tablename__ = 'goods'

    gid = db.Column(db.Integer,primary_key=True,nullable=False)
    gname = db.Column(db.String(30))
    screen_size = db.Column(db.Float(3,2))
    battery = db.Column(db.Integer)
    camera = db.Column(db.Integer)
    ROM = db.Column(db.Integer)
    RAM = db.Column(db.Integer)
    price = db.Column(db.Float(7,2))
    color = db.Column(db.String(45))
    storage = db.Column(db.Integer)
    shop_car = db.relationship(
        'Shoppingcar',
        backref='good',
        lazy='dynamic'
    )

    def __repr__(self):
        return '<Good %r>'%(self.gname)

# db.create_all()
from  app import db

class Customer(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    user_name = db.Column(db.String(64),index=True,unique=True)
    password = db.Column(db.String(64))
    email = db.Column(db.Unicode(128),index=True,unique=True)
    nickname= db.Column(db.String(64),index=True,unique=True)

    # 打印格式
    def __repr__(self):
          return '<User %r>'%(self.nickname)



class Goods(db.Model):
    __tablename__ = 'Goods'

    gid = db.Column(db.Integer,primary_key=True,nullable=False)
    gname = db.Column(db.String(30))
    screen_size = db.Column(db.Float(3,2))
    camera = db.Column(db.Integer)
    ROM = db.Column(db.Integer)
    RAM = db.Column(db.Integer)
    price = db.Column(db.Float(7,2))
    color = db.Column(db.String(45))

    # def __init__(self,gname,screen_size,camera,ROM,RAM,price,color):
    #     self.gname = gname
    #     self.screen_size = screen_size
    #     self.camera = camera
    #     self.ROM = ROM
    #     self.RAM = RAM
    #     self.price = price
    #     self.color = color
#

    def __repr__(self):
        return '<Good %r>'%(self.gname)


class  shopCar(db.Model):
    id = db.Column(db.Integer,primary_key=True,nullable=False)
    img_url = db.Column(db.String)




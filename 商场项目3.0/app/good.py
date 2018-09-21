from sqlalchemy import MetaData,create_engine,Table
from sqlalchemy.ext.automap import  automap_base
from sqlalchemy.orm import sessionmaker
# from sqlalchemy import *
# from sqlalchemy.databases.mysql import *


uri = 'mysql+pymysql://root:123456@localhost:3306/HUAWEI'
engine = create_engine(uri,echo=False)

metadata = MetaData(engine)

apply_info = Table('Goods',metadata,autoload=True)
keys = apply_info.columns.keys()

Session = sessionmaker(bind=engine)

session = Session()

rows = session.query(apply_info).first()


# metadata.reflect(bind=engine)
#
# metadata.tables.keys()
#
# apply_info = metadata.tables['apply_info']




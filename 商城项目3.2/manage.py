'''
此模块用于数据库的迁移
'''

from flask_script import Manager,Server
from flask_migrate import MigrateCommand,Migrate

from  website_flask.app.models import Customer,Shoppingcar,Goods
from  website_flask.app  import app
from  website_flask.app import db

migrate = Migrate(app,db)

manager = Manager(app)
manager.add_command('server',Server())
manager.add_command('db',MigrateCommand)

@manager.shell
def  make_shell_context():
    return dict(app=app,db=db,Customer=Customer,shoppingcar=Shoppingcar,Goods=Goods)

if  __name__ == '__main__' :
     manager.run()
from flask import session
from flask import sessions
from flask import request,Response
from  flask.ext.principal  import identity_loaded,Principal,Permission,RoleNeed
#需要下载扩展Flask-Principal
import app
from  celery  import  Celery

@identity_loaded.connect_via(app)
def on_identity_loaded(sender,identity):
    pass

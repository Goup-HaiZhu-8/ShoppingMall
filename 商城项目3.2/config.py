import os
from flask import Config

#密钥
CSRF_ENABLED = True
SECRET_KEY = os.urandom(25)

#连接mysql数据库
class SQLConfig(Config):
  SQLALCHEMY_DATABASE_URI =  'mysql+pymysql://root:1357928tyl@localhost:3306/HUAWEI'
  SQLALCHEMY_TRACK_MODIFICATIONS = True
  SQLALCHEMY_COMMIT_TEARDOWN = True
  SQLALCHEMY_COMMIT_ON_TEARDOWN = True


#flask_cache配置项
class ProConfig(Config):
    # CACHE_TYPE = 'redis'
    # CACHE_REDIS_HOST = 'localhost'
    # CACHE_REDIS_PORT = '6379'
    # CACHE_REDSI_PASSWORD = ''
    # CACHE_REDIS_DB = '0'
    CACHE_TYPE = 'simple'

#链接redis数据库
config_redis={
    'CACHE_TYPE':'redis',
    'CACHE_REDIS_HOST':'127.0.0.1',
    'CACHE_REDIS_PORT':'6379',
    'CACHE_REDIS_DB':'',
    'CACHE_REDIS_PASSWORD':''
}


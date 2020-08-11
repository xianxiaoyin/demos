# coding:utf-8

class Config(object):
    """配置参数"""
    # 设置连接数据库的URL
    host = "127.0.0.1"
    port = 3306
    user = 'root'
    password = r'123456'
    database = 'spike'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s:%s/%s' % (user, password, host, port, database)

    # 设置sqlalchemy自动更跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 查询时会显示原始SQL语句
    SQLALCHEMY_ECHO = True

    # 禁止自动提交数据处理
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

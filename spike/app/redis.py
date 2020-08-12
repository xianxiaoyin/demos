# coding:utf-8
import redis
from app import app
from app.config  import Config

config = Config()

class Redis(object):
    """
    redis数据库操作
    """

    @staticmethod
    def _get_r():
        host = config.REDIS_HOST
        port=config.REDIS_PORT
        db=config.REDIS_DB
        r = redis.StrictRedis(host, port,db)
        return r

    @classmethod
    def write(cls, key, value, expire=None):
        """
        写入键值对
        """
        # 判断是否有过期时间，没有就设置默认值
        if expire:
            expire_in_seconds = expire
        else:
            expire_in_seconds = config.REDIS_EXPIRE
        r = cls._get_r()
        r.set(key, value, ex=expire_in_seconds)

    @classmethod
    def read(cls, key):
        """
        读取键值对内容
        """
        r = cls._get_r()
        value = r.get(key)
        return value.decode('utf-8') if value else value

    @classmethod
    def hset(cls, name, key, value):
        """
        写入hash表
        """
        r = cls._get_r()
        r.hset(name, key, value)


    @classmethod
    def expire(cls, name, expire=None):
        """
        设置过期时间
        """
        if expire:
            expire_in_seconds = expire
        else:
            expire_in_seconds = config.REDIS_EXPIRE
        r = cls._get_r()
        r.expire(name, expire_in_seconds)
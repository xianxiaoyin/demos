'''
Author: xianxiaoyin
LastEditors: xianxiaoyin
Descripttion: 
Date: 2020-12-19 12:28:05
LastEditTime: 2020-12-19 14:15:48
'''
import pymysql

pymysql.version_info = (1, 4, 0, 'final', 0)  #指定版本，这句才是关键
pymysql.install_as_MySQLdb()
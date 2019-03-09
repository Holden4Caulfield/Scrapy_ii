# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql.cursors
class TexPipeline(object):
    def __init__(self):
        self.limit=15
    def process_item(self,item,spider):
        if item['cont']:
            if len(item['cont'])>self.limit:
                item['cont']=item['cont'][0:self.limit].rstrip()+'...'
            return item
        else:
            return DropItem('miss texe')
    pass

class SavePipline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='localhost',  # 数据库地址
            port=3306,  # 数据库端口
            db='scrapymysql',  # 数据库名
            user='root',  # 数据库用户名
            passwd='123456',  # 数据库密码
            charset='utf8',  # 编码方式
            use_unicode=True)
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        self.cursor.execute(
            """insert into mingyan(tag, cont)
            value (%s, %s)""",  # 纯属python操作mysql知识，不熟悉请恶补
            (item['tag'],  # item里面定义的字段和表字段对应
             item['cont'],))
        # 提交sql语句
        self.connect.commit()
        return item  # 必须实现返回

#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : export_data.py
# Create date : 2019-08-21 20:34
# Modified date : 2019-08-21 20:45
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

import pymongo

class LawSpider:
    def __init__(self):
        conn = pymongo.MongoClient()
        self.db = conn['lawsuit']['case']
        self.db_crime = conn['lawsuit']['crime']

    '''导出判决数据'''
    def export_data(self):
        i = 0
        for item in self.db.find({'cate':'刑事'}).limit(500):
            i += 1
            title = item['title']
            pubtime = item['pub_time']
            cate = item['cate']
            content = '\n'.join(item['content'])
            f = open('corpus_lawsuit/%s.txt'%i, 'w+')
            f.write('category:' + cate + '\n')
            f.write('title:' + title +'\n')
            f.write('publictime:'+ pubtime + '\n')
            f.write('content:' + content + '\n')
            f.close()

        for item in self.db.find({'cate':'民事'}).limit(500):
            i += 1
            title = item['title']
            pubtime = item['pub_time']
            cate = item['cate']
            content = '\n'.join(item['content'])
            f = open('corpus_lawsuit/%s.txt'%i, 'w+')
            f.write('category:' + cate + '\n')
            f.write('title:' + title +'\n')
            f.write('publictime:'+ pubtime + '\n')
            f.write('content:' + content + '\n')
            f.close()
        return

    '''导出犯罪数据'''
    def export_data_crime(self):
        i = 0
        for item in self.db_crime.find().limit(1000):
            i += 1
            title = item['title']
            cate = item['category']
            content = '\n'.join(item['content'])
            f = open('corpus_crime/%s.txt' % i, 'w+')
            f.write('category:' + cate + '\n')
            f.write('title:' + title + '\n')
            f.write('content:' + content + '\n')
            f.close()
        return

def test():
    handler = LawSpider()
    handler.export_data_crime()

#test()

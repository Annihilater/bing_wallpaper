#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/11/22 08:45
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : spider.py
import os

import requests
from pyquery import PyQuery as pq


class Spider:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end
        self.base_url = 'https://bing.ioliu.cn/'
        self.url = None
        self.dir = 'data/'
        self.file = None
        self.path = None
        self.img = None
        self.page = self.start - 1
        self.num = 0

    def run(self):
        for i in range(self.start, self.end + 1):
            self.page += 1
            self.num = 0

            self.url = self.base_url + f'?p={i}'
            r = requests.get(self.url)

            doc = pq(r.text)
            items = doc.find('.item')
            for item in items.items():
                self.img = item.find('div img').attr('src')
                self.file = self.img.split('/')[-1]
                self.path = self.dir + self.file
                self.num += 1
                print(f'{self.page}页  {self.num}个  {self.img}')
                if not os.path.exists(self.path):
                    self.save_img()
                    print('保存新图')
                else:
                    print('已存在')

    def save_img(self) -> None:
        """
        保存一张图片
        :return:
        """
        path = self.dir + self.file
        r = requests.get(self.img)
        with open(path, mode='xb') as f:
            f.write(r.content)


if __name__ == '__main__':
    start = 97
    end = 113
    spider = Spider(start, end)
    spider.run()

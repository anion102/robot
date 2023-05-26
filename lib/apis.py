# encoding=utf-8
import json

import yaml
import sys
import datetime
from lib.base_request import req_get, req_post


class Apis:
    def __init__(self, host):
        self.host = host

    def user_register(self, user_name, tel, pwd):
        try:
            request_data = {'user_name': user_name, 'user_tel': tel, 'user_pwd': pwd}
            url = self.host + sys._getframe().f_code.co_name
            print(url)
            # result = req_post(url, request_data)
            # return result
            user_id = 123
            return user_id
        except Exception as ex:
            print(ex)
            return ex

    def get_user_info(self, user_id):
        try:
            param = {'user_id':user_id}
            url = self.host + sys._getframe().f_code.co_name
            # print(url)
            # result = req_get(url, param)
            result = {'user_id': 1002, 'user_name': 'Jane', 'user_tel': 18605500300, 'sex': 'W'}
            return result
        except Exception as ex:
            print(ex)
            return ex

    def query_order_info(self, order_id):
        try:
            param = {'order_id': order_id}
            url = self.host + sys._getframe().f_code.co_name
            print(url)
            result = req_post(url, param)
            return result
            return 1
        except Exception as ex:
            print(ex)
            return ex

    def query_orders_by_user(self, user_id, time=datetime.datetime.now().strftime('%Y-%m-%d')):
        try:
            param = {'user_id': user_id, 'period': time}
            url = self.host + sys._getframe().f_code.co_name
            # print(url)
            result = req_post(url, param)
            return result
        except Exception as ex:
            print(ex)
            return ex

    def books(self, book_id=None):
        try:
            if book_id:
                url = self.host + sys._getframe().f_code.co_name + '/' +str(book_id)
            else:
                url = self.host + sys._getframe().f_code.co_name
            print(url)
            result = req_get(url)
            return result
        except Exception as ex:
            print(ex)
            return ex

    def orders(self, book_id, name):
        try:
            param = {'bookId': book_id, 'customerName': name}
            url = self.host + sys._getframe().f_code.co_name
            print(url)
            result = req_post(url, param)
            return result
        except Exception as ex:
            print(ex)
            return ex

api = Apis("https://simple-books-api.glitch.me/")
books = api.orders(2,'Jenny')
print(json.loads(books))

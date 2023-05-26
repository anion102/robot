import json

from robot.api.logger import info, debug, trace, console
from lib.apis import Apis
from lib.mysql import Mysql
import os
import yaml


class ApiLibrary:
    ROBOT_LIBRARY_SCOPE = 'SUITE'  # GLOBAL  SUITE  CASE： init once in the certain scope

    def __init__(self):

        cur_path = os.path.dirname(os.path.realpath(__file__))
        self.yaml_path = os.path.join(cur_path, "./data.yaml")
        self._api: Apis = None
        self._mysql: Mysql = None
        self.yaml = None
        self.user = None
        self.host = None

    def init_api(self):
        self._api = Apis(self.host)

    def connect_to_mysql(self, mysql_tag, db):
        host = self.yaml[mysql_tag]['host']
        port = self.yaml[mysql_tag]['port']
        user = self.yaml[mysql_tag]['user']
        pwd = self.yaml[mysql_tag]['password']
        print(host)
        self._mysql = Mysql(host, port, user, pwd, db)

    def close_dbconnection(self):
        self._mysql.close()

    def yaml_parse(self):
        self.yaml = self.load_data()

    def init_items_data(self, user_tag, host_tag):
        self.yaml_parse()
        self.init_host(host_tag)
        self.init_user(user_tag)
        return True

    def init_user(self, user_tag):
        self.user = self.yaml[user_tag]
        return True

    def init_host(self, host_tag):
        self.host = self.yaml[host_tag]
        return True

    def get_host(self):
        return self.host

    def get_user_data(self):
        return self.user

    def load_data(self):
        with open(self.yaml_path, 'r', encoding='utf-8') as f:
            try:
                data = yaml.load(f, Loader=yaml.FullLoader)
                info(f'yaml data: {data}')
                return data
            except yaml.YAMLError as e:
                info(f'{e}')

    """server apis functions"""

    def register(self):
        # debug(f'_api: {self._api}')
        result = self._api.user_register(self.user['name'], self.user['tel'], self.user['pwd'])
        return result

    def get_user_information(self, user_tag=None):
        if user_tag is None:
            user_id = self.user['user_id']
        else:
            user_id = self.yaml[user_tag]['user_id']
        user_info = self._api.get_user_info(user_id)
        return user_info

    def get_books(self, book_id=None):
        book_info = self._api.books(book_id)
        return json.loads(book_info)

    """DB operation functions"""

    def query_user(self, user_id):
        sql = "select * from T_users where user_id=%d" % user_id
        re = self._mysql.query_execution(sql)
        return re[0]


# li = ApiLibrary()
# li.yaml_parse()
# li.connect_to_mysql('mysql', 'user')
# r = li.query_user(1005)
# print(r)
# li.close_dbconnection()

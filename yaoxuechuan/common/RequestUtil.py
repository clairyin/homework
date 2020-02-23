from common.base import BaseObj
import requests
from common.func import dict_to_json
from common.func import print_json
from common.func import json_to_dict
import json
class RequsestUtil(BaseObj):
    def __init__(self):
        super().__init__()
        self.headers =  {'Content-Type': 'application/json'}

    def send_request(self):
        self.url = self.compose_url()
        json_body = dict_to_json(self.body) if self.body else None
        print(json_body)
        resp = self.__send_request(data=json_body)
        print('=======================打印反序列化结果dict=======================')
        print(resp)
        self.resp = json_to_dict(resp)
        print('=======================把dict序列化为对象属性=====================')
        print(self.resp)
        return self

    def compose_url(self):
        return self.host+self.uri
    def update_headers(self,add_headers={}):
        self.headers.update(add_headers)

    #组装参数url和headers,data放在send调用时传
    def __send_request(self,data=None):
        common_condition = dict(url=self.url,headers=self.headers)
        print(self.method)
        print('==========================开始发送请求================================')
        r = None
        if self.method == 'post':
            r = requests.post(**common_condition,data=data)
        if self.method == 'get':
            r = requests.get(**common_condition,params=data)
        print('=========================开始判断返回结果==============================')

        print(r.status_code)
        if str(r.status_code) == '200':
            response = r.json()
            return response
        else:
            print('返回接口为None')
            return None


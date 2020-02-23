
from common.RequestUtil import RequsestUtil
from ordermanage.auth import auth_token
class BaseOrder(RequsestUtil):

    def __init__(self):

        self.host = 'http://144.34.200.237:8080'
        print('===================开始获取tokens===============================')
        super().__init__()
        self.set_token()
    #把鉴权的字符串父子给auth
    def  set_token(self):
        self.update_headers(dict(Authorization=auth_token))
        print(self.headers)
        print("====================获取tokens结束==============================")
        return self


if __name__ == '__main__':
    r = BaseOrder().set_token()
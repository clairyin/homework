from ordermanage.BaseOrder import BaseOrder

class CoupConrollerList(BaseOrder):
    #传入**kargs的值，会被base.py的update_value绑定
    def __init__(self,**kargs):
        super().__init__()
        self.uri = '/coupon/list'
        self.method = 'get'
        self.body = self.Body(**kargs)

    class Body:
        def __init__(self,**kwargs):
            super().__init__()
            self.name = 'aaa'
            self.type = 1
            self.pageSize = 1
            self.pageNum = 1


CoupConrollerList().send_request()






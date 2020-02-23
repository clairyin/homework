
from common.RequestUtil import RequsestUtil

class AdminLogin(RequsestUtil):
    def __init__(self, **kargs):
        super().__init__()
        self.host = 'http://144.34.200.237:8080'
        self.uri = '/admin/login'
        self.method = 'post'
        self.body = self.Body(**kargs)

    class Body:
        def __init__(self,**kargs):
            self.username = 'ceshijiagoushi'
            self.password = '123456'
            super().__init__(**kargs)








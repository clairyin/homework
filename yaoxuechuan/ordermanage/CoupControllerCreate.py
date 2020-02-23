from ordermanage.BaseOrder import BaseOrder



class CoupControllerCreate(BaseOrder):
    def __init__(self,**kargs):
        super().__init__()
        self.uri = '/coupon/create'
        #self.method = 'post'
        self.body = self.Body(**kargs)


    class Body:
        def __init__(self,**kargs):
            super().__init__()
            self.productCategoryRelationList = [self.CategoryRelationList()]
            self.productRelationList = [self.ProductRelationList()]
            self.amount = 0
            self.code = 0
            self.enableTime = "2020-02-18T13:38:49.311Z"
            self.endTime = "2020-02-18T13:38:49.311Z"
            self.id = 0
            self.memberLevel = 0
            self.minPoint = 0
            self.name = 'string'
            self.note = 'string'
            self.perLimit = 0
            self.platform = 0
            self.publishCount = 0
            self.receiveCount =0
            self.startTime = '2020-02-18T13:38:49.311Z'
            self.type = 0
            self.useCount = 0
            self.useType = 0

        class CategoryRelationList:
            def __init__(self):
                super().__init__()
                self.couponId = 0
                self.id = 0
                self.parentCategoryName = 'string'
                self.productCategoryId = 0
                self.productCategoryName = 0

        class ProductRelationList:
            def __init__(self):
                super().__init__()
                self.couponId = 0
                self.id = 0
                self.productId = 0
                self.productName = 'string'
                self.productSn = 'string'

r = CoupControllerCreate().send_request()




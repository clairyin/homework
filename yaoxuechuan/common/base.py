

class BaseObj:
    def __init__(self, *args, **kwargs):
        """origin doc"""
        #self.name ='abc'
        self.update_value(**kwargs)  # 思考这个方法的作用是什么
    #实例化后打印对象时，取__repr__的返回值。使用__dict__先后查到对象的属性、类的属性
    def __repr__(self):
        """我就是str的备胎"""
        return str(self.__dict__)
        # return   str('abc')

    def __enter__(self):
        """使用with语法时候会调用此处"""
        print("{}进入宠物店".format(self.name))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """使用with语法时会调用此处"""
        print("{}走出宠物店".format(self.name))
    #传入字典,把key、value通过setattr方法变为对象的属性值即__dict__中的值
    def update_value(self, **kwargs):
        if kwargs:
            for attribute_name in kwargs.keys():
                setattr(self, attribute_name, kwargs.get(attribute_name))

    def get_value(self, name, default=None):
        """
        获取对象的属性值
        :param name: 属性名
        :param default: 如果没有返回的默认值
        :return:
        """
        value = getattr(self, name, default)
        if value is None:
            return default
        else:
            return value

    def __getattr__(self, attr):
        """实现.符号取值"""
        try:
            return self.__getattribute__(attr)
            # return self.name
        except AttributeError:
            # raise AttributeError(attr)
            return None

    @staticmethod
    def static_func():
        return "静态方法"
    #
    # def clear_value(self):
    #     for k, v in vars(self).items():
    #         setattr(self, k, None)

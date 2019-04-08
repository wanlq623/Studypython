# 请补全以下代码：

class Person:
    def __init__(self,name):
        self.name = name

    def show(self):
        print('大家注意了！')
        print('一个叫“%s”的人来了。' % self.name)




# 子类的继承和定制
class Man(Person):
    def __init__(self):
        Person.__init__(self,name='范罗苏姆')

    def show(self):
        print('大家注意了！')
        print('一个叫“%s”的男人来了。' % self.name)

    def leave(self):
        print('大家注意了！')
        print('那个叫“%s”的男人留下了他的背影。' % self.name)






author1 = Person('吉多')
author1.show()
# author1.leave()  # 补全代码后，运行该行会报错：AttributeError：'Person' object has no attribute 'leave'.
author2 = Man()
author2.show()
author3 = Man()
author3.leave()

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must be 0-100!')

        self._score = value

a = Student()
# 这种写法还是很有问题的啊 _score如果先get 那么实例中还没有这个属性
# print(a.score)
a.score = 10
print(a.score)


# 使用type可以创建类
# 实际上python中class 在解释器处理时也是用type来创建的
# 也就是python这种动态语言的优势 可以动态创建类

def fn(self, name='world'):
    print('Hello %s' % name)


Hello = type('Hello', (object,), dict(hello = fn))

h = Hello()
h.hello()


# metaclass

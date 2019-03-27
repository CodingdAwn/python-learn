
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

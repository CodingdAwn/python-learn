from types import MethodType

class Student(object):

    static_property = 'Static'

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print(self):
        print('Student name is %s, score is %s' % (self.name, self.score))


dAwn_ = Student('dAwn_', 100)
dAwn_.print()

breAk = Student('breAk', 50)
breAk.print()

dAwn_.age = 18
print('dAwn\'s age is %s' % dAwn_.age)
#print('breAk\'s age is %s' % breAk.age)

print(dir(dAwn_))
print('Student class property: %s' % Student.static_property)
print('dAwn_ intance property: %s' % dAwn_.static_property)
print('breAk intance property: %s' % breAk.static_property)

# 这里的操作 会覆盖掉Student中的属性 生成了一个新的属性
dAwn_.static_property = 'Dynamic_modify'
breAk.static_property = 'breAk modify'
print('Student class property: %s' % Student.static_property)
print('dAwn_ intance property: %s' % dAwn_.static_property)
print('breAk intance property: %s' % breAk.static_property)

# 可以看到这里再次使用类的方式修改属性 也无法改变实例的值了
# 所以不应该把这个理解成 c++中的静态函数 静态变量
Student.static_property = 'Static'
print('Student class property: %s' % Student.static_property)
print('dAwn_ intance property: %s' % dAwn_.static_property)
print('breAk intance property: %s' % breAk.static_property)

# 测试绑定函数
def set_age(self, age):
    self.age = age

dAwn_.set_age = MethodType(set_age, dAwn_)

# 这里如果直接将函数设置到instance上是不行的
# 测试绑定后 函数的指针都不一样了 如果不绑定指针都是一样的
#dAwn_.set_age = set_age
print(set_age)
print(dAwn_.set_age)
dAwn_.set_age(30)
print(dAwn_.age)

# 给class绑定函数
def set_score(self, scroe):
    self.score = scroe

Student.set_score = set_score
dAwn_.set_score(100)
print('dAwn\'s score is %s ' % dAwn_.score)
breAk.set_score(99)
print('dAwn\'s score is %s ' % dAwn_.score)
print('breAk\'s score is %s ' % breAk.score)

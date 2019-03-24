

class Student(object):

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
print('breAk\'s age is %s' % breAk.age)

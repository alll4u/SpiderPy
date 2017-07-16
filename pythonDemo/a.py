class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.abc = 'xxx'
    def print_score(self):
        print('%s: %s' % (self.name, self.score))
from Elementary_Sorting import Selection, Insertion, Shell
from random import randint
from datetime import datetime

class sortcompare:
    def __init__(self, N, T):
        self.length = N
        self.a = []
        self.times = T
        self.total = 0

    def timeRandomInput(self, sort_method):
        for i in range(self.times):
            for j in range(self.length):
                self.a.append(randint(1,100))
            self.total += self.time(sort_method)
        return self.total

    def time(self, sort_method):

        time_start = datetime.now()
        if sort_method == 'Selection':
            Selection(self.a)
        if sort_method == 'Insertion':
            Insertion(self.a)
        if sort_method == 'Shell':
            Shell(self.a)

        time_end = datetime.now()
        return ((time_end - time_start).microseconds)/(10**6)


if __name__ == '__main__':
    sc1 = sortcompare(100000, 5)
    time1 = sc1.timeRandomInput('Insertion')
    sc2 = sortcompare(100000, 5)
    time2 = sc2.timeRandomInput('Selection')
    sc3 = sortcompare(100000, 5)
    time3 = sc3.timeRandomInput('Shell')
    print(time3)
    print(time2)
    print(time1)
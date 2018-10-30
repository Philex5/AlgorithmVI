# 蒙特卡洛(Monte Carlo)方法仿真分析渗透判断系统
import numpy as np
import sys
from random import random, randint
sys.path.append('/media/philex/File/Workspace/AlgorithmsVI/Chapter1_Fundamentals')
from Percolation import percolation
from math import sqrt

class percolationstats:
    def __init__(self, n, trials):  # perform trials independent experiments on an n-by-n grid
        if n <= 0 or trials <= 0:
            raise ValueError
        self.N = n
        self.trials = trials
        self.thresholds = []                 # 每一次独立实验的阈值(渗透需开启的格子数）

    def simulation(self):
        for i in range(self.trials):
            print('Processing percolation %s' % i)
            threshold = self.process_percolation()
            self.thresholds.append(threshold)


    def process_percolation(self):
        pl = percolation(self.N)
        threshold = 0
        resultlist = []
        flag = pl.percolates()
        while not flag:
            i = randint(0, self.N-1)
            j = randint(0, self.N-1)
            if (i, j) not in resultlist:
                resultlist.append((i, j))
                pl.open(i, j)
                threshold += 1
            flag = pl.percolates()
        print('ts', threshold)
        return threshold

    def mean(self):  # sample mean of percolation threshold
        return np.mean(self.thresholds)

    def stddev(self):  # sample standard deviation of percolation threshold
        stddev_quantic = 0
        for i in range(self.trials):
            stddev_quantic += (self.thresholds[i] - self.mean())**2

        stddev = sqrt(stddev_quantic/(self.trials-1))
        return stddev

    def confidenceLo(self):  # low endpoint of 95% confidence interval
        return self.mean() - ((1.96*self.stddev()) / sqrt(self.trials))

    def confidenceHi(self):  # high endpoint of 95% confidence interval
        return self.mean() + ((1.96 * self.stddev()) / sqrt(self.trials))


if __name__ == '__main__':
    n = 2
    strials = 10000
    ps = percolationstats(n, strials)
    ps.simulation()
    print('mean', ps.mean() / (n**2))
    print('stddev', ps.stddev())
    print('95% confidence interval[{}, {}]'.format(ps.confidenceLo()/(n**2), ps.confidenceHi()/(n**2)))



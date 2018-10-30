# 渗透系统判断实现

import numpy as np
import sys
sys.path.append('/media/philex/File/Workspace/AlgorithmsVI/Chapter1_Fundamentals')
from Union_find.weighted_quick_union import WeightedQuickUnionUF
from Union_find.quick_find import UF
from random import random
from tkinter import *


class percolation:
    def __init__(self, n):   # ceate n-by-n grid, with all site blocked
        self.grid_state = np.zeros([n, n], dtype=np.int32)   # 初始为0:close 1：open  2：full
        self.grid_link = WeightedQuickUnionUF(n*n+1)
        self.count = 0  # count the number of open site
        self.N = n
        self.ispercolated = self.percolates()

    def open(self, row, col):  # open site(row, col) if it is not open already

        if self.grid_state[row, col] >= 1:
            return

        if self.grid_state[row, col] == 0:
            self.grid_state[row, col] = 1
            self.count += 1

        if row == 0:
            self.grid_link.union(self.xyto1D(row, col), self.N**2)
            self.grid_state[row, col] = 2
            return


        if (row-1 >= 0) and (self.isOpen(row-1, col)):
            self.grid_link.union(self.xyto1D(row, col), self.xyto1D(row-1, col))
            if self.grid_state[row-1, col] == 2:
                self.grid_state[row, col] = 2

        if (col+1 <= 0) and (self.isOpen(row, col-1)):
            self.grid_link.union(self.xyto1D(row, col), self.xyto1D(row, col+1))
            if self.grid_state[row, col+1] == 2:
                self.grid_state[row, col] = 2

        if (row+1<self.N)  and (self.grid_state[row+1, col] >= 1):
            self.grid_link.union(self.xyto1D(row, col), self.xyto1D(row+1, col))
            if self.grid_state[row+1, col] == 2:
               self.grid_state[row, col] = 2

        if (col - 1 >= 0) and (self.isOpen(row, col - 1)):
            self.grid_link.union(self.xyto1D(row, col), self.xyto1D(row, col - 1))
            if self.grid_state[row, col-1] == 2:
                self.grid_state[row, col] = 2

        if self.grid_state[row, col] == 2:
            self.full(row, col)

    def full (self, row, col): # full site after link
        for i in range(self.N):
            for j in range(self.N):
                if self.grid_link.connected(self.xyto1D(row, col), self.xyto1D(i, j)):
                    self.grid_state[i, j] = 2
                    self.grid_link.union(self.xyto1D(i, j), self.N**2)

    def xyto1D(self, row, col):
        return row * self.N + col

    def isOpen(self, row, col):  # is site(row, col) open ?
        return self.grid_state[row, col] >= 1

    def isFull(self, row, col): # is site(row, col) full ?
        return self.grid_link.connected(self.xyto1D(row, col), self.N**2)

    def numberOfOpenSites(self):  # number of open sites
        return self.count

    def percolates(self): # dose the system percolate ?
        flag = False
        for i in range(self.N):
            if self.grid_link.connected(self.N**2, self.xyto1D(self.N-1, i)):
                flag = True
                #print('(%s, %s)' % (self.N-1, i))
                return flag
        return flag

    # 网格可视化
    def grid_visualization(self, startx=10, starty=10, cellwidth=20):
        width = 4 * startx + self.N * cellwidth
        height = 6 * starty + self.N * cellwidth
        colors = ['black', 'white', 'blue']
        root = Tk()
        canvas = Canvas(root, bg="white")
        canvas.pack()
        canvas.config(width=width, height=height)
        for i in range(self.N):
            for j in range(self.N):
                color = colors[self.grid_state[i, j]]
                cellx = startx + j * cellwidth
                celly = starty + i * cellwidth
                canvas.create_rectangle(cellx, celly, cellx+cellwidth, celly+cellwidth,
                                        fill=color, outline="black")
        canvas.update()
        mainloop()


if __name__ == '__main__':
    for iter in range(1):
        pl = percolation(20)
        for i in range(20):
            for j in range(20):
                prob = random()
                if prob > 0.5:
                    pl.open(i, j)

        print(pl.numberOfOpenSites())
        print(pl.grid_link.count)
        print('Is percolating? ', pl.percolates())
        pl.grid_visualization()
        print(' ')

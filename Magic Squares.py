
import math
import os
import random
import re
import sys

class Magic:
    def infoMagic(self,n):
        return f"For {n}x{n} \nThere are {self.noofsquers} Magic Squares That The Sum of Each Directions of it = {self.allsum(n)} \nThe Lowest Cost to convert The square you entered to the best match is : {self.FormMagic(s,n)}\nThe one that fits for you at lowest cost ({self.FormMagic(s,n)}) is : {self.MatThatFits(s,n)} "
    ################################################     Creating Magic Square    ###########################################
    def FormMagic(self,s,n):
        self.n = n
        self.s = s 
        self.s = sum(self.s, []) # flaten s
                                        ################   IF 3x3 Matrix  #################
        if self.n == 3:
            self.magic_squares = [
                [8, 1, 6, 3, 5, 7, 4, 9, 2],
                [6, 1, 8, 7, 5, 3, 2, 9, 4],
                [4, 9, 2, 3, 5, 7, 8, 1, 6],
                [2, 9, 4, 7, 5, 3, 6, 1, 8],
                [8, 3, 4, 1, 5, 9, 6, 7, 2],
                [4, 3, 8, 9, 5, 1, 2, 7, 6],
                [6, 7, 2, 1, 5, 9, 8, 3, 4],
                [2, 7, 6, 9, 5, 1, 4, 3, 8]]
            self.costs = []  # this variable will contain all possible costs
            for magic_square in self.magic_squares:
                self.costs.append(sum([abs(magic_square[i] - self.s[i]) for i in range(self.n*self.n)]))
            return min(self.costs)
                                        ################   IF 4x4 Matrix  #################        
        if self.n == 4: 
            self.magic_squares = [
                [1,15,14,4,10,11,8,5,7,6,9,12,16,2,3,13],
                [1,8,13,12,15,10,3,6,4,5,16,9,14,11,2,7],
                [1,8,10,15,14,11,5,4,7,2,16,9,12,13,3,6],
                [1,12,13,8,15,6,3,10,4,9,16,5,14,7,2,11],
                [2,7,14,11,13,12,1,8,3,6,15,10,16,9,4,5],
                [2,11,14,7,13,8,1,12,3,10,15,6,16,5,4,9],
                [3,6,12,13,16,9,7,2,5,4,14,11,10,15,1,8],
                [3,10,15,6,16,5,4,9,2,11,14,7,13,8,1,12],
                [4,9,16,5,14,7,2,11,1,12,13,8,15,6,3,10],
                [4,5,16,9,14,11,2,7,1,8,13,12,15,10,3,6],
                [5,16,9,4,11,2,7,14,8,13,12,1,10,3,6,15],
                [5,4,9,16,11,14,7,2,8,1,12,13,10,15,6,3],
                [6,15,10,3,9,4,5,16,7,14,11,2,12,1,8,13],
                [6,3,10,15,9,16,5,4,7,2,11,14,12,13,8,1],
                [7,14,11,2,12,1,8,13,6,15,10,3,9,4,5,16],
                [7,2,11,14,12,13,8,1,6,3,10,15,9,16,5,4],
                [8,13,12,1,10,3,6,15,5,16,9,4,11,2,7,14],
                [8,1,12,13,10,15,6,3,5,4,9,16,11,14,7,2],
                [9,16,5,4,7,2,11,14,12,13,8,1,6,3,10,15],
                [9,4,5,16,7,14,11,2,12,1,8,13,6,15,10,3],
                [10,15,6,3,5,4,9,16,11,14,7,2,8,1,12,13],
                [10,3,6,15,5,16,9,4,11,2,7,14,8,13,12,1],
                [11,14,7,2,8,1,12,13,10,15,6,3,5,4,9,16],
                [11,2,7,14,8,13,12,1,10,3,6,15,5,16,9,4],
                [12,1,8,13,6,15,10,3,9,4,5,16,7,14,11,2],
                [12,6,15,1,13,3,10,8,2,16,5,11,7,9,4,14],
                [12,13,8,1,6,3,10,15,9,16,5,4,7,2,11,14],
                [13,8,1,12,3,10,15,6,16,5,4,9,2,11,14,7],
                [13,12,1,8,3,6,15,10,16,9,4,5,2,7,14,11],
                [14,11,2,7,1,8,13,12,15,10,3,6,4,5,16,9],
                [14,7,2,11,1,12,13,8,15,6,3,10,4,9,16,5],
                [15,10,3,6,4,5,16,9,14,11,2,7,1,8,13,12],
                [15,6,3,10,4,9,16,5,14,7,2,11,1,12,13,8],
                [16,5,4,9,2,11,14,7,13,8,1,12,3,10,15,6],
                [16,2,3,13,5,11,10,8,9,7,6,12,4,14,15,1],
                [16,3,13,2,5,10,8,11,4,15,1,14,9,6,12,7],
                [7,9,6,12,2,16,3,13,11,5,10,8,14,4,15,1],
                [9,6,12,7,16,3,13,2,5,10,8,11,4,15,1,14],
                [6,12,7,9,3,13,2,16,10,8,11,5,15,1,14,4],
                [12,7,9,6,13,2,16,3,8,11,5,10,1,14,4,15],
                [2,16,3,13,11,5,10,8,14,4,15,1,7,9,6,12],
                [3,13,2,16,10,8,11,5,15,1,14,4,6,12,7,9],
                [11,5,10,8,14,4,15,1,7,9,6,12,2,16,3,13],
                [5,10,8,11,4,15,1,14,9,6,12,7,16,3,13,2],
                [10,8,11,5,15,1,14,4,6,12,7,9,3,13,2,16],
                [8,11,5,10,1,14,4,15,12,7,9,6,13,2,16,3],
                [14,4,15,1,7,9,6,12,2,16,3,13,11,5,10,8],
                [1,14,4,15,8,11,5,10,13,2,16,3,12,7,9,6]]
            self.costs = []  # this variable will contain all possible costs
            for magic_square in self.magic_squares:
                self.costs.append(sum([abs(magic_square[i] - self.s[i]) for i in range(self.n*self.n)]))
            return min(self.costs)
                                    ################   IF 5x5 Matrix  #################
        if self.n == 5: 
            self.magic_squares = [
                [17,24,1,8,15,23,5,7,14,16,4,6,13,20,22,10,12,19,21,3,11,18,25,2,9],
                [11,24,7,20,3,4,12,25,8,16,17,5,13,21,9,10,18,1,14,22,23,6,19,2,15],
                [23,12,1,20,9,4,18,7,21,15,10,24,13,2,16,11,5,19,8,22,17,6,25,14,3],
                [8,12,4,17,24,11,20,10,23,1,19,21,13,5,7,25,3,16,6,15,2,9,22,14,18],
                [18,24,5,6,12,22,3,9,15,16,1,7,13,19,25,10,11,17,23,4,14,20,21,2,8],
                [1,15,22,18,9,23,19,6,5,12,10,2,13,24,16,14,21,20,7,3,17,8,4,11,25],
                [1,7,13,19,25,18,24,5,6,12,10,11,17,23,4,22,3,9,15,16,14,20,21,2,8]]
            self.costs = []  # this variable will contain all possible costs
            for magic_square in self.magic_squares:
                self.costs.append(sum([abs(magic_square[i] - self.s[i]) for i in range(self.n*self.n)]))
            return min(self.costs)
    #############################################   The Minmum Sum of Each Direction  #################################################
    def allsum(self,n):
        if n == 3 :
            return 15
        if n == 4:
            return 34
        if n == 5:
            return 65
    #############################################   Famous Matrix for this Number  #################################################
    def noofsquers(self,n):
        if n == 3 :
            return 8
        if n == 4:
            return 47
        if n == 5:
            return 7
    #############################################   Returning The Fitting Matrix  #################################################
    def MatThatFits(self,s,n):
        return self.magic_squares[self.costs.index(min(self.costs))]        
    ################################################################################################################################

print ("Enter your nXn size : ")
n = int(input())
print ("Enter your Matrix ( row by row ) each 2 numbers separated by space : ")
s = []

for _ in range(n):
    s.append(list(map(int, input().rstrip().split())))

results = Magic()
print (results.infoMagic(n))


#### Checking Repo ####
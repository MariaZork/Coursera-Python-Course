# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 01:21:36 2018

author: Maria Zorkaltseva
"""
from sys import stdin
from copy import deepcopy


class MatrixError(Exception):
    def __init__(self, Mat1, Mat2):
        self.matrix1 = Mat1
        self.matrix2 = Mat2


class Matrix():
    def __init__(self, list_of_lists):
        self.mat = deepcopy(list_of_lists)
        self.row = len(self.mat)
        self.col = len(self.mat[0])
        self._matRes = []

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.mat)

    def size(self):
        return (self.row, self.col)

    def __add__(self, other):
        if self.row == other.row and self.col == other.col:
            self._matRes = [
                [0 for r in range(self.col)] for c in range(self.row)
            ]
            for i in range(self.row):
                for j in range(self.col):
                    self._matRes[i][j] += self.mat[i][j] + other.mat[i][j]
        else:
            raise MatrixError(self, other)
        return Matrix(self._matRes)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self._matRes = [
                [0 for r in range(self.col)] for c in range(self.row)
            ]
            for i in range(self.row):
                for j in range(self.col):
                    self._matRes[i][j] = other * self.mat[i][j]
            return Matrix(self._matRes)

    def __rmul__(self, other):
        return self.__mul__(other)

    def transpose(self):
        self.row, self.col = self.col, self.row
        self.mat = [list(item) for item in zip(*self.mat)]
        return Matrix(self.mat)

    @staticmethod
    def transposed(self):
        m = self.mat
        m = [list(item) for item in zip(*self.mat)]
        return Matrix(m)

exec(stdin.read())

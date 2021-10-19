from sys import stdin
from copy import deepcopy

class Matrix():
    def __init__(self, list_of_lists):
        self.mat = deepcopy(list_of_lists)
        self.row = len(self.mat)
        self.col = len(self.mat[0])
        self._matRes =[]
    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.mat)

    def size(self):
        return (self.row, self.col)

    def __add__(self, other):
        if self.row == other.row and self.col == other.col:
            self._matRes = [
                [0 for _ in range(self.col)] for _ in range(self.row)
            ]
            for i in range(self.row):
                for j in range(self.col):
                    self._matRes[i][j] += self.mat[i][j] + other.mat[i][j]
        return Matrix(self._matRes)
    def transpose(self):
        print(*zip(*self.mat))
        self.mat = [list(item) for item in zip(*self.mat)]
        print(*zip(*self.mat))
        return Matrix(self.mat)

m = Matrix([[10, 10], [0, 0], [1, 1]])
m2 = Matrix([[0, 1], [20, 0], [-1, -2]])
print(m)
print(m.size())
print(m+m2)
print()
print(m.transpose())

exec(stdin.read())
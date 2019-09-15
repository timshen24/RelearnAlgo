from typing import List
from collections import Counter, defaultdict


def distance(i, j):
    return (i[0] - j[0]) * (i[0] - j[0]) + (i[1] - j[1]) * (i[1] - j[1])


def numberOfBoomerangs(points: List[List[int]]) -> int:
    d = dict()
    for i in range(len(points)):
        for j in range(len(points)):
            if i != j:
                d[distance(points[i], points[j])] = d.get(distance(points[i], points[j]), 0) + 1

    sum = 0
    for v in d.values():
        sum += v * (v - 1)
    return sum

if __name__ == '__main__':
    print(numberOfBoomerangs([[0, 0], [1, 0], [2, 0]]))
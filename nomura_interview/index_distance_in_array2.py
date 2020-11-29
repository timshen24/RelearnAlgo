import sys

def shortest_distance_in_array(A):
    l = []
    for i, v in enumerate(A):
        l.append((i, v))
    l.sort(key=lambda x: x[1])
    print(l)
    num = sys.maxsize
    for i in range(len(l) - 1):
        j = i
        while l[j][1] == l[j + 1][1]:
            j += 1
        if i != j:
            for x in range(i, j + 1):
                if abs(l[x][0] - l[j + 1][0]) < num:
                    num = abs(l[x][0] - l[j + 1][0])
            i = j + 1
        if abs(l[i + 1][0] - l[i][0]) < num:
            num = abs(l[i + 1][0] - l[i][0])
    return num

if __name__ == '__main__':
    print(shortest_distance_in_array([1, 4, 7, 3, 3, 5]))
    print(shortest_distance_in_array([1, 5, 7, 3, 3, 4]))

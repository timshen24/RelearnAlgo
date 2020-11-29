def shortest_distance_in_array(A):
    l = []
    for i, v in enumerate(A):
        l.append((i, v))
    l.sort(key=lambda x: x[1])
    print(l)
    num = 8888888888888
    for i in range(len(l) - 1):
        l2 = []
        while l[i + 1][1] == l[i][1]:
            l2.append(l[i])
            l2.append(l[i + 1])
            i += 1
        if l2 and min(abs(l2[0][0] - l[i + 1][0]), abs(l2[-1][0] - l[i + 1][0])) < num:
            num = min(abs(l2[0][0] - l[i + 1][0]), abs(l2[-1][0] - l[i + 1][0]))
        if abs(l[i + 1][0] - l[i][0]) < num:
            num = abs(l[i + 1][0] - l[i][0])
    return num


if __name__ == '__main__':
    print(shortest_distance_in_array([1, 4, 7, 3, 3, 5]))
    print(shortest_distance_in_array([1, 5, 7, 3, 3, 4]))

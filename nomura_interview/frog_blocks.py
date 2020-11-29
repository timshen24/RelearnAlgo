def longest_distance(blocks):
    distance = -1
    for i in range(len(blocks)):
        index_1, index_2 = i, i
        for j in range(i - 1, -1, -1):
            if blocks[j] >= blocks[index_1]:
                index_1 = j
            else:
                break
        for k in range(i + 1, len(blocks)):
            if blocks[k] >= blocks[index_2]:
                index_2 = k
            else:
                break
        if index_2 - index_1 + 1 > distance:
            distance = index_2 - index_1 + 1
    return distance


if __name__ == '__main__':
    print(longest_distance([2, 6, 8, 5]))
    print(longest_distance([1, 5, 5, 2, 6]))
    print(longest_distance([1, 1]))

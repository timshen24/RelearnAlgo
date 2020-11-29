def longest_distance(blocks):
    max_incre_seq_length, max_decre_seq_length = [0] * len(blocks), [0] * len(blocks)
    for i in range(1, len(blocks)):
        max_incre_seq_length[i] = max_incre_seq_length[i - 1] + 1 if blocks[i] >= blocks[i - 1] else 1
    for i in range(1, len(blocks)):
        max_decre_seq_length[i] =  max_decre_seq_length[i - 1] + 1 if blocks[i] <= blocks[i - 1] else 1
    return max([max_incre_seq_length[i] + max_decre_seq_length[i] for i in range(len(blocks))])



if __name__ == '__main__':
    print(longest_distance([2, 6, 8, 5]))
    print(longest_distance([1, 5, 5, 2, 6]))
    print(longest_distance([1, 1]))

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def xorFromOne(N):
    if N % 4 == 0:
        return N
    elif N % 4 == 1:
        return 1
    elif N % 4 == 2:
        return N + 1
    return N


def solution(M, N):
    # write your code in Python 3.6
    return xorFromOne(M - 1) ^ xorFromOne(N)


print(solution(5, 13))
print(solution(88888, 1000000000))
def flip(a):
    num1, num2 = 0, 0
    # 先做010101
    for i, e in enumerate(a):
        if not i % 2:
            if e:
                num1 += 1
        else:
            if not e:
                num1 += 1
    for i, e in enumerate(a):
        if not i % 2:
            if not e:
                num2 += 1
        else:
            if e:
                num2 += 1
    return num1 if num1 < num2 else num2


if __name__ == '__main__':
    A = [1, 0, 1, 0, 1, 1]
    print(flip(A))
    A = [1, 1, 1]
    print(flip(A))
    A = [1, 1, 0, 1, 1]
    print(flip(A))
    A = [0, 1, 0]
    print(flip(A))
    A = [0, 1, 1, 0]
    print(flip(A))
[]
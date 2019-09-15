def isHappy(n: int) -> bool:
    s = set()
    sum = 0
    while True:
        l = n_to_digits(n)
        for i in l:
            sum += i * i
        if sum == 1:
            return True
        if sum in s:
            return False
        s.add(sum)
        n = sum
        sum = 0


def n_to_digits(n):
    l = []
    while n > 0:
        l.append(n % 10)
        n = int(n / 10)
    return l

if __name__ == '__main__':
    print(isHappy(19))
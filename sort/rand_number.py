import random
import pymssql
def random_numbers(n, low, high):
    return [random.randint(low, high) for i in range(n)]

if __name__ == '__main__':
    print(random_numbers(100, 0, 10000))
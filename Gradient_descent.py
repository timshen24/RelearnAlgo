# 用梯度下降算法求函数最小值：L=x1^2 + 2x2^2
import matplotlib.pyplot as plt

m = 0.01
x1 = 1
x2 = 3
L = x1 ** 2 + 3 * x2 ** 2
n = 0
err = 1
threshold = 0.0000001
value = []

while (err > threshold and n < 100000):
    x1 = x1 - 2 * m * x1  # 迭代
    x2 = x2 - 4 * m * x2  # 迭代
    err = abs(x1 ** 2  + 3 * x2 ** 2 - L)  # 计算前后两次迭代后函数差值的绝对值
    value.append(err)
    L = x1 ** 2 + 3 * x2 ** 2
    n += 1

print(x1, x2, L, n)
plt.plot(value)
plt.show()
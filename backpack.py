n = 5
w = 9
items = [2, 2, 4, 6, 3]
states = [False for i in range(w + 1)]
states[0] = True
states[items[0]] = True

def dp():
    for i in range(1, n):
        # for j in range(w - items[i], -1, -1):
        for j in range(0, w - items[i] + 1):
            if states[j]:
                states[j + items[i]] = True
    for i in range(w, -1, -1):
        if states[i] == True:
            return i
    return 0


print(dp())

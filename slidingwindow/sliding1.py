def maxSum(arr, k):
    length = len(arr)
    assert length >= k
    result = -11111111
    window_sum = sum(arr[:k])
    print(f"init window_sum is {window_sum}")
    for i in range(k, length):
        window_sum = window_sum + arr[i] - arr[i-k]
        print(f'window_sum = {window_sum}, i = {i}')
        if window_sum > result:
            result = window_sum
    return result


arr = [80, -50, 90, 100]
k = 2
answer = maxSum(arr, k)
print(answer)
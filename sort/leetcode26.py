def removeDuplicates(nums):
    j = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
    return len(nums[0:j])


if __name__ == '__main__':
    data = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    data = [1, 1, 2]
    data = [1, 2, 3, 4, 5]
    l = removeDuplicates(data)
    print(l)

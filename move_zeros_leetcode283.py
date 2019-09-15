# leecode 283

def move_zeros0(nums):
    k = 0
    for i in range(len(nums)):
        if nums[i]:
            nums[k] = nums[i]
            k+=1
    for i in range(k, len(nums)):
        nums[i] = 0

def move_zeros(nums):
    k=0
    for i in range(nums):
        if nums[i] != 0:
            if i != k:
                nums[k], nums[i] = nums[i], nums[k]
            k+=1
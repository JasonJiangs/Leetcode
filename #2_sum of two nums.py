# -*- codeing = utf-8 -*-
# @Time : 2020/11/24 17:17
# @Author : Jason
# @File : #2_sum of two nums.py
# @Software: PyCharm

# given nums = [2, 7, 11, 15], target = 9
#
# since nums[0] + nums[1] = 2 + 7 = 9
# then return [0, 1]

# algorithm1: key is to find if there exist num2 = target - num1


def twoSum1(nums, target):
    lens = len(nums)  # get length of the array
    j = -1  # initialize index j
    for i in range(lens):  # i start from 0 to lens-1
        if (target - nums[i]) in nums:  # check if there exist such element, dive into
            # count shows if element only shows once
            if (nums.count(target - nums[i]) == 1) & (target - nums[i] == nums[i]):
                continue
            else:
                j = nums.index(target - nums[i], i + 1)  # find num2 after index of num1
                break
    if j > 0:
        return [i, j]
    else:
        return []


# algorithm2: optimize base on first algorithm
# for algorithm2, we find num2 after num1, this time we find num2 before num1
# this method is more direct than the first one which will go through the whole list
def twoSum2(nums, target):
    lens = len(nums)  # still get length of array
    j = -1  # initialize j
    for i in range(1, lens):  # get index i from 1 to lens, not 0 since we check backward
        if (target - nums[i]) in nums[:i]:  # match num2 with target
            j = nums.index(target - nums[i], 0, i)  # get the index of the matching
            break
    if j >= 0:
        return [j, i]
    else:
        return []


# algorithm3: using hashmap(dict) to track the index related to the element
# speed is faster and logic is clear
def twoSum3(nums, target):
    hashmap = {}
    # create hashmap by using for loop
    for index, num in enumerate(nums):
        hashmap[num] = index  # element point to the index
    for i, num in enumerate(nums):
        j = hashmap.get(target - num)  # get index j, it may get result or none
        if j is not None and i != j:
            return [i, j]
    return []


# algorithm4: also using hashmap, and improve algorthm3 like from A1 to A2
# instead of go through the whole list, try just check before or after
# this time check num1 before
def twoSum4(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        # if there is possible that exist num2
        # no need check if it's just same index
        if hashmap.get(target - num) is not None:
            return [i, hashmap.get(target - num)]
        # renew the hashmap every time to match the data before num1
        hashmap[num] = i
    return []


# algorithm5: sort + two pointers
# idea is kind of like quick sort, first sort values, then two indexes start from both ends
# sum up two values, if small, increase; if too big, decrease by moving index
def twoSum5(nums, target):
    nums = bubble_sort(nums)
    i, j = 0, len(nums) - 1
    while i < j:
        sum = nums[i] + nums[j]
        if sum < target:
            i += 1
        elif sum > target:
            j -= 1
        else:
            return [i + 1, j + 1]
    return []


# bubble sort used for algorithm5
def bubble_sort(data):
    for i in range(len(data) - 1):
        indicator = False
        for j in range(len(data) - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                indicator = True
        if not indicator:
            break


# implementation code: hrt random input of what you want and get output
arr = input("Input nums: ")
nums = [int(n) for n in arr.split()]
target = int(input("Input target value: "))
# res = twoSum1(nums, target)
# res = twoSum2(nums, target)
# res = twoSum3(nums, target)
res = twoSum4(nums, target)
# res = twoSum5(nums, target)
print("Result shown: ", res)

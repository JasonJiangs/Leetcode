# -*- coding: utf-8 -*-
# @Time : 2021/1/21 10:38 
# @Author : Jason
# @File : #628 Maximum Product of Three Numbers.py 
# @Software: PyCharm

from timeit import default_timer as timer


# EASY
# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

class Solution(object):
    # Reverse=True lists the nums in descending order.
    # Try the maximum, using slicing, first product is the product of first three numbers which are the largest.
    # But there exist chances that two negative numbers with one positive number.
    # So that here grab the last two integers which might be negative values
    # with one positive number that should be the largest, it is nums[0]
    def maximumProductMethod1(self, nums):
        nums.sort(reverse=True)
        return max(nums[0] * nums[1] * nums[2], nums[0] * nums[-1] * nums[-2])

    # In method1, we just need the largest three integers and the last two smallest integers
    # So here scan the whole list to find those numbers without using its own method.
    # The flaw for this is that is still using list which cost more time complexity
    # when find min and max of list every time in the loop;
    def maximumProductMethod2(self, nums):
        posiInf = float("inf")
        negInf = -float("inf")
        posiList = [negInf, negInf, negInf]
        negList = [posiInf, posiInf]
        for i in range(len(nums)):
            posiMin = min(posiList)
            negMax = max(negList)
            if nums[i] > posiMin:
                posiList[posiList.index(posiMin)] = nums[i]
            if nums[i] < negMax:
                negList[negList.index(negMax)] = nums[i]
        return max(posiList[0] * posiList[1] * posiList[2], negList[0] * negList[1] * max(posiList))

    # Here is the result from official which has same logic as method 2
    # but without using list, cost only O(N) time complexity whose N is the length of array
    # space complexity is O(1)
    # much faster, but less readability
    def maximumProductMethod3(self, nums):
        min1 = float("inf")
        min2 = float("inf")
        max1 = -float("inf")
        max2 = -float("inf")
        max3 = -float("inf")
        for i in range(len(nums)):
            if (nums[i] < min1):
                min2 = min1
                min1 = nums[i]
            elif (nums[i] < min2):
                min2 = nums[i]
            if (nums[i] > max1):
                max3 = max2
                max2 = max1
                max1 = nums[i]
            elif (nums[i] > max2):
                max3 = max2
                max2 = nums[i]
            elif (nums[i] > max3):
                max3 = nums[i]
        return max(min1 * min2 * max1, max1 * max2 * max3)

# Analysis: The solutions above are some kinds of greedy approach
# We can also use enumeration method which will cause much more time O(N^3)
# Since we need to try and compare every answers.


nums = [1, 2, 3, -2, -230, 2, 0, 1, 32, 43]

start1 = timer()
result1 = Solution().maximumProductMethod1(nums)
end1 = timer()
print("The result of method 1 is ", result1)
print("The time consuming is ", end1 - start1, '\n')

start2 = timer()
result2 = Solution().maximumProductMethod2(nums)
end2 = timer()
print("The result of method 2 is ", result2)
print("The time consuming is ", end2 - start2, '\n')

start3 = timer()
result3 = Solution().maximumProductMethod3(nums)
end3 = timer()
print("The result of method 3 is ", result3)
print("The time consuming is ", end3 - start3, '\n')


# -*- coding: utf-8 -*-
# @Time : 2021/2/9 13:44 
# @Author : Jason
# @File : #455 Assign Cookies.py 
# @Software: PyCharm

from timeit import default_timer as timer


# EASY
# Question: Assume you are an awesome parent and want to give your children some cookies.
# But, you should give each child at most one cookie.
# Each child i has a greed factor g[i], which is the minimum size of a cookie that the child
# will be content with; and each cookie j has a size s[j].
# If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content.
# Your goal is to maximize the number of your content children and output the maximum number.

class Solution(object):
    # greedy approach, first rank the greed factor, and start from the child that has the least factor
    # Also rank the size array. Start a loop to fit the size
    # the core is not waste the number of cookie, do not give the extra quantity of cookie to the child.
    def findContentChildren1(self, g, s):
        mergeSort(g, 0, len(g) - 1)
        mergeSort(s, 0, len(s) - 1)
        contentNum = 0
        for i in range(len(g)):
            for j in range(len(s)):
                if s[j] >= g[i]:
                    contentNum = contentNum + 1
                    s[j] = -1
                    break
        return contentNum
    # The method is passed, but it takes much space and time since every time it will go through the array once
    # So the time complexity will mainly based on len(s)*len(g).

    # The second solution is to delete the cookies that have been used here.
    # which will not be repeated in the following loops.
    # It reduce more than half of the time.
    def findContentChildren2(self, g, s):
        g.sort()
        s.sort()
        contentNum = 0
        for i in range(len(g)):
            for j in range(len(s)):
                if s[j] >= g[i]:
                    s.remove(s[j])
                    contentNum = contentNum + 1
                    break
        return contentNum

    # This method we will not use loop to do it.
    # Put two keys to those two sorted arrays.
    # Judge the situations and decide how to do it.
    def findContentChildren3(self, g, s):
        g.sort()
        s.sort()
        g_len, s_len = len(g), len(s)
        g_left = s_left = contentNum = 0
        while g_left < g_len and s_left < s_len:
            if g[g_left] <= s[s_left]:
                contentNum += 1
                g_left += 1
                s_left += 1
            else:
                s_left += 1
        return contentNum


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:
        m = int((l + (r - 1)) / 2)
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


# Variable Input
g = [1, 2, 3, 1]  # greed factor (min size of a cookie that the child wil be content)
s = [1, 1, 2, 3]  # each cookie's size

# Result testing and time consuming.
start1 = timer()
result1 = Solution().findContentChildren1(g, s)
end1 = timer()
duration1 = end1 - start1
print("Result one is ", result1, ", time cost is ", duration1, ".")

g = [1, 2, 3, 1]  # greed factor (min size of a cookie that the child wil be content)
s = [1, 1, 2, 3]  # each cookie's size

start2 = timer()
result2 = Solution().findContentChildren2(g, s)
end2 = timer()
duration2 = end2 - start2
print("Result one is ", result2, ", time cost is ", duration2, ".")

g = [1, 2, 3, 1]  # greed factor (min size of a cookie that the child wil be content)
s = [1, 1, 2, 3]  # each cookie's size

start3 = timer()
result3 = Solution().findContentChildren3(g, s)
end3 = timer()
duration3 = end3 - start3
print("Result one is ", result3, ", time cost is ", duration3, ".")
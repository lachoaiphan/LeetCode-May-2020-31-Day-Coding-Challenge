"""
Prompt:
You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, 
all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
 which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. 
Implement a function to find the first bad version. 
You should minimize the number of calls to the API.
"""

# Runs in O(log n) time and O(1) space. Used a binary search algorithm


def isBadVersion(n):
    version = 3
    return n >= version


def firstBadVersion(n):
    left = 1
    right = n
    while left <= right:
        mid = (left + right) // 2
        if isBadVersion(mid) == False:
            if isBadVersion(mid + 1) == True:
                return mid + 1
            left = mid + 1
        else:
            if isBadVersion(mid - 1) == False:
                return mid
            right = mid - 1
    raise ValueError("No bad version!")


# Test Case:
print(firstBadVersion(5))  # prints bad version number in function

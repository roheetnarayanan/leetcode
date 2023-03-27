# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            middle = (left+right)//2

            if isBadVersion(middle):
                right = middle ## since it might be the first bad version
            else:
                left = middle+1
        return left
        

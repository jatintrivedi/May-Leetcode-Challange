class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        while(i < n):
            mid = int(i +(n-i)/2)
            if(isBadVersion(mid)):
                n = mid                  
            else:
                i = mid + 1           
        return i

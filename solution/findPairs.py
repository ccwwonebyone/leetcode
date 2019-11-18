from typing import List
import collections

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        vt = collections.Counter(nums)
        for i in vt:
            if (k > 0 and i+k in vt) or (k == 0 and vt[i] > 1):
                res += 1
        return res

if __name__ == '__main__':

    solution = Solution()
    print(solution.findPairs([1,2,3,4,3], 3))

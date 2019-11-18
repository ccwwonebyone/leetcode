from typing import List

class Solution(object):
    def findRelativeRanks(self, nums:List[int]) -> List[str]:
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        numS = {}
        for i in range(len(nums)):
            numS[i] = nums[i]
        numS = sorted(numS.items(), key=lambda asd:asd[1],reverse = True)
        re = nums
        j = 1
        for i in numS:
            a,s = i
            print(a)
            if j > 3:
                re[a] = str(j)
            else:
                if j == 1:
                    re[a] = 'Gold Medal'
                if j == 2:
                    re[a] = 'Silver Medal'
                if j == 3:
                    re[a] = 'Bronze Medal'
            j += 1
        return re


if __name__ == '__main__':

    solution = Solution()
    print(solution.findRelativeRanks([1,2,3,4,3]))

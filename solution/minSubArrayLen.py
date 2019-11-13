import sys

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        length = len(nums)
        sumS = 0
        minSub = sys.maxsize
        for i in range(length):
            sumS += nums[i]
            while sumS >= s:
                sumS -= nums[j]
                minSub = min(minSub,i - j + 1)
                j += 1
        return 0 if minSub == sys.maxsize else minSub

if __name__ == "__main__":

    solution = Solution()
    print(solution.minSubArrayLen(7,[2,3,1,2,4,3]))

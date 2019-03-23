class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        temp = 0
        maxs = 0
        passNum = {}
        for i in range(len(nums)):
            try:
                c = passNum[i]
                continue
            except:
                pass
            first = nums[i]
            j = 0
            while first != nums[i] or j == 0:
                i = nums[i]
                passNum[i] = i
                j += 1
            if maxs < j:maxs=j
        return maxs

if __name__ == '__main__':

    solution = Solution()
    print(solution.arrayNesting([5,4,0,3,1,6,2]))
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        con = [0]*(len(nums)+1)
        for i in nums:
            con[i] += 1
            if con[i] > 1:
                return i

if __name__ == '__main__':

    solution = Solution()
    print(solution.findDuplicate([1,2,3,4,3]))

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        revser = k%len(nums)
        for i in range(revser):
            nums.insert(0,nums.pop())

if __name__ == "__main__":
    solution = Solution()
    nums = [-1,-100,3,99]
    print(solution.rotate(nums, 2))
    print(nums)

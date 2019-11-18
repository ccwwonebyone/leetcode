from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        the best
        start = 0
        count = 1
        while count <= len(nums):
            if nums[start] == 0:
                del nums[start]
                nums.append(0)
            else:
                start += 1
            count += 1
        """
        zero_num = 0
        for num in nums:
            if num == 0:
                zero_num += 1
        for i in range(zero_num):
            nums.remove(0)
        nums += [0] * zero_num
        print(nums)
if __name__ == "__main__":
    solution = Solution()
    print(solution.moveZeroes([0,0,1]))

from typing import List


class Solution(object):
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums), 0, -1):
            if nums[i - 1] == val:
                nums.remove(nums[i - 1])
        return len(nums)


if __name__ == "__main__":
    solution = Solution()
    nums = [1]
    print(solution.removeElement(nums, 1))
    print(nums)

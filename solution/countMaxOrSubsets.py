from typing import List


class Solution:
    max_num = 0
    count = 0
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        for i in nums:
            self.max_num = self.max_num | i
        self.dfs(nums, 0, 0)
        return self.count

    def dfs(self, nums: List[int], deep, sub_num):
        if deep == len(nums):
            if sub_num == self.max_num:
                self.count += 1
            return

        self.dfs(nums, deep + 1, sub_num | nums[deep])
        self.dfs(nums, deep + 1, sub_num)


if __name__ == '__main__':
    solution = Solution()
    print(solution.countMaxOrSubsets([3, 1]))

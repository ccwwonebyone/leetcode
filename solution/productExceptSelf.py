from typing import List

class Solution:
    # [1, 2, 3, 4] -> [1, l1, l1*l2, l1*l2*l3] -> [l2*l3*l4, (l1*l2)*l3, ...]
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        base_num = 1
        for num in nums:
            res.append(base_num)
            base_num = base_num * num
        temp_base_num = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * temp_base_num
            temp_base_num = temp_base_num * nums[i]
        return res

if __name__ == "__main__":

    solution = Solution()
    print(solution.productExceptSelf([2,3,4,5]))
    print(solution.productExceptSelf([1,2,3,4]))

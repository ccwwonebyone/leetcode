from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        rnl,rkl = range(len(nums)), range(k)
        sub = 0
        for i in rnl:
            if i+k > len(nums) : continue
            if i == 0:
                for j in rkl:
                    sub += nums[i+j]
                maxTotal = sub
            else:
                sub -= nums[i-1]
                sub += nums[i+k-1]
            if maxTotal < sub:
                maxTotal = sub
        return float(maxTotal)/k

if __name__ == "__main__":

    solution = Solution()
    print(solution.findMaxAverage([1,12,-5,-6,50,3], 4))

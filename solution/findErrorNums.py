from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums2 = range(1,len(nums)+1)
        count = [0]*(len(nums)+1)
        for j in nums:
            count[j] += 1
        for i in nums2:
            if count[i] == 0:
                zeroe = i
            if count[i] == 2:
                two = i
        return [two,zeroe]

if __name__ == "__main__":

    solution = Solution()
    print(solution.findErrorNums([1,2,2,4]))

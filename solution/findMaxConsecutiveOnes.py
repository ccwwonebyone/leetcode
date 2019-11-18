from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = 0
        temp = 0
        for num in nums:
            if num == 1:
                temp += 1
            else:
                if temp > maxi :
                    maxi = temp
                temp = 0
        return maxi if temp < maxi else temp


if __name__ == '__main__':

    solution = Solution()
    print(solution.findMaxConsecutiveOnes([0,1,1,2,2,2,3,4,3,200]))

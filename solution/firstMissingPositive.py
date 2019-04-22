class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        nums.sort()
        i = 1
        for num in nums:
            if num > 0:
                if num != i:
                    if i not in nums:
                        return i
                    else:
                        i += 1
                else:
                    i += 1
        return i

if __name__ == '__main__':

    solution = Solution()
    print(solution.firstMissingPositive([7,8,9,11,12]))
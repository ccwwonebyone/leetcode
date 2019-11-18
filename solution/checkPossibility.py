from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        change_num = 0
        for i in range(len(nums)):
            print('in', nums)
            if i == 0:
                continue
            elif i == 1 and nums[i] < nums[0]:
                print('change')
                nums[0] == nums[i]
                change_num += 1
            elif nums[i] < nums[i - 1]:
                if nums[i] >= nums[i-2]:
                    if change_num == 0:
                        nums[i - 1] = nums[i]
                    else:
                        nums[i] = nums[i-1]
                else:
                    nums[i] = nums[i-1]
                change_num += 1

            print('out', change_num, nums)
            if change_num > 1:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.checkPossibility([1,4,-1,6]))

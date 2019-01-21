

class Solution:
    
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1+nums2
        nums.sort()
        length = len(nums)
        if length%2 == 0 :
            return (nums[int(length/2)-1]+nums[int(length/2)])/2
        else :
            return nums[int(length/2)]

if __name__ == "__main__":

    solution = Solution()
    print(solution.findMedianSortedArrays([1, 3], [2]))
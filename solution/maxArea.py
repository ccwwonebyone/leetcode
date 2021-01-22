

class Solution:
    
    def maxArea(self, height):
        area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            area = max(area, (right-left) * min(height[left],height[right]))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return area        
       
        # for i in range(len(height)-1, -1, -1):
        #     pass
        # max_res = 0
        # for i in range(len(height)-1):
        #     for j in range(i + 1, len(height)):
        #         info = height[i] if height[i] < height[j] else height[j]
        #         area = (j-i) * info
        #         if max_res < area:
        #             max_res = area
        return area


if __name__ == "__main__":

    solution = Solution()
    print(solution.maxArea([1,5,6,19,21,32,1]))


class Solution:
    
    def maxArea(self, height):
        for i in range(len(height)-1, -1, -1):
            pass
        max_res = 0
        for i in range(len(height)-1):
            for j in range(i + 1, len(height)):
                info = height[i] if height[i] < height[j] else height[j]
                area = (j-i) * info
                if max_res < area:
                    max_res = area
        return max_res


if __name__ == "__main__":

    solution = Solution()
    print(solution.maxArea([1,5,6,19,21,32,1]))
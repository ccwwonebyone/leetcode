class Solution:

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return pow(x,n)

if __name__ == "__main__":

    solution = Solution()
    print(solution.myPow(6,7))
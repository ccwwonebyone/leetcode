class Solution(object):
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]

if __name__ == "__main__":

    solution = Solution()
    print(solution.isPalindrome(2))

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s

if __name__ == "__main__":

    solution = Solution()
    print(solution.shortestPalindrome('aacecaaa'))

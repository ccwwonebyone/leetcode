import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        if s == '':
            return True
        pattern = re.compile('[A-Za-z0-9]')
        ls = list(filter(pattern.match,s))
        return True if ls == ls[::-1] else False


if __name__ == "__main__":

    solution = Solution()
    print(solution.isPalindrome('A man, a plan, a canal: Panama'))

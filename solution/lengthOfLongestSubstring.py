

class Solution:
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        maxRes = 0
        strs = ''
        for i in range(len(s)):
            pos = strs.find(s[i])
            if pos != -1:
                if res > maxRes:
                    maxRes = res
                strs = strs[pos+1:] + s[i]
                res = len(strs)
            else:
                strs += s[i]
                res += 1
        return maxRes if maxRes > res else res


if __name__ == "__main__":

    solution = Solution()
    print(solution.lengthOfLongestSubstring('aasdciaclasj'))
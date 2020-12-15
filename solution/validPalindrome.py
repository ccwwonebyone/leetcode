class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = -1
        for i in range(int(len(s)/2)):
            if s[i] != s[-i-1]:
                start = i
                s1 = s[:i]+s[i+1:] if i > 0 else s[i+1:]
                s2 = s[:-i-1]+s[-i:] if i != 0 else s[:-i-1]
                break
        if start == -1 : return True
        for i in range(start,int(len(s)/2)):
            if s1[i] != s1[-i-1] and s2[i] != s2[-i-1]:
                return False
        return True            

if __name__ == "__main__":
    print(Solution().validPalindrome('abca'))
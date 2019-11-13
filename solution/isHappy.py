class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        m = []
        def doit(num):
            res = 0
            for i in num:
                res += int(i)**2
            if res == 1:
                return True
            if res in m:
                return False
            else:
                m.append(res)
            return doit(str(res))
        return doit(str(n))

if __name__ == "__main__":

    solution = Solution()
    print(solution.isHappy(19))

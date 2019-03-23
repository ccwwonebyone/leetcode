class Solution:

    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        dis = {
            'a':A,
            'b':B
        }
        first,second = ('a','b') if A > B else ('b','a')
        times = 0
        s = ''
        for i in range(A + B):
            if dis[first] != dis[second]:
                change = first if times < 2 else second
                times = 0 if times >= 2 else times + 1
            else:
                change = first if s == '' or s[-1] == second else second
                times = 0 if change == second else 2
            dis[change] -= 1
            s += change
        return s

if __name__ == "__main__":

    solution = Solution()
    print(solution.strWithout3a3b(6,7))
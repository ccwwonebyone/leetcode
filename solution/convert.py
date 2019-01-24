

class Solution:
    
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        strMap = []
        for i in range(numRows):
            strMap += [{}]
        temp = 0
        temp2 = 0
        direction = 1
        for i in range(len(s)):
            strMap[temp][temp2] = s[i]
            if temp == 0:
                direction = 1
            if temp == numRows-1:
                direction = -1
            temp += direction
            if direction == -1:
                temp2 += 1
        res = ''
        for info in strMap:
            for index in info:
                res += info[index]
        return res


if __name__ == "__main__":

    solution = Solution()
    print(solution.convert('ABC', 1))
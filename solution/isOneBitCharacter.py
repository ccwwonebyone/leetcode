class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        res = False
        while i <= len(bits)-1:
            if bits[i] == 0:
                i += 1
                res = True
            else:
                i += 2
                res = False
        return res

if __name__ == '__main__':

    solution = Solution()
    print(solution.isOneBitCharacter([1,3,4]))
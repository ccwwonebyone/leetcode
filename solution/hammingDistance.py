class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = x ^ y
        y = 0
        while(x != 0):
            if(x % 2):
                y += 1
            x //= 2
        return y        
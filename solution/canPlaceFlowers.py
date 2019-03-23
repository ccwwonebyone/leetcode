class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        l = len(flowerbed)
        if n == 0:
            return True
        if l == 1:
            if n == 1:
                if flowerbed[0] == 0:
                    return True
                else:
                    return False
            else:
                return False
        for i in range(l):
            if i == 0 or i == l-2:
                if flowerbed[i] == flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        break
                    continue
            if i > l - 2:
                continue
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    break
        return True if n == 0 else False

if __name__ == '__main__':

    solution = Solution()
    print(solution.canPlaceFlowers([1,0,0,0,1],1))
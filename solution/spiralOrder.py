class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if [] == matrix:
            return []
        x = len(matrix)
        y = len(matrix[0])
        s = 0
        b = 0
        re = [matrix[0][0]]
        total = x*y
        z = 0
        j = 0
        right = True
        left  = False
        up    = False
        down  = False
        if y == 1:
            right = False
            down  = True
        x -= 1
        y -= 1
        for i in range(1,total):
            if right:
                j += 1
            if left:
                j -= 1
            if up:
                z -= 1
            if down:
                z += 1
            re.append(matrix[z][j])
            if right and j+1 > y:
                s += 1
                right = False
                down = True
                continue
            if down and z+1 > x:
                y -= 1
                down = False
                left = True
                continue
            if left and j-1 < b:
                x -= 1
                left = False
                up = True
                continue
            if up and z-1 < s:
                b += 1
                up = False
                right = True
                continue
        return re

if __name__ == "__main__":

    solution = Solution()
    print(solution.spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]))

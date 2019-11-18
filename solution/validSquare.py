from typing import List
import math

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distance(one,two):
            return math.sqrt((one[0]-two[0])**2 +(one[1]-two[1])**2)
        ps = [p1,p2,p3,p4]
        diss = {}
        for i in range(len(ps)):
            diss[i] = []
            for j in range(len(ps)):
                if i==j:continue
                diss[i].append(distance(ps[i],ps[j]))
            diss[i].sort()
        print(diss)
        if diss[0] == diss[1] and diss[1] == diss[2] and diss[2] == diss[3] and 0 not in diss[0] and (diss[0][0] == diss[0][1] or diss[0][1] == diss[0][2] or diss[0][0] == diss[0][2]):
            return True
        else:
            return False

if __name__ == '__main__':
    solution = Solution()
    print(solution.validSquare([0,0], [1,1], [1,0], [0,1]))

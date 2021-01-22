from typing import List 

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs) == 0):
            return ""
        commonPrefix = strs[0]
        for i in range(1, len(strs)):
            short = min(len(commonPrefix), len(strs[i]))
            temp = ""
            for j in range(short):
                if commonPrefix[j] == strs[i][j]:
                    temp += commonPrefix[j]
                else:
                    break  
            if temp == "":
                return temp
            commonPrefix = temp    
        return commonPrefix

if __name__ == "__main__":

    solution = Solution()
    print(solution.longestCommonPrefix(["aaa","aa","aaa"]))                
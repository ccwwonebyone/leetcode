class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        re = [[]]
        def sub(subNum,num):
            if len(num)>1:
                for i in range(len(num)):
                    subN = subNum[::]
                    subN.append(num[i])
                    re.append(subN)
                    sub(subN,num[i+1:])
            elif len(num) == 1:
                subN = subNum[::]
                subN.append(num[0])
                re.append(subN)
        sub([],nums)
        return re




if __name__ == "__main__":

    solution = Solution()
    print(solution.subsets([1,2,3]))

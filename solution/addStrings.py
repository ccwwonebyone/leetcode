class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        nums = {
            '0':0,'1':1,'2':2,'3':3,'4':4,
            '5':5,'6':6,'7':7,'8':8,'9':9
        }
        num1 = num1[::-1]
        num2 = num2[::-1]
        re = ''
        l1 = len(num1)
        l2 = len(num2)
        if l1 < l2:
            l1,l2 = l2,l1
            num1,num2 = num2,num1
        nextAdd = 0
        for i in range(l1):
            if i < l2:
                string = str(((nums[num1[i]]+nums[num2[i]]+nextAdd)%10))
                nextAdd = (nums[num1[i]]+nums[num2[i]]+nextAdd)//10
            else:
                string = str((nums[num1[i]]+nextAdd)%10)
                nextAdd = (nums[num1[i]]+nextAdd)//10
            re += string
        if nextAdd > 0:
            re += str(nextAdd)
        return re[::-1]

if __name__ == '__main__':

    solution = Solution()
    print(solution.addStrings("0","0"))
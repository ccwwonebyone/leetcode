

class Solution:
    
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        mark = True
        userful_num = ''
        check = False
        for i in range(len(str)):
            if str[i].isdigit():
                check = True
                userful_num += str[i]
                continue
            elif str[i] == '-' and check == False:
                mark = False
                check = True
                continue
            elif str[i] == '+' and check == False:
                check = True
                continue
            elif str[i] == ' ' and check == False:
                continue
            elif str[i].isdigit() == False:
                break

        if userful_num == '':
            return 0
        max_num = pow(2, 31) - 1
        min_num = -(max_num + 1)
        userful_num = int(userful_num)
        if mark:
            return max_num if userful_num > max_num else userful_num
        else:
            return min_num if userful_num > max_num + 1 else -userful_num


if __name__ == "__main__":

    solution = Solution()
    print(solution.myAtoi('asdasd-123'))
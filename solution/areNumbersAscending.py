from typing import List


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s_arr = s.split(" ")
        base_num = -1
        for i in s_arr:
            if i.isdigit():
                x = int(i)
                if base_num >= x:
                    return False
                base_num = x
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.areNumbersAscending("sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"))

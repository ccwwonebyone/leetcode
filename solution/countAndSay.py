class Solution:
    def countAndSay(self, n: int) -> str:
        init_str = "1"
        while n > 1:
            nums = 0
            base_num = 0
            res = ""
            for i in range(len(init_str)):
                # 第一次
                if i == 0:
                    base_num = init_str[i]
                    nums = 1
                else:
                    # 一样那么直接加一
                    if base_num == init_str[i]:
                        nums += 1
                    # 不一样结束计数
                    else:
                        res += str(nums) + str(base_num)
                        base_num = init_str[i]
                        nums = 1

                if i == len(init_str) - 1:
                    res += str(nums) + str(base_num)
                    continue

            init_str = res
            n -= 1
        return init_str


if __name__ == '__main__':
    solution = Solution()
    print(solution.countAndSay(3))

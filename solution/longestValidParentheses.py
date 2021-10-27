from typing import List


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        stack = [-1]
        for i, chars in enumerate(s):
            if chars == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestValidParentheses("))(((())"))

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.dfs(n, "", res, 0, 0)
        return res

    def dfs(self, n, paths, lists, open_num, close):
        if close > open_num or open_num > n:
            return

        if len(paths) == n * 2:
            lists.append(paths)
            return
        self.dfs(n, paths + "(", lists, open_num + 1, close)
        self.dfs(n, paths + ")", lists, open_num, close + 1)


if __name__ == "__main__":
    solution = Solution()
    print(solution.generateParenthesis(3))

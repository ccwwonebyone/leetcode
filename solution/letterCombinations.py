from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        num_to_char = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        res = []
        self.dfs(num_to_char, "", res, 0, digits)
        return res

    def dfs(self, num_to_char, path, res, now, digits):
        if len(path) == len(digits):
            res.append(path)
            return

        for s in num_to_char[digits[now]]:
            self.dfs(num_to_char, path + s, res, now + 1, digits)


if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCombinations(""))

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 1:
            return False
        if s == '':
            return True
        valid_strs = {'(':')','{':'}','[':']'}
        need_strs = []
        for character in s:
            if len(need_strs) > 0 and character == need_strs[-1]:
                need_strs.pop()
            else:
                if character not in valid_strs.keys():
                    return False
                need_strs.append(valid_strs[character])
        return False if len(need_strs) > 0 else True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid(')('))

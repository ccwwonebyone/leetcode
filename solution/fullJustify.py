class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        allLi = []
        li = []
        oneLi = 0
        for word in words:
            if (len(word) + oneLi + len(li)) <= maxWidth:
                oneLi += len(word)
                li.append(word)
            else:
                space = 0
                isgreedy = 0
                extraLen = maxWidth - oneLi
                if len(li) == 1:
                    li[0] = li[0]+extraLen*' '
                else:
                    space = int(extraLen / (len(li)-1))
                    isgreedy = extraLen % (len(li)-1)
                if isgreedy != 0:
                    for i in range(isgreedy):
                        li[i] += ' '
                allLi.append((space*' ').join(li))
                li = []
                li.append(word)
                oneLi = 0
                oneLi += len(word)
        allLi.append((' ').join(li))
        allLi[-1] += (maxWidth-len(allLi[-1]))*' '
        return allLi



if __name__ == "__main__":

    solution = Solution()
    print(solution.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))

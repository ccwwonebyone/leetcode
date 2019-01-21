

class Solution:
    
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dict_symbol = {
            "1000": "M",
            "900": "CM",
            "500": "D",
            "400": "CD",
            "100": "C",
            "90": "XC",
            "50": "L",
            "40": "XL",
            "10": "X",
            "9": "IX",
            "5": "V",
            "4": "IV",
            "1": "I"
        }
        res = ""
        for symbolNum, symbol in dict_symbol.items():
            symbolNum = int(symbolNum)
            nums = num // symbolNum
            num = num % symbolNum
            res += symbol*nums
        return res


if __name__ == "__main__":

    solution = Solution()
    print(solution.intToRoman(123))
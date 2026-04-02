class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numToLetters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        def combo(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in numToLetters[digits[i]]:
                combo(i + 1, curStr + c)
            
        if digits:
            combo(0, "")
        return res
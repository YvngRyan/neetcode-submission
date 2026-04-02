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
        def backtrack(i, currStr):
            if i == len(digits):
                res.append(currStr)
                return
            if i > len(digits):
                return
            
            for c in numToLetters[digits[i]]:
                backtrack(i + 1, currStr + c)
        if digits:
            backtrack(0, "")
        return res
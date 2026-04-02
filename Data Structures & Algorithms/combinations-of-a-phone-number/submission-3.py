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
        def dfs(i, currCombo):
            if len(currCombo) == len(digits):
                res.append(currCombo)
                return
            if i == len(digits):
                return

            for c in numToLetters[digits[i]]:
                dfs(i + 1, currCombo + c)
        if digits:
            dfs(0, "")
        return res
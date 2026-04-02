class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        # if len(array) == 2 and arr[0] != arr[1]:
        #     return 2

        res = 1

        sign = ""
        curr = 1
        for i in range(1, len(arr)):
            if sign == "":
                if arr[i] > arr[i - 1]:
                    curr += 1
                    sign = "more"
                elif arr[i] < arr[i - 1]:
                    curr += 1
                    sign = "less"
                else:
                    curr = 1
                    sign = ""
            else:
                if arr[i] > arr[i - 1] and sign == "less":
                    curr += 1
                    sign = "more"
                elif arr[i] < arr[i - 1] and sign == "more":
                    curr += 1
                    sign = "less"
                else:
                    curr = 2 if arr[i] != arr[i - 1] else 1
                    sign = "more" if arr[i] > arr[i - 1] else ("less" if arr[i] < arr[i - 1] else "")
            res = max(curr, res)

        return res
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        memo = {}

        def dfs(i):
            if i == len(s):
                return 0

            if i in memo:
                return memo[i]

            # take current char as extra
            res = 1 + dfs(i + 1)

            # try matching dictionary words
            for j in range(i, len(s)):
                if s[i:j + 1] in words:
                    res = min(res, dfs(j + 1))

            memo[i] = res
            return res

        return dfs(0)
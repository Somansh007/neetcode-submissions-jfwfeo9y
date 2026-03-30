class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]

            memo[i] = max(dfs(i + 1),
                          nums[i] + dfs(i + 2))
            return memo[i]

        return dfs(0)
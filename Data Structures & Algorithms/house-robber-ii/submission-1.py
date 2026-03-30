class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        memo = {}

        def dfs(i, flag):
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0

            if (i, flag) in memo:
                return memo[(i, flag)]

            res = max(
                dfs(i + 1, flag),
                nums[i] + dfs(i + 2, flag or i == 0)
            )

            memo[(i, flag)] = res
            return res

        return max(dfs(0, True), dfs(1, False))
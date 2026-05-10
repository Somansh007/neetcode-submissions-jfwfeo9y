class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def canSplit(maxSum):
            pieces = 1
            curSum = 0

            for num in nums:
                if curSum + num > maxSum:
                    pieces += 1
                    curSum = 0

                curSum += num

            return pieces <= k

        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = (left + right) // 2

            if canSplit(mid):
                right = mid
            else:
                left = mid + 1

        return left
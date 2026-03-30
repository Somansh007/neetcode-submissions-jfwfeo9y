from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []

        for i in range(len(nums)):
            # Remove indices out of window
            if dq and dq[0] == i - k:
                dq.popleft()

            # Remove smaller elements (useless)
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # Start adding results after first window
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
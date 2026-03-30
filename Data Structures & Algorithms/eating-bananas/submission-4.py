import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2

            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile / mid)

            if totalTime <= h:
                right = mid   # try smaller speed
            else:
                left = mid + 1  # need more speed

        return left
# """
# This is MountainArray's API interface.
# class MountainArray:
#     def get(self, index: int) -> int:
#     def length(self) -> int:
# """

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:

        n = mountainArr.length()

        # 1. Find peak
        left, right = 0, n - 1

        while left < right:
            mid = (left + right) // 2

            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1
            else:
                right = mid

        peak = left

        # 2. Binary search increasing part
        left, right = 0, peak

        while left <= right:
            mid = (left + right) // 2
            val = mountainArr.get(mid)

            if val == target:
                return mid
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        # 3. Binary search decreasing part
        left, right = peak + 1, n - 1

        while left <= right:
            mid = (left + right) // 2
            val = mountainArr.get(mid)

            if val == target:
                return mid
            elif val > target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
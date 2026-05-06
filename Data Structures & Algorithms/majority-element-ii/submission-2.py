class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        # Step 1: Find candidates
        cand1 = cand2 = None
        count1 = count2 = 0
        
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = num, 1
            elif count2 == 0:
                cand2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Step 2: Verify counts
        res = []
        for c in [cand1, cand2]:
            if c is not None and nums.count(c) > len(nums) // 3:
                res.append(c)
        
        return res
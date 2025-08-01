#  Solution 1 (General)
# ------------------------------ O(n) TC --------- O(1) SC -----------------
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False


# Solution 2 (fast)
# --------------------------- O(n) avg TC ---------- O(n) SC ----------------

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        n = len(nums)

        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False


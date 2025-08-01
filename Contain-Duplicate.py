#  Solution 1 (General)
# ------------------------------ O(n) TC --------- O(1) SC -----------------
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False


# Solution 2 (fast) + hash set
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


# Solution 3 (using sorting)
# -------------------------- O(n log(n)) TC ------------ O(1) SC --------

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return True
        return False


# Solution 4 ----------- using hash-map
# --------------------------- O(n) TC ------------- O(n) SC --------------

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen and seen[num] >= 1:
                return True
            seen[num] = seen.get(num, 0) + 1
        return False








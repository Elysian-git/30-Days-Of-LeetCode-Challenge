# SOLUTION 1
# ------------------ O(N × (sum(weights) − max(weights))) TC ----------- O(1) SC --------

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        minCap = max(weights)
        maxCap = sum(weights)

        def canShip(cap):
            d = 1
            curr = 0
            for w in weights:
                if curr + w <= cap:
                    curr += w
                else:
                    d += 1
                    curr = w
            return d <= days

        for cap in range(minCap, maxCap + 1):
            if canShip(cap):
                return cap

# SOLUTION 2
# ------------------ O(N∗Log(Sum(Weights))) TC ----------- O(1) SC --------

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canShip(cap):
            sums = 0
            d = 1
            for w in weights:
                if sums+w <= cap:
                    sums += w
                else:
                    d += 1
                    sums = w
            return d <= days
            
        while l <= r:
            cap = (l + r) // 2    # cap == mid
            if canShip(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1
        return res

# SOLUTION 3
# ------------------ O(N∗Log(Sum(Weights))) TC ----------- O(1) SC --------

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canShip(cap):
            d, currCap = 1, cap
            for w in weights:
                if currCap - w < 0:
                    d += 1
                    currCap = cap                   
                currCap -= w
            return d <= days
            
        while l <= r:
            cap = (l + r) // 2    # cap == mid
            if canShip(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1
        return res

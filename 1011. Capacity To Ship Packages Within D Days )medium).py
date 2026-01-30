# SOLUTION 1
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

# SOLUTION 2
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

# Solution 1
# ---------------------- O(len(flowerbed)) TC ----------------- O(1) SC ---------- 

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)

        for i in range(length):
            if n == 0:
                return True

            if (i==0) or flowerbed[i-1]==0:
                if (i==length-1) or flowerbed[length-1]==0:
                    count += 1
                    if count >= n:
                        return True
        return False

# Solution 2
# ----------------------O(len(flowerbed)) TC ----------------- O(1) SC ---------- 

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)

        for i in range(length):
            if n == 0:
                return True

            if ((i==0) or flowerbed[i-1]==0) and ((i==length-1) or flowerbed[length-1]==0):
                count += 1
                if count >= n:
                    return True
        return False

        

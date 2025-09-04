class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        xArrives = 0
        yArrives = 0
        if x > z:
            xArrives = x - z
        else:
            xArrives = z - x

        if y > z:
            yArrives = y - z
        else:
            yArrives = z - y
        
        if yArrives > xArrives:
            return 1
        elif yArrives < xArrives:
            return 2
        else: 
            return 0 
        
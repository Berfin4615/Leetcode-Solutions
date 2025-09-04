class Solution:
    def minDominoRotations(self, tops, bottoms):
        def check(target):
            rot_top = rot_bot = 0
            for a, b in zip(tops, bottoms):
                if a != target and b != target:
                    return float('inf')
                if a != target:
                    rot_top += 1
                if b != target:
                    rot_bot += 1
            return min(rot_top, rot_bot)

        candidates = {tops[0], bottoms[0]}
        ans = min(check(c) for c in candidates)
        return -1 if ans == float('inf') else ans

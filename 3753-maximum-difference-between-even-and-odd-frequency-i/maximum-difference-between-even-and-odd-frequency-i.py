class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        odd_freqs = [f for f in freq.values() if f % 2 == 1]
        even_freqs = [f for f in freq.values() if f % 2 == 0]
        
        if not odd_freqs or not even_freqs:
            return 0
        
        return max(odd_freqs) - min(even_freqs)
            
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()  
        heap = []
        day = 1
        res = 0
        i = 0
        n = len(events)
        max_day = max(e[1] for e in events)  

        for day in range(1, max_day + 1):
            while i < n and events[i][0] == day:
                heapq.heappush(heap, events[i][1])
                i += 1

            while heap and heap[0] < day:
                heapq.heappop(heap)

            if heap:
                heapq.heappop(heap)
                res += 1

        return res
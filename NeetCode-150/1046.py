class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heap = stones 
        heapq.heapify_max(self.heap)
        while len(self.heap) >1: 
            first = heapq.heappop_max(self.heap)
            second = heapq.heappop_max(self.heap)
            if first != second:
                heapq.heappush_max(self.heap, first - second)
        if self.heap:
            return self.heap[0]
        return 0

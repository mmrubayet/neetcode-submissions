class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert to a max-heap using negative values
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            # Pop the two heaviest stones
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            # If they are different, push the remaining weight
            if x != y:
                heapq.heappush(heap, -(x - y))

        # Return the last stone's weight, or 0 if empty
        return -heap[0] if heap else 0

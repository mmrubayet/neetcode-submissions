class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # Move a node down until the max-heap property is restored
        def sift_down(heap, i):
            n = len(heap)

            while True:
                largest = i
                left = 2 * i + 1
                right = 2 * i + 2

                if left < n and heap[left] > heap[largest]:
                    largest = left

                if right < n and heap[right] > heap[largest]:
                    largest = right

                if largest == i:
                    break

                heap[i], heap[largest] = heap[largest], heap[i]
                i = largest

        # Remove and return the maximum element
        def pop_max(heap):
            maximum = heap[0]
            last = heap.pop()

            if heap:
                heap[0] = last
                sift_down(heap, 0)

            return maximum

        # Insert a new element into the max-heap
        def push(heap, value):
            heap.append(value)
            i = len(heap) - 1

            while i > 0:
                parent = (i - 1) // 2

                if heap[parent] >= heap[i]:
                    break

                heap[parent], heap[i] = heap[i], heap[parent]
                i = parent

        # Build max-heap from the input
        heap = stones[:]

        for i in range(len(heap) // 2 - 1, -1, -1):
            sift_down(heap, i)

        # Simulate smashing
        while len(heap) > 1:
            x = pop_max(heap)
            y = pop_max(heap)

            if x != y:
                push(heap, x - y)

        return heap[0] if heap else 0
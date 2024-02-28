class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        adj = collections.defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))
        best = collections.defaultdict(lambda: collections.defaultdict(lambda: float("inf")))
        best[src][K+1] = 0
        min_heap = [(0, src, K+1)]
        while min_heap:
            result, u, k = heapq.heappop(min_heap)
            if k < 0 or best[u][k] < result:
                continue
            if u == dst:
                return result
            for v, w in adj[u]:
                if result+w < best[v][k-1]:
                    best[v][k-1] = result+w                    
                    heapq.heappush(min_heap, (result+w, v, k-1))
        return -1
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        
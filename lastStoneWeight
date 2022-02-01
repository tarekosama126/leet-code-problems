import heapq
def lastStoneWeight(stones) -> int:
    myneglist = [-x for x in stones]
    heapq.heapify(myneglist)
    while len(myneglist) >= 2:
        x = heapq.heappop(myneglist) * -1
        y = heapq.heappop(myneglist) * -1
        heapq.heappush(myneglist, (x - y) * -1)
    return myneglist(0) * -1
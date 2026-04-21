class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        else:
            self.parent[yroot] = xroot
            if self.rank[xroot] == self.rank[yroot]:
                self.rank[xroot] += 1
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        dsu = UnionFind(n:=len(source))
        for a,b in allowedSwaps:
            dsu.union(a,b)
        for i in range(n):
            dsu.find(i)
        groups = defaultdict(list)
        for i in range(n):
            groups[dsu.parent[i]].append(i)
        visited = [False] * n
        dist = n
        for key, val in groups.items():
            idxis = defaultdict(int)
            for idx in val:
                visited[idx] = True
                idxis[source[idx]] += 1
            for idx in val:
                if idxis[target[idx]] > 0:
                    dist -= 1
                    idxis[target[idx]] -= 1
        for i in range(n):
            if not visited[i]:
                dist -= source[i] == target[i]
        return dist


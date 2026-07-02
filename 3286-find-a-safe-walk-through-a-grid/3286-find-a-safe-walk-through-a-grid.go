func findSafeWalk(grid [][]int, health int) bool {
	m, n := len(grid), len(grid[0])
	dis := make([][]int, m)
	for i := range dis {
		dis[i] = make([]int, n)
		for j := range dis[i] {
			dis[i][j] = -1
		}
	}
	dirs := [4][2]int{{0, 1}, {1, 0}, {-1, 0}, {0, -1}}

	pq := &MinHeap{}
	heap.Push(pq, Item{val: grid[0][0], x: 0, y: 0})
	for pq.Len() > 0 {
		cur := heap.Pop(pq).(Item)
		if dis[cur.x][cur.y] >= 0 {
			continue
		}
		dis[cur.x][cur.y] = cur.val
		for _, d := range dirs {
			nx, ny := cur.x+d[0], cur.y+d[1]
			if nx < 0 || ny < 0 || nx >= m || ny >= n || dis[nx][ny] >= 0 {
				continue
			}
			heap.Push(pq, Item{val: cur.val + grid[nx][ny], x: nx, y: ny})
		}
	}
	return dis[m-1][n-1] < health
}

type Item struct {
	val, x, y int
}
type MinHeap []Item

func (h MinHeap) Len() int            { return len(h) }
func (h MinHeap) Less(i, j int) bool  { return h[i].val < h[j].val }
func (h MinHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *MinHeap) Push(x interface{}) { *h = append(*h, x.(Item)) }

func (h *MinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}
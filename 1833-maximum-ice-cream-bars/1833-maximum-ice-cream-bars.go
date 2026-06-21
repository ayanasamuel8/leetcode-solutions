func maxIceCream(costs []int, coins int) int {
    slices.Sort(costs)
    used := 0
    i := 0
    n := len(costs)
    for i < n && used + costs[i] <= coins{
        used += costs[i]
        i += 1
    }
    return i
}
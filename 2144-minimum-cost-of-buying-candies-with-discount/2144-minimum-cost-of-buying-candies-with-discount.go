func minimumCost(cost []int) int {
    sort.Ints(cost)
    total := 0
    
    for len(cost) > 0 {
        total += cost[len(cost)-1]
        cost = cost[:len(cost)-1]
        
        if len(cost) > 0 {
            total += cost[len(cost)-1]
            cost = cost[:len(cost)-1]
        }
        
        if len(cost) > 0 {
            cost = cost[:len(cost)-1]
        }
    }
    return total
}
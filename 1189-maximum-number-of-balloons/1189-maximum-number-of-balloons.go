func maxNumberOfBalloons(text string) int {
    cntr := map[rune]int{
        'b': 0,
        'a': 0,
        'l': 0,
        'o': 0,
        'n': 0,
    }
    
    for _, val := range text {
        if _, ok := cntr[val]; ok {
            cntr[val]++
        }
    }
    
    cntr['l'] /= 2
    cntr['o'] /= 2
    
    min := cntr['b']
    for _, count := range cntr {
        if count < min {
            min = count
        }
    }
    
    return min
}
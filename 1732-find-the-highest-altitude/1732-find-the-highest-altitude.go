func largestAltitude(gain []int) int {
    var curr int = 0
    var max int = 0
    for _, v := range gain{
        curr += v
        max = int(math.Max(float64(max), float64(curr)))
    }
    return max
}
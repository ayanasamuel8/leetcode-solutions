func minElement(nums []int) int {
    var minnum int = math.MaxInt
    for _, v := range nums{
        minnum = min(minnum, digit_sum(v))
    }
    return minnum
}
func digit_sum(num int) int{
    var total int = 0
    for num > 0{
        total += num %10
        num /= 10
    }
    return total
}
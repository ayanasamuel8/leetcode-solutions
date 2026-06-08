func pivotArray(nums []int, pivot int) []int {
    less := []int{}
    greater := []int{}
    cnt := 0
    for _, v := range nums{
        if v < pivot{
            less = append(less, v)
        }else if v > pivot{
            greater = append(greater, v)
        }else{
            cnt += 1
        }
    }
    for i := 0; i < cnt; i++ {
        less = append(less, pivot)
    }
    return append(less, greater...)
}
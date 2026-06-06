func leftRightDifference(nums []int) []int {
    n := len(nums)
    var ans []int
    for i := 0; i < n; i++{
        leftsum := 0
        for j := 0; j < i; j++{
            leftsum += nums[j]
        }
        rightsum := 0
        for j := i + 1; j < n; j++{
            rightsum += nums[j]
        }
        diff := int(math.Abs(float64(leftsum - rightsum)))
		ans = append(ans, diff)
    }
    return ans
}
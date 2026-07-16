import (
	"slices"
)
func gcdSum(nums []int) int64 {
    var max int64 = int64(nums[0])
    var pref []int64
    for i := 0; i < len(nums); i++{
        max = int64(math.Max(float64(max), float64(nums[i])))
        pref = append(pref, gcd(max, int64(nums[i])))
    }
    slices.Sort(pref)
    left := 0
    right := len(pref) - 1
    var ans []int64
    for left < right{
        ans = append(ans, gcd(pref[left], pref[right]))
        left += 1
        right -= 1
    }
    return Sum(ans)
}

func gcd(a int64, b int64) int64 {
    if (b == 0){
        return a
    }
    return gcd(b, a % b)
}

func Sum(numbers []int64) int64 {
	var total int64 = 0
	for _, num := range numbers {
		total += num
	}
	return total
}

func findKthSmallest(coins []int, k int) int64 {
	sort.Ints(coins)
	n := len(coins)
	m := 1 << n

	l := int64(k)
	r := int64(coins[0])*int64(k) + 1

	bitCount := make([]int, m)
	lcm := make([]int64, m)

	for mask := 1; mask < m; mask++ {
		curLcm := int64(1)
		for i, coin := range coins {
			if mask>>i&1 == 1 {
				g := gcd(curLcm, int64(coin))
				tmp := curLcm / g

				if tmp <= r/int64(coin) {
					curLcm = tmp * int64(coin)
				} else {
					curLcm = r + 1
					break
				}
				bitCount[mask]++
			}
		}
		lcm[mask] = curLcm
	}

	count := func(x int64) int64 {
		var res int64 = 0
		for mask := 1; mask < m; mask++ {
			if lcm[mask] > x {
				continue
			}
			if bitCount[mask]&1 == 1 {
				res += x / lcm[mask]
			} else {
				res -= x / lcm[mask]
			}
		}
		return res
	}

	for l < r {
		x := l + (r-l)/2
		if count(x) >= int64(k) {
			r = x
		} else {
			l = x + 1
		}
	}
	return l
}

func gcd(a, b int64) int64 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
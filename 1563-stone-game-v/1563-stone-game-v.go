func stoneGameV(stoneValue []int) int {
	n := len(stoneValue)
	f := make([][]int, n)
	for i := range f {
		f[i] = make([]int, n)
	}

	var dfs func(left, right int) int
	dfs = func(left, right int) int {
		if left == right {
			return 0
		}
		if f[left][right] != 0 {
			return f[left][right]
		}

		sum := 0
		for i := left; i <= right; i++ {
			sum += stoneValue[i]
		}
		suml := 0
		for i := left; i < right; i++ {
			suml += stoneValue[i]
			sumr := sum - suml
			if suml < sumr {
				val := dfs(left, i) + suml
				if val > f[left][right] {
					f[left][right] = val
				}
			} else if suml > sumr {
				val := dfs(i+1, right) + sumr
				if val > f[left][right] {
					f[left][right] = val
				}
			} else {
				val := max(dfs(left, i), dfs(i+1, right)) + suml
				if val > f[left][right] {
					f[left][right] = val
				}
			}
		}
		return f[left][right]
	}

	return dfs(0, n-1)
}
func smallestNumber(n int, t int) int {
	check := func(num int) bool {
		product := 1
		for num > 0 {
			product *= num % 10
			num /= 10
			if product == 0 {
				break
			}
		}
		return product%t == 0
	}
	for !check(n) {
		n++
	}
	return n
}
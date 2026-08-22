func prod(n int) int {
	if n == 0 {
		return 0
	}
	
	product := 1
	if n < 0 {
		n = -n
	}

	for n > 0 {
		digit := n % 10
		product *= digit
		n /= 10
	}
	return product
}

func sum(n int) int {
	total := 0
	if n < 0 {
		n = -n
	}

	for n > 0 {
		digit := n % 10
		total += digit
		n /= 10
	}
	return total
}

func checkDivisibility(n int) bool {
	p := prod(n)
	s := sum(n)

	divisible := (p != 0 || s != 0) && n%(p + s) == 0

	return divisible
}
func gcdOfOddEvenSums(n int) int {
	var gcd func(int, int) int
	gcd = func(x, y int) int {
		if y == 0 {
			return x
		}
		return gcd(y, x%y)
	}
	return gcd(n*n, n*(n+1))
}
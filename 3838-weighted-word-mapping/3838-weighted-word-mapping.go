func mapWordWeights(words []string, weights []int) string {
    s := "zyxwvutsrqponmlkjihgfedcba"
    ans := []rune{}

    for _, word:=range words{
        tot := 0
        for _, ch:=range word{
            tot += weights[int(ch) - 97]
        }
        ans = append(ans, rune(s[(tot % 26)]))
    }
    return string(ans)
}
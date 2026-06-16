func processStr(s string) string {
    var stack []rune
    for _, v:= range s{
        if unicode.IsLetter(v){
            stack = append(stack, v)
        }else if v == '*'{
            if len(stack) > 0{
                stack = stack[:len(stack)-1]
            }
        }else if v == '#'{
            stack = append(stack, stack...)
        }else{
            stack = reverse(stack)
        }
    }
    return string(stack)
}

func reverse(s []rune) []rune{
    var rev []rune
    n := len(s)
    for i := n - 1; i >= 0; i--{
        rev = append(rev, s[i])
    }
    return rev
}
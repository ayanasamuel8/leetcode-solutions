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
            slices.Reverse(stack)
        }
    }
    return string(stack)
}

func asteroidsDestroyed(mass int, asteroids []int) bool {
    sort.Ints(asteroids)
    for _, v:= range asteroids{
        if (mass < v){
            return false
        }else{
            mass += v
        }
    }
    return true
}
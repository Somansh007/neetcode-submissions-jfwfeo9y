func countSubstrings(s string) int {
    res := 0
    for i := range s {
        for j := i; j < len(s); j++ {
            l, r := i, j
            for l < r && s[l] == s[r] {
                l++
                r--
            }
            if l >= r {
                res++
            }
        }
    }
    return res
}
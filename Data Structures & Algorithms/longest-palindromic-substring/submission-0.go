func longestPalindrome(s string) string {
    res := ""
    resLen := 0

    for i := 0; i < len(s); i++ {
        for j := i; j < len(s); j++ {
            l, r := i, j
            for l < r && s[l] == s[r] {
                l++
                r--
            }

            if l >= r && resLen < (j-i+1) {
                res = s[i : j+1]
                resLen = j - i + 1
            }
        }
    }

    return res
}
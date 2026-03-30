func numDecodings(s string) int {
    return dfs(s, 0)
}

func dfs(s string, i int) int {
    if i == len(s) {
        return 1
    }
    if s[i] == '0' {
        return 0
    }
    res := dfs(s, i+1)
    if i < len(s)-1 {
        if s[i] == '1' || (s[i] == '2' && s[i+1] < '7') {
            res += dfs(s, i+2)
        }
    }
    return res
}
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)

        if s[-1] == '1':
            return False

        reachable = [False] * n
        reachable[0] = True

        pre = 0

        for i in range(1, n):
            # add new reachable position into window
            if i - minJump >= 0 and reachable[i - minJump]:
                pre += 1

            # remove position leaving window
            if i - maxJump - 1 >= 0 and reachable[i - maxJump - 1]:
                pre -= 1

            # current index is reachable
            if pre > 0 and s[i] == '0':
                reachable[i] = True

        return reachable[-1]
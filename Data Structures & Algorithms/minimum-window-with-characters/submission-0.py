class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        tCount, sCount = defaultdict(int), defaultdict(int)
        res = [0, 0]
        minLength = float("inf")

        for c in t:
            tCount[c] += 1

        l, have, need = 0, 0, len(tCount)

        for r in range(len(s)):
            sCount[s[r]] += 1

            if s[r] in tCount and sCount[s[r]] == tCount[s[r]]:
                have += 1

            while have == need:
                if (r - l  + 1) < minLength:
                    res = [l, r]
                    minLength = r - l + 1

                sCount[s[l]] -= 1
                if s[l] in tCount and sCount[s[l]] < tCount[s[l]]:
                    have -= 1

                l += 1

        l, r = res

        return s[l : r + 1] if minLength != float("inf") else ""
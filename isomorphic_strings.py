class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dps = {}
        dpt = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            ss = s[i]
            tt = t[i]
            if s[i] not in dps:
                dps[ss] = tt
            if t[i] not in dpt:
                dpt[tt] = ss
            if dps[ss] != tt or dpt[tt] != ss:
                return False
        return True
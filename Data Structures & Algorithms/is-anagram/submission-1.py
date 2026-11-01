class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sl = list(s)
        tl = list(t)
        sl.sort()
        tl.sort()
        if len(sl) != len(tl):
            return False
        for i in range(len(sl)):
            if sl[i] != tl[i]:
                return False
        return True
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_a = []
        t_a = []
        for n in range(len(s)):
            s_a.append(s[n])
        for n in range(len(t)):
            t_a.append(t[n])
        s_a.sort()
        t_a.sort()
        if s_a == t_a:
            return True
        return False

        
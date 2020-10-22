class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0 # 熊孩子
        j = 0 # 小饼干
        flag = 0
        while i < len(g) and j<len(s):
            if g[i] <= s[j]:
                i+=1
                j+=1
                flag+=1
            else:
                j+=1
        return flag
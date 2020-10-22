# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         _flag = 0
#         _cur = 0
#         _res = 0
#         _temp = {}
#         _data = list(s)
#         while _cur < len(_data):
#             if _data[_cur] in _temp:
#                 _cur = _temp[_data[_cur]]
#                 _temp = {}
#                 _flag = 0
#             else:
#                 _temp[_data[_cur]] = _cur
#                 _flag += 1
#             if _res < _flag:
#                 _res = _flag
#             _cur += 1
#
#         return _res

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 使用一个辅助变量来暂时存储匹配的子串
        ans = ''
        tep = ''
        for i in s:
            # 遍历，若不重复则记录该字符
            if i not in tep:
                tep += i
            # 如果遇到了已经存在的字符，则找到该字符所在位置，删除该字符，并保留该位置之后的子串，并把当前字符加入到最后，完成更新
            else:
                tep = tep[tep.index(i)+1:]
                tep += i
            # 如果是当前最长的，就替换掉之前存储的最长子串
            if len(tep) > len(ans):
                    ans = tep
        return len(ans)



_d = Solution()
print(_d.lengthOfLongestSubstring(' '))
print(_d.lengthOfLongestSubstring('abcabcbb'))
print(_d.lengthOfLongestSubstring('bbbbbb'))
print(_d.lengthOfLongestSubstring('pwwkew'))
print(_d.lengthOfLongestSubstring('dvdf'))

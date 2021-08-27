"""
557. 反转字符串中的单词 III
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。



示例：

输入："Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc"


提示：

在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
"""

class Solution:
    def reverse(self, s):
        start = 0
        end = len(s) - 1
        result = ""
        while start <= end:
            result += s[end]
            end -= 1
        return result


    def reverseWords(self, s: str) -> str:
        words = s.split()
        i = 0
        while i < len(words):
            words[i] = self.reverse(words[i])
            i += 1
        return " ".join(words)
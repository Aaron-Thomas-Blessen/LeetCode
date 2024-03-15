# -*- coding: utf-8 -*-
"""14. Longest Common Prefix.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U2ULU9_jvWPeiKp8OBcoQ_6vsZY5F00D
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sum=""
        strs=sorted(strs)
        for i in range(min(len(strs[0]),len(strs[-1]))):
            if (strs[0][i]!=strs[-1][i]):
                return sum
            sum=sum+strs[0][i]
        return sum
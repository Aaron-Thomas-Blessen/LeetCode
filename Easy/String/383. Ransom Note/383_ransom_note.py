# -*- coding: utf-8 -*-
"""383. Ransom Note.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17K-88XTlEqFDYaZ-OQNeDJXEI_F_q9AY
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ret = True
        for i in ransomNote:
            if i in magazine:
                magazine = magazine.replace(i, '', 1)
            else:
                ret = False

        return ret
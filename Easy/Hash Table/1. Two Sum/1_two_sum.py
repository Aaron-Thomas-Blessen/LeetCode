# -*- coding: utf-8 -*-
"""1. Two Sum.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dxoAg1iKfCVMlcOtR6_qtqxiMU2RSUMw
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum=0
        result=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j] == target):
                    result.append(i)
                    result.append(j)
                    break
        return result
# -*- coding: utf-8 -*-
"""412. Fizz Buzz.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CVF7rFOiaTKUtp_3aUNBjs7MvlpgjpRF
"""

from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result=[]
        for i in range(1,n+1):
            if(i%3 == 0):
                if(i%5 == 0):
                    result.append("FizzBuzz")
                else:
                    result.append("Fizz")
            else:
                if(i%5 == 0):
                    result.append("Buzz")
                else:
                    result.append(str(i))
        return result

s=Solution()
s.fizzBuzz(15)


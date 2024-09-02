class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if(digits.count(9)==len(digits)):
            digits=[0]*(len(digits)+1)
            digits[0]=1
        else:
            shift=1
            for i in range(len(digits)-1,-1,-1):
                x=digits[i]+shift
                digits[i]=x%10
                shift=x//10
        return digits

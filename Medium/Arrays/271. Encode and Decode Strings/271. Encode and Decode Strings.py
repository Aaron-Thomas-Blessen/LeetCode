class Solution:

    def encode(self, strs: List[str]) -> str:
        string=""
        for i in strs:
            string+=i
            string+=";"
        return string

    def decode(self, s: str) -> List[str]:
        strin=""
        listy=[]
        for i in s:
            if(i == ";"):
                listy.append(strin)
                strin=""
            else:
                strin+=i
        return listy

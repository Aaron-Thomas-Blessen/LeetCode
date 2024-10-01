# given a target value target
# Find which 2 index adds up to the target
# array = [2,4,5,3]; target = 6
# output = [0,1]


array=[]
output=[]
target=int(input("enter target"))
n=int(input("Enter n"))

print("Enter values")
for i in range(n):
    x=int(input("Enter value"))
    array.append(x)

flag=False

for i in range(len(array)):
    rest = target-array[i]
    if rest in array:
        index = array.index(rest)
        output.append(i)
        output.append(index)
        flag=True
        break
    else:
        continue
if flag:
    print(output)
else:
    print(-1)
        
        
    

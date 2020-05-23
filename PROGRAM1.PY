tup=tuple(map(int,input().split(" ")))
n=int(input("Enter number"))
count=0
for i in tup: 
        if (i == n): 
            count = count + 1
print(count)            
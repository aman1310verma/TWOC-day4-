d={}
n=int(input("Enter the range"))
d = [ map(int,input().split()) for x in range(n)]
max=max(d)
max2=0
for i in d:
    if i>max2 and v<max:
        max2=v
print("second Largest is:",max2)            


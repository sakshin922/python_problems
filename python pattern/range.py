n=int(input("enter any number"))
for i in range(n,0,-1):
    for j in range(i,i+1):
        print(j,end=" ")
    print()
for i in range(0,5):
    for j in range(0,5):
        print("*",end="")
    print()

for i in range(0,5):
    for j in range(0,i):
        print("*",end="")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(i,end="")
    print()

for i in range(0,5):
    for j in range(0,5-i):
        print("*",end="")
    print()

for i in range(1,6):
    for j in range(1,6-i+1):
        print(j,end="")
    print()

for i in range(1,6):
    for j in range(1,5-i+1):
        print(" ",end="")
    for k in range(1,2*i):
        print("*",end="")
    for l in range(1,5-i+1):
        print(" ",end="")
    print()

for i in range(0,5):
    for j in range(0,i):
        print(" ",end="")
    for k in range(0,(2*5-(2*i+1))):
        print("*",end="")
    for l in range(0,i):
        print(" ",end="")
    print()


for i in range(0,5):
    for j in range(0,i+1):
        print("*",end="")
    print()
for i in range(0,4):
    for j in range(0,4-i):
        print("*",end="")
    print()

for i in range(0,5):
    for j in range(0,i+1):
        if (i+j)%2==0:
            print("1 ",end="")
        else:
            print("0 ",end="")
    print()

for i in range(1,5):
    for j in range(1,i+1):
        print(j,end="")
    for k in range(1,5-i):
        print(" ",end="")
    for k in range(1,5-i):
        print(" ",end="")
    for l in range(i,0,-1):
        print(l,end="")
    print()

n=1
for i in range(1,6):
    for j in range(1,i+1):
        print(n," ",end="")
        n+=1
    print()
    

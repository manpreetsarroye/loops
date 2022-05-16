
n= int(input("Please Enter the no : "))

i = 0
while i <= n:
    j=0
    k=0
    while j <=i:
        print(k*i, end = '  ')
        k=k+1
        j=j+1
        
    i = i + 1
    print()
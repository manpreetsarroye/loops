# rows = int(input("Enter the number of rows: "))    
# for i in range(rows + 1, 0, -1):    
#     for j in range(0, i - 1):  
#         print(, end=' ')  
#     print(" ")


i=5
while i>=1:
    j=5
    while j>=i:
        print(j,end=" ")
        j-=1
    print()
    i-=1



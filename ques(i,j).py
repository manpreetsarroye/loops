
# a = int(input("Please Enter the Total Number of Rows  : "))

# i = 1
# while(i <= a):
#     j = 1
#     while(j <= a):
#         if(j <= a - i):
#             print(' ', end = '  ')
#         else:
#             print(j, end = '  ')
#         j = j + 1
#     i = i + 1
#     print()



r=1
while r<=5:
    c=1
    while c<=5-r:
        print(' ', end = '  ')
        c=c+1
    j=r
    while r<=1:
        print(j, end = '  ')
        j=j+1
    print()
r=r+1
    

rows = 6
i=1
while i<=rows:
    b= 1
    j=6
    while j>=1:
        if j > i:
            print(b, end=' ')
            b  += 1
        j-=1
    i+=1
    print("")
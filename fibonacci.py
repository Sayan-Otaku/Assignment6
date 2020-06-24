n=int(input("Enter the number of fibonacci numbers you want: - "))
a,b=0,1
print("\n{}\t{}".format(a,b),end=" ")
for i in range(n-2):
    c=a+b
    print("\t{}".format(c),end=" ")
    a=b
    b=c

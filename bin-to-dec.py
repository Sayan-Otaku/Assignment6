binary=input("Enter a binary number: - ")
l=len(binary)
p=0
dec=0
for i in range(l-1,-1,-1):
    k=int(binary[i])
    dec=dec+(k*pow(2,p))
    p+=1
    k=0
print("\nDecimal equivalent of {} = {}".format(binary,dec))
    


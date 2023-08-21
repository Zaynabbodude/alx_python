for number in range(100):
    print("{:02}".format(number),end=", ") 

lst=[]
i=00
while i<=99:
    lst.append(str(i))
    i=i+1  
print(', '.join(lst))
   
n=int(input("entre the size of the arrays:"))
print("the first array :")
tab1=[]
for i in range(n):
    b=int(input("entre the numbre : "))
    tab1.append(b)
print("the second array :")
tab2=[]
for i in range(n):
    a=int(input("entre the numbre : "))
    tab2.append(a)
tab=[]
for i in range(n):
    sum=tab1[i]+tab2[i]
    tab.append(sum)

print("the sum is:",tab)




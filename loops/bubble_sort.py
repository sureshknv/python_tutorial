import sys
a=[]
i=0
for x in raw_input().split() :
    a.append(int(x))
#    print a[i]
    i+=1
i=0
j=0
for i in range(len(a)) :
    j=i 
    temp=a[i]
    while  j>0 and temp<a[j-1] :
        a[j]=a[j-1]
        j-=1
    a[j]=temp
    i+=1
i=0
for i in range(len(a)) :
    print a[i]
    i+=1

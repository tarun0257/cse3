#for finding duplicate numbers 
count=0
l1=[1,1,2,2,3,3,4,4,4,4,5,5]
for i in range(0,len(l1)-1):
      if l1[li]==l1[i+1]:
          count=count+1
print(count)

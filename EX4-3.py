x = int(input())
num=[]             
for i in range(2,x+1):
   for j in range(2,i):
      if(i%j==0):
         break
   else:
      num.append(i)
print(max(num))
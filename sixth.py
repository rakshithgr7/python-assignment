
def gens(n):
    i=0
    while i<=n:
        
        if i % 7 == 0 and i % 5 == 0:
         yield i
        i=i+1
        
        
print("please enter the value of n ")
n=input()
n=int(n)
gens(n)      

for value in gens(n):
  print(value,sep=',')
    


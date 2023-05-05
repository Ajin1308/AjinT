Limit = int(input("Fibonacci sequence Between 0 and: "))

n1, n2 = 1, 1

if Limit <= 0:
   print("Please enter a positive integer")

elif Limit == 1:
   print("Fibonacci sequence upto",Limit,":")
   print(n1)

else:
   print("Fibonacci sequence upto",Limit,":")
   while n1 < Limit:
       print(n1)
       n1,n2=n2,n1+n2
   
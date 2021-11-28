n=int(input("enter the number"))
s=0;
t=n;
while(n>0):
    r=n%10;
    s=s+(r*r*r);
    n=n//10;

if(t==s):
    print("armstrong number");
else:
    print("not a armstrong number");
    
 

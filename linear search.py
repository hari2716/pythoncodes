
list1=[1,2,3,4,5]
key=int(input("enter the key number"))
flag=0
for i in range (len(list1)):
 if key==list1[i]:
  flag=1
  print("key found")
  break
else:
    print("key not found")

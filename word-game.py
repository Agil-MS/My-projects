print("****----WORD GAME----****")
a=25
n=input("Enter the Name ")
i=0
x=0

while i<a:
    print("*")
    i+=1
mylist=[]
l=len(n)
while x<l:
    mylist.append("_")
    x+=1
c=''.join(mylist)
print(c)
s=list(n)

i=0
true=0
z=l+3
while i<l+3:
    print("Number of chances=",z)
    b=input("\nEnter the letter ")
    if b in s:
        index=s.index(b)
        #mylist[index]=b
        e=''.join(mylist)
        print("~~~~~~Character is correct~~~~~~~")
        print(e)
        true+=1
        z-=1
        s[index]=[]
        i=i+1
        if true==l:
            print("\n\n\n----~~~~~~All characters are correct~~~~~~~~~-----")
            print("\n\nThe word is=",e)
            print("\n\n\n")
            break
    else:
        print("\n~~~~~~~Incorrect, try again~~~~~~~~")
        z-=1
        #print("Number of chances=",z)
        e=''.join(mylist)
        print(e)
        i+=1
if true!=l:
    print("\n~~~~~~~~~Game over~~~~~~~~~~~")
    print("\n\n\n")
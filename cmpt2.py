def cmpa(a,b,c):
    if(a>b and a>c):
        print(f"{a} is greatest")
    elif(b>c):
        print(f"{b} is greatest")
    else:
        print(f"{c} is greatest")

e=input("Enter the 1st number: ")
f=input("Enter the 2nd number: ")
g=input("Enter the 3rd number: ")
cmpa(e,f,g)

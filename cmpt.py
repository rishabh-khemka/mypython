def cmpa(a,b,c):
    if(a>b):
        if(a>c):
            print(f"{a}is greatest")
        else:
            print("{} is greatest".format(c))
    else:
        if(b>c):
            print("{} is greatest".format(b))
        else:
            print("{} is greatest".format(c))


e=input("enter the value of a: ")
f=input("enter the value of b: ")
g=input("enter the value of c: ")

cmpa(e,f,g)

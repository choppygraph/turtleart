x=float(input("What is your items percentage number?"))
b=1//x+1
print("It will take ",1//x+1,"crates to get your item\n")
c=input("Is your crate special or regular?")
if c==("special"):
    print("The wave you will need to get to is ",(3*b*5)+15," ")
elif c==("regular"):
    print("The wave you will need to get to",(2*b*5)," ")
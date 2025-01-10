import random
randval= random.randint(0,100)

userinput = int(input("Please give me a number: "))

while userinput != randval:
    if userinput > (randval) and userinput < (randval + 10):
        print("Too big")
    else:
        if userinput < (randval) and userinput > randval - 10:
            print("Too small")
    if userinput >= (randval + 10):
            print("Way too big")
    else:
        if userinput <= randval - 10:
            print("Way too small")
    userinput = int(input("please give me a number: "))

if randval == userinput:
    print("Correct!")

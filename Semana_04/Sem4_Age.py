name = input("Type your name: ")
age = int(input(f"Hello {name}, What's your age? "))

if(age <= 4):
    print(name,"you are a baby")

elif(age <= 9):
    print(name,"you are a kid")

elif(age <= 12):
    print(name,"you are a preteenager")

elif(age <= 17):
    print(name,"you are a teenager")

elif(age <= 29):
    print(name,"you are a young adult")

elif(age <= 64):
    print(name,"you are an adult")

else:
    print(name,"you are an elder")

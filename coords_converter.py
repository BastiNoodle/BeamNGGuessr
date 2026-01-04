count = 1
while True:
    print("-------")
    x = int(input("x: "))
    y = int(input("y: "))
    xn = x
    yn = y
    yn = yn * -1
    print("[",yn,",",xn,",","\"",count,".png\"],", sep="")
    count = count + 1
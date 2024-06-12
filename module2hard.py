def tstDef(n):
    rez=''
    if n>3:
        if n<20:
            for i in range(1,n):
                for j in range(i+1,n-i+1):
                    if n%(i+j)==0:
                        rez=rez+str(i)+str(j)
        else:
            print("меньше 20")
    else:
        print("больше 3")
    return (rez)

x=int(input("Число "))

print(tstDef(x))
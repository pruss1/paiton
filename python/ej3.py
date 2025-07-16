n=int(input("ingrese n del 1 al 10"))
m=int(input("ingrese m del 1 al 10"))
try:
    if 1<=n<=10 and 1<=m<=10:
        archivo=open("tabla-n.txt","w")
        for i in range(1, 11):
            archivo.write(f"{n}x{i}={n*i}\n")
        archivo.close()
        archivo=open("tabla-n.txt")
        l=archivo.readlines()
        print(l[m-1])
        archivo.close()
    else:
        print("lelelel")
except IOError:
    print("oooooooo")

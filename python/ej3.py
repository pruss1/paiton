n=int(input("ingrese n del 1 al 10"))
m=int(input("ingrese m del 1 al 10"))
try:
    archivo=open("tabla-n.txt","w")
    for i in range(1,11):
        archivo.write(f"{n}x{i}={n*i}\n")
    archivo.close()
    archivo=open("tabla-n.txt")
    l=archivo.readlines()
    print(l[m-1])
    archivo.close()
except IOError:
    print("oooooooo")
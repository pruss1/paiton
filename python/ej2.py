print("ingrese n del 1 al 10")
n=int(input())
try:
    if 1<=n<=10:
        archivo=open(f"tabla-n.txt","w")
        for i in range(1,11):
            linea=f"{n}x{i}={n*i}"
            archivo.write(linea)
            print(linea)
        archivo.close()
    else:
        print("eee")
except IOError:
    print("oooooooo")
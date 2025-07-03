print("ingrese n del 1 al 10")
n=int(input())
if 1<=n<=10:
    archivo=open("tabla-n.txt","w")
    for i in range(1,11):
        linea=f"{n}x{i}={n * i}\n"
        archivo.write(linea)
    archivo.close()
else:
    print("eee")
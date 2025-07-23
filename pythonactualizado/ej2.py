def ej2():
    print("ingrese n del 1 al 10")
    n=int(input())
    try:
        if 1<=n<=10:
            archivo=open(f"tabla-{n}.txt","r")
            print(archivo.read())
            archivo.close()
        else:
            print("eee")
    except IOError:
        print("oooooooo")
ej2()
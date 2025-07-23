def ej3():
    n=int(input("ingrese n de la tabla del 1 al 10:"))
    m=int(input("ingrese m(fila de la tabla) del 1 al 10:"))
    try:
        if 1<=n<=10 and 1<=m<=10:
            archivo=open(f"tabla-{n}.txt","r")
            l=archivo.readlines()
            print(l[m-1])
            archivo.close()
        else:
            print("lelelel")
    except IOError:
        print("oooooooo")
ej3()
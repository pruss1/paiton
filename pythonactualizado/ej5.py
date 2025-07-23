def ej5():
    try:
        archivo=open("pib.csv","r")
        codigo=input("escribi las iniciales del pais:").strip().upper()
        campo=archivo.readline().strip().split(",")
        for linea in archivo:
            datos=linea.strip().split(",")
            if datos[1].upper()==codigo:
                print(f"PIB per capita de {datos[0]}:")
                for i in range(2,len(datos)):
                    print(campo[i],datos[i])
        archivo.close()
    except IOError:
        print("error")
ej5()
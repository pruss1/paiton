def ej6():
    import csv
    f=open("cotizacion.csv")
    lector=csv.reader(f, delimiter=",", quotechar='"')
    filas=list(lector)
    f.close()
    titulos=filas[0]
    datos={}
    for columna in titulos:
        datos[columna]=[]
    for fila in filas[1:]:
        for i in range(len(titulos)):
            datos[titulos[i]].append(fila[i])
    salida=open("fichero.txt", "w")
    salida.write("columna;min;max;media\n")

    for nombre in datos:
        numeros=[]
        for valor in datos[nombre]:
            try:
                valor=valor.replace(".","").replace(",",".").replace('"',"")
                numeros.append(float(valor))
            except:
                print("")
        if numeros:
            minimo=min(numeros)
            maximo=max(numeros)
            media=sum(numeros)/len(numeros)
            salida.write(f"{nombre};{minimo};{maximo};{media}\n")
    salida.close()
ej6()
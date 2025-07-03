import urllib.request
url=input("ingresa url:")
respuesta=urllib.request.urlopen(url)
datos=respuesta.read()
texto=datos.decode("utf-8")
palabras=texto.split()
print("hay", len(palabras),"palabras")
from io import open

mi_archivo=open("regi.txt","a+")  
soloTexto="17-08-2022"
mi_archivo.write(soloTexto)
mi_archivo.close()
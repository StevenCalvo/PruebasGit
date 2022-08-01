"""Cree un algoritmo, que le permita crear el aumento de los empleados dependiendo del 
departamento. Se debe imprimir una tabla con los datos de los empleados, el valor del 
aumento y el monto final después del aumento. Por último debe imprimir el valor total de la 
planilla antes del aumento, el valor total de los aumentos y la totalidad de la planilla al aplicar 
los aumentos"""
from ast import Index
aumento1=0.0232
aumento2=0.0203
aumento3=0.0173
h=0
fg=0
nombre=[]
area=[]
aumentos=[]
areasocios={}
areaadministrativo={}
areaoperativos={}

id=["6564045883","828613192","1855107112","1602426694","9214272107","2638542857","4160695396","6848447102","6795405079","1377375633","2097476031","5515500717","2216847585","1227435568","4999253399","6588423799","5556458995","5372980370","660062178","5175494899","8786387499","5208261014","9450511055","6748073685","6177508367","8264795072","6738682883","6198718611","956945171","5245421879","4281506489","6835544449"]
Nombres=["lindi","abram","salomi","estel","kathlin","adina","raeann","bentlee","danella","jenine","davon","carlene","manon","robinett","krissy","whit","trev","zeb","tobie","veronica","val","brenn","peg","ania","cleopatra","corney","glenine","jessamyn","chantalle","montague","zora","jaclyn"]
apellidos=["Leithgoe","Dobney","Pinckstone","Fehners","Deary","Crumbleholme","Kovacs","Davion","veronique","doerffer","vowells","baughn","carletto","copland","bringloe","armell","deppe","jacobsohn","maggorini","shier","morilla","davsley","lawless","arrigucci","battersby","karlolczak","robken","nairns","kubyszek","wagenen","glasbey","colisbe"]
departamento=["operativos","administrativos","socios","operativos","administrativos","operativos","administrativos","socios","administrativos","operativos","administrativos","socios","administrativos","operativos","socios","administrativos","operativos","socios","administrativos","operativos","socios","operativos","administrativos","socios","operativos","administrativos","operativos","Administrativos","Socios","administrativos","operativos","administrativos"]
salarios=[551690,431298,795406,890987,1160645,1000154,652182,1131439,391010,1113810,437702,771209,938783,410205,664115,440158,1066497,645260,1135481,419851,1128536,530349,837626,529910,512743,1132685,1085963,798176,742414,895712,872395,1125305]
print("\n" "*********************************Empresa chapulin******************************" "\n")

def impresion ():
    print("Cedúla""        ""Nombre""             "" Apellidos""          "" Departamento""           ""Salario""\n")
    for a,b,c,d,e in zip(id,Nombres,apellidos,departamento,salarios):
      print(a,"\t",b,"\t",c,"\t",d,"\t",e)     

impresion()

def resolucion ():
    for f in nombre:
        print(id[Nombres.index(f)],Nombres[Nombres.index(f)],apellidos[Nombres.index(f)],departamento[Nombres.index(f)],salarios[Nombres.index(f)])

resolucion()

def aument_salario():
    areasocios["socios"]=

aument_salario()

while h==fg:
    print("**********************************************************************************")
    nombre+=[input(" Cuál es el nombre ")]
    area+=[input(" Es salario es ")]
    print("**********************************************************************************")
    desicion=input(" Desea continuar si/no ")
    if desicion == "no":
        fg=1
resolucion()
aument_salario()






    







    

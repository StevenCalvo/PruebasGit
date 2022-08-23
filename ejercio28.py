class auto:
    marca="Toyota"

    def _int_(self,color,modelo):
        print(color,modelo)

        self.color=color
        self.modelo=modelo
        

    def avance(self,distancia):
        print("Avanza: ",distancia, " metros")

mi_auto=auto("Rojo","2003")
mi_auto.avance("200")


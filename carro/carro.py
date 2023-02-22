class Carro:
    def __init__(self, request):
        self.request=request
        self.session=request.session
        carro=self.session.get("carro")
        if not carro:
            carro=self.session["carro"]={}
            
        self.carro=carro

    def agregar(self, curso):
        if(str(curso.id) not in self.carro.keys()):
            self.carro[curso.id]={
                "curso_id": curso.id,
                "nombre": curso.nombre,
                "precio": str(curso.precio),
                "cantidad":1,
                "imagen": curso.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key==str(curso.id):
                    value["cantidad"]=value["cantidad"]+1
                    value["precio"]=float(value["precio"])+curso.precio
                    if value["cantidad"]>1:
                        self.eliminar(curso)
                    break
        self.guardar_carro()
    
    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True

    def eliminar(self, curso):
        curso.id=str(curso.id)
        if curso.id in self.carro:
            del self.carro[curso.id]
            self.guardar_carro()

    def restar(self, curso):
        for key, value in self.carro.items():
            if key==str(curso.id):
                value["cantidad"]=value["cantidad"]-1
                value["precio"]=float(value["precio"])-curso.precio
                if value["cantidad"]<1:
                    self.eliminar(curso)
                break
        self.guardar_carro()

    def limpiar_carro(self):
        carro=self.session["carro"]={}
        self.session.modified=True

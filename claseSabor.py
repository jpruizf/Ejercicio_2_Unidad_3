class Sabor:
    __idsabor: int
    __ingredientes: str
    __nombreSabor: str
    def __init__(self,idsabor,ingredientes,nombreSabor):
        self.__idsabor = idsabor
        self.__ingredientes = ingredientes
        self.__nombreSabor = nombreSabor
    def get_idsabor(self):
        return self.__idsabor
    def get_ingredientes(self):
        return self.__ingredientes
    def get_nombreSabor(self):
        return self.__nombreSabor
    
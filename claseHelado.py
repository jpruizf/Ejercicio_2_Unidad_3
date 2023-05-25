class Helado:
    __gramos: float
    __precio: float
    def __init__(self,gramos,precio):
        self.__gramos = gramos
        self.__precio = precio
    def get_gramos(self):
        return self.__gramos
    def get_precio(self):
        return self.__precio
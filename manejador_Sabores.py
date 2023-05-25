import csv
from claseSabor import Sabor
class Gestor_Sabores:
    __listaSabores: list
    __total:int
    def __init__(self):
        self.__listaSabores = []
        self.__total = 0
    def abrir_sabores(self):
        '''Arbir el archivo de sabores y asignar en una instancia de la clase sabor
        los atributos idsabor,ingredientes y nombre de cada sabor'''
        with open('sabores.csv','r',encoding='UTF-8') as archivo:
            lector = csv.reader(archivo, delimiter=',')
            next(lector)
            for fila in lector:
                if len(fila) >= 3:
                    idsabor = int(fila[0])
                    ingredientes = str(fila[1])
                    nombre_sabor = str(fila[2])
                    todos_sabores = Sabor(idsabor,ingredientes,nombre_sabor)
                    self.__listaSabores.append(todos_sabores)
        return self.__listaSabores
    
    def mostrar_sabores(self):
        """
            Muestra los sabores en la lista de sabores.
            Imprime el ID, ingredientes y nombre de cada sabor.
        """
        for sabor in self.__listaSabores:
            print(f"{sabor.get_idsabor()} | {sabor.get_ingredientes()} | {sabor.get_nombreSabor()}")
    def cuenta_sabores(self):
        '''Cuenta la cantidad de sabores que el cliente va a elegir'''
        contador = 0
        bandera = True
        for fila in self.__listaSabores:
            if bandera:
                elige_sabor = int(input("Seleccione el sabor ingresando el numero de ID >>"))
                if fila.get_idsabor() == elige_sabor:
                    if contador <= 3:
                        contador += 1
                        self.__total += contador
                        print("Sabor cargado")
                    else:
                        bandera = False
                else:
                    print("ID no valido, no se cargo ningun sabor")
            else:
                return contador
    def sabores_mas_vendidos(self):
        '''Muestra los sabores mas vendidos'''
        for fila in self.__listaSabores:
            if self.__total > 2:
                print(fila.get_nombreSabor())
    def total_gramos(self,aux_gramos):
        '''Recibe a partir de la instancia de la clase gestor 
        sabores en la clase gestor helados y muestra el total aproximado de gramos de helado vendido'''
        aux_total = 0
        if self.__total > 0:
            aux_total = aux_gramos // self.__total
        if aux_total > 0:
            print(aux_total)
        else:
            print("No se vendio ningun gramos de helado")


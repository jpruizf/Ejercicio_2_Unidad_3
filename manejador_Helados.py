from claseHelado import Helado
from manejador_Sabores import Gestor_Sabores
class Gestor_Helados:
    __lista_helados:list
    def __init__(self):
        self.__lista_helados = []
    def cargar_helados(self):
        '''Cargar la cantidad en gramos de helado y el precio correspondiente'''
        gramos = float(input("Ingrese la cantidad en gramos de helado >> "))
        while gramos != 0:
            precio = float(input("Ingrese el precio >>"))
            helado = Helado(gramos,precio)
            self.__lista_helados.append(helado)
            gramos = float(input("Ingrese la cantidad en gramos de helado >> "))
        return self.__lista_helados
    def ver_helados(self):
        '''Muestra los gramos de helados cargados y su precio correspondiente'''
        for fila in self.__lista_helados:
            print(f"Gramos >>  {fila.get_gramos()} | Precio >> {fila.get_precio()}")
    def venta_helados(self):
        '''Carga la venta de helados ingresando el peso en gramos'''
        aux_contador = 0
        seleccion_gramos = float(input("Ingrese los gramos a vender (Para finalizar ingrese 0) > >"))
        while  seleccion_gramos != 0:
            if seleccion_gramos == 100:
                aux_contador += 1
            elif seleccion_gramos == 150:
                aux_contador += 1
            elif seleccion_gramos == 250:
                aux_contador += 1
            elif seleccion_gramos == 500:
                aux_contador += 1
            elif seleccion_gramos == 1000:
                aux_contador += 1
            else:
                print("Error inesperado, vuelva a intentarlo :/")
            seleccion_gramos = float(input("Ingrese los gramos ah vender (Para finalizar ingrese 0) > >"))
        return aux_contador
    def enviar_gramos(self):
        '''Enviar los gramos vendidos a partir de la instacia de la clase gestor sabores'''
        manejador_sabores = Gestor_Sabores()
        seleccion_gramos = float(input("Ingrese los gramos a vender (Para finalizar ingrese 0) > >"))
        manejador_sabores.total_gramos(seleccion_gramos)
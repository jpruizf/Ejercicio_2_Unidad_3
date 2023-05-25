from manejador_Helados import Gestor_Helados
from manejador_Sabores import Gestor_Sabores

def menu():
    gestor_sabores = Gestor_Sabores()
    gestor_helados = Gestor_Helados()
    print("Bienvenido a la heladeria El Conito :-) ")
    print("1 >> Cargar archivo de los sabores")
    print("2 >> Registrar un helado vendido")
    print("3 >> Mostrar el nombre de los 5 sabores mas pedidos")
    print("4 >> Ingresar un numero de sabor y ver el total de gramos vendidos")
    print("5 >> Terminar")
    opcion = input("Seleccione una de las opciones dadas >> ")
    while opcion != 0:
        if opcion == '1':
            gestor_sabores.abrir_sabores()
            gestor_helados.cargar_helados()
            gestor_sabores.mostrar_sabores()
            gestor_helados.ver_helados()
        elif opcion == '2':
            if gestor_helados.venta_helados() > 0 :
                if gestor_sabores.cuenta_sabores() > 0:
                    print("<<< El helado vendido a sido registrado >>>")
        elif opcion == '3':
            gestor_sabores.sabores_mas_vendidos()
        elif opcion == '4':
            gestor_helados.enviar_gramos()
            print("<< Total aproximado en gramos de la venta de helados >>")
        elif opcion == '5':
            return  0
        else:
            print("Opcion no valida!. Intente nuevamente")
        print("Bienvenido a la heladeria El Conito")
        print("1 >> Cargar archivo de los sabores")
        print("2 >> Registrar un helado vendido")
        print("3 >> Mostrar el nombre de los 5 sabores mas pedidos")
        print("4 >> Ingresar un numero de sabor y ver el total de gramos vendidos")
        print("5 >> Terminar")
        opcion = input("Seleccione una de las opciones dadas >> ")
if __name__=='__main__':
    menu()
            
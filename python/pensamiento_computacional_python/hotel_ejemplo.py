class Hotel:
    
    def __init__(self, stars, rooms, room_bats):
        self._estrellas = stars                     #atributo privado 
        self._cuartos = rooms                        #atributo privado este dato lo estaré variando
        self._cuartos_bano = room_bats               #atributo privado este dato lo estaré variando

        self._cuartos_max = rooms                   #este dato es fijo, representa los cuartos máximo que introduce el usuario
        self._cuartos_bano_max = room_bats          #este dato es fijo, representa los cuartos baño máximo que introduce el usuario
    
    def _actualizar_datos(self, accion, cuartos, cuartos_bano):#metodo privado

        if accion == 'alquilar'or accion == 'reservar':        # al alquilar y reservar, restamos y calculamos los cuartos disponibles
            if self._cuartos - cuartos < 0:                     # verificamos que el usuario no reserve cuartos que no se dispone
                print(f'*** NO SE DISPONE DE {cuartos} CUARTOS, SOLO QUEDAN {self._cuartos} CUARTOS ***')
            else:                                               # si todo es conforme, actualizamos la data
                self._cuartos -= cuartos        
            if self._cuartos_bano - cuartos_bano < 0:           # verificamos que el usuario no reserve cuartos baño que no se dispone
                print(f'*** NO SE DISPONE DE {cuartos_bano} CUARTOS BAÑO, SOLO QUEDAN {self._cuartos_bano} CUARTOS ***')
            else:                                                # si todo es conforme, actualizamos la data
                self._cuartos_bano -= cuartos_bano              #actualizamos los atributos

        elif accion == 'cancelar_reserva':                      #al cancelar reserva, sumamos y calculamos los cuartos disponibles
            if self._cuartos + cuartos > self._cuartos_max:
                print(f'*** NO SE PUEDE EJECUTAR LA ACCIÓN, SE DISPONE DE {self._cuartos} CUARTOS ***')
            else:
                self._cuartos += cuartos
            if self._cuartos_bano + cuartos_bano > self._cuartos_bano_max:
                print(f'*** NO SE PUEDE EJECUTAR LA ACCIÓN, SE DISPONE DE {self._cuartos_bano} CUARTOS BAÑO ***')
            else:
                self._cuartos_bano += cuartos_bano              #actualizamos los atributos
    
    def alquilar(self, cuartos, cuartos_bano):#método público
        self._actualizar_datos('alquilar', cuartos, cuartos_bano)
        print(f'Quedan {self._cuartos} cuartos y {self._cuartos_bano} cuartos baño disponibles')
    
    def reservar(self, cuartos, cuartos_bano):#método público
        self._actualizar_datos('reservar', cuartos, cuartos_bano)
        print(f'Quedan {self._cuartos} cuartos y {self._cuartos_bano} cuartos baño disponibles')
    
    def cancelar_reserva(self,cuartos, cuartos_bano):#metodo público
        self._actualizar_datos('cancelar_reserva', cuartos, cuartos_bano)
        print(f'Quedan {self._cuartos} cuartos y {self._cuartos_bano} cuartos baño disponibles')
    
    def llamar_asistente(self):#metodo_público
        print(""" 
        
        --- EL ASISTENTE ESTÁ EN CAMINO  --- """)
    
    def menu(self):
        
        opcion = int(input(f"""
        ----------------- WELCOME TO HOTEL ASSISTENT ----------------- 
            Este es el asistente para trabajar con los hoteles
            
            DISPONES DE:
            - {self._cuartos} CUARTOS
            - {self._cuartos_bano} CUARTOS BAÑO
            -----------------------------
                ¿Qué es lo que deseas hacer?  
                    1.- Alquilar
                    2.- Reservar
                    3.- Cancelar reserva
                    4.- Llamar sistente
                    5.- Salir del programa

            Eliga una opción ---> """))
        return opcion

        

def preguntar():#función para preguntarle al usuario cuantos cuartos y cuartos va alquilar, reservar o cancelar la reserva
    cuartos = int(input('Cuantos cuartos: '))          
    cuantos_bano = int(input('Cuantos cuartos baño: '))

    return cuartos, cuantos_bano        #retorno 2 valores

def run():

    hotel_cielo = Hotel(3,20,15)        #creo un objeto de la clase Hotel. Parametros 3 estrellas x'dd , 20 cuartos y 15 cuartos baño

    while True:
        opcion = hotel_cielo.menu()
        if opcion == 1:
            print(" ----------------- ALQUILAR ----------------------")
            cuartos, cuartos_bano = preguntar()
            hotel_cielo.alquilar(cuartos, cuartos_bano)
        elif opcion == 2:1
            print(" ----------------- RESERVAR ----------------------")
            cuartos, cuartos_bano = preguntar()
            hotel_cielo.reservar(cuartos, cuartos_bano)
        elif opcion == 3:
            print(" ----------------- CANCELAR RESERVA ----------------------")
            cuartos, cuartos_bano = preguntar()
            hotel_cielo.cancelar_reserva(cuartos, cuartos_bano)
        elif opcion == 4:
            hotel_cielo.llamar_asistente()
        else:
            break


if __name__ == '__main__':		#entry point
    run()
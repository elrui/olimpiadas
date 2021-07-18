'''
Comentarios:
** La tarea requiere que las cosas se guarden en un archivo, el programa al arrancar deberia leer el archivo y actualizar su contenido
** También indica que se deben usar funciones. Supongo que se refiere a las funciones que definimos ayer

Para la pregunta 1, estoy asumiendo que se puede:
  - Agregar un atleta nuevo
  - Agregar medallas a un atleta existente
  - Si un atleta puede participar en más de un deporte debe tener ID distinto (para que los ID sean unicos)
  - El ID se introduce a mano y puede ser alfanumerico. Si se quiere que sea autoincremental hay que hacer una función extra para eso

Para la pregunta 2, simplemente se consulta la base de datos y se formatea como tabla



'''
##Algoritmo Medallero

import os
import platform

import olimpiclib as ol 

filename='medallero.txt'
delimiter='#'

# Verificar si el archivo existe, y de no ser así, crearlo vacío
if not os.path.isfile(filename):
    ol.createFile(filename)


cls = 'cls' if platform.system() == 'Windows' else 'clear'   ## Esto es solo para que el cls funcione en todas las plataformas, se puede omitir

def menu():  
    os.system(cls)
    print("Medallero Olimpico".center(60))
    print("\n\n")
    print("1.  Registro de Atletas")
    print("2.  Consultar medallas obtenidas por pais")
    print("3.  Consultar pais con mayor numero de medallas")
    print("4.  Consultar medallas por atleta")
    print("5.  Listar por un deporte X")
    print("6.  Salir")

    opcion = input("Ingrese la Opcion del menu: ")
    return opcion

#Se invoca la función
while True:
    registry = ol.readFile(filename, delimiter=delimiter)    # leer el archivo y actualizar el registro cada vez que se carga el menu
    opcion = menu()
    
    ##1 Registrar atleta

    if opcion == '1':

        while True:
            id      = int(input('Ingrese el ID del atleta: '))

            atleta = ol.findAthlete(id, registry)

            if not atleta:      # si el atleta con ese ID no existe, se crea
                nombre  = input('Ingrese el nombre del atleta: ')
                pais    = input('Ingrese el país al que representa el atleta: ')
                deporte = input('Indique en qué deporte compite el atleta: ')
                registry = ol.createAthlete(id, nombre, pais, deporte, registry)
                
            else: 
                print('Nombre del atleta: ', atleta['name'])
                print('País al que representa: ', atleta['country'])
                print('Deporte en el que compite: ', atleta['sport'])

            medallas = int(input('Indique número de medallas a cargar (0 para salir) '))

            while medallas > 0:
                tipo = input('Indique tipo de medalla a cargar (Oro: 1, Plata: 2, Bronce: 3) ')
                if tipo == '1':
                    registry = ol.addMedal(id, 'gold', 1, registry)
                elif tipo == '2':
                    registry = ol.addMedal(id, 'silver', 1, registry)
                elif tipo == '3':
                    registry = ol.addMedal(id, 'bronze', 1, registry)
                else:
                    pass

                medallas -= 1

            otro = input('Desea agregar otro atleta? (S/N) ').lower()

            if otro != 's':
                break    

        ol.writeFile(filename, registry, delimiter=delimiter)    # Actualizar el archivo en disco


    ##2 Medallas por país

    elif opcion =='2':
        os.system(cls)
        country = input("Ingrese el nombre del pais a consultar: ")
        
        atletas = ol.byCountry(country, registry)
        
        print('{:<30} {:<30} {:<8} {:<8} {:<8} '.format('Nombre', 'Deporte', 'Oro', 'Plata', 'Bronce')) 

        for atleta in atletas:
            print('{:<30} {:<30} {:<8d} {:<8d} {:<8d} '.format(atleta['name'], atleta['sport'], int(atleta['gold']), int(atleta['silver']), int(atleta['bronze']))) 
        
        while True:
            _ = input('Presione enter para volver al menú principal ')
            break

    ##3 País con mas medallas, medallero por deporte

    elif opcion == '3':
        os.system(cls)

        country = ol.topMedalistCountry(registry)
        print('El país con más medallas es:', country)
        print()

        medallero = ol.sportMedalsByCountry(country, registry)

        print('{:<30} {:<8} {:<8} {:<8} '.format('Deporte', 'Oro', 'Plata', 'Bronce')) 

        for deporte, med in medallero.items():
            print('{:<30} {:<8d} {:<8d} {:<8d} '.format(deporte, int(med['gold']), int(med['silver']), int(med['bronze'])))

        while True:
            _ = input('Presione enter para volver al menú principal ')
            break

    ##4 Medallas atleta

    elif opcion =='4':
        os.system(cls)
        id = input("Indique el ID del atleta a consultar: ")

        atleta = ol.findAthlete(id, registry)

        print('{:<30} {:<30} {:<30} {:<8} {:<8} {:<8} '.format('Nombre', 'Pais', 'Deporte', 'Oro', 'Plata', 'Bronce')) 
        if atleta:
            print('{:<30} {:<30}  {:<30} {:<8d} {:<8d} {:<8d} '.format(atleta['name'], atleta['country'], atleta['sport'], int(atleta['gold']), int(atleta['silver']), int(atleta['bronze']))) 
        
        while True:
            _ = input('Presione enter para volver al menú principal ')
            break


    ##5 Medallero por deporte

    elif opcion =='5':
        os.system(cls)
        sport = input("Indique el deporte a consultar: ")

        atletas = ol.bySport(sport, registry)

        print('{:<30} {:<30} {:<8} {:<8} {:<8} '.format('Nombre', 'Pais', 'Oro', 'Plata', 'Bronce')) 

        for atleta in atletas:
            print('{:<30} {:<30} {:<8d} {:<8d} {:<8d} '.format(atleta['name'], atleta['country'], int(atleta['gold']), int(atleta['silver']), int(atleta['bronze']))) 
        
        while True:
            _ = input('Presione enter para volver al menú principal ')
            break
            
    ##6

    elif opcion =='6':
        os.system(cls)
        print("Adios".center(60))
        break
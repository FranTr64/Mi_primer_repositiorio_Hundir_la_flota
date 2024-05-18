# Tablero dinamico
# Oponente IA
import random
def main():
    def set_up():    
        tablero = []
        tablero2 = []
        print('inicio')
        filas = int(input('Filas'))
        # filas = 10
        columnas = int(input('Columans'))
        # columnas = 10
        area = (filas * columnas)//5

        barcos={1:[],2:[],3:[],4:[],5:[]}
        for _ in range(0,filas):
            tablero.append([0]*columnas)
        for _ in range(0,filas):
            tablero2.append([0]*columnas)
        crear_b={1:0,2:0,3:0,4:0,5:0}
        while area>0:
            sel=random.randint(1,5)
            if(area-sel)>=0:
                crear_b[sel]+=1
                area-=sel

        def crear_barcos(crear_b):
            barquitos={1:[],2:[],3:[],4:[],5:[]}
            for j in crear_b:
                while crear_b[j]>0:
                    pos_x = random.randint(1,columnas)
                    pos_y = random.randint(1,filas)
                    elec_eje=random.choice(['v','h'])
                    barco=[[pos_x,pos_y],elec_eje]
                    barquitos[j].append(barco)
                    crear_b[j]-=1
            poner_posiciones(barquitos)         
        def poner_posiciones(barquitos):
            luz=True
            for i in range(1,6):
                for j in barquitos[i]:
                    y = (j[0][1])
                    x = (j[0][0])
                    coordenada=[]
                    vacio=True
                    if j[1]=='v':
                        x-=1
                        y-=2
                        c=0
                        for _ in range(0,i):
                            if y<filas-1:
                                y+=1
                                c+=1
                                if tablero[y][x] !=0:
                                    vacio=False
                                    luz=False
                            else:
                                y = (j[0][1])
                                y-=1
                                for _ in range(0,(i-c)):
                                    y-=1
                                    if tablero[y][x] !=0:
                                        vacio=False
                                        luz=False
                                break
                        
                        if vacio==True:
                            molde_barco=[]
                            y = (j[0][1])-2
                            x = (j[0][0])-1
                            for _ in range(0,c):
                                y+=1
                                tablero[y][x] = i
                                coordenada=[[(x+1),(y+1)],'f']
                                molde_barco.append(coordenada)
                            y = (j[0][1])-1
                            x = (j[0][0])-1
                            for _ in range(0,i-c):
                                y-=1
                                tablero[y][x] = i
                                coordenada=[[(x+1),(y+1)],'f']
                                molde_barco.append(coordenada)
                            barcos[i].append(molde_barco)
                        else:
                            crear_b[i]+=1
                    else:
                        y-=1
                        x-=2
                        c=0
                        for _ in range(0,i):
                            if x<columnas-1:
                                x+=1
                                c+=1
                                if tablero[y][x] != 0:
                                    vacio=False
                                    luz=False
                            else:
                                x = (j[0][0])
                                x-=1
                                for _ in range(0,(i-c)):
                                    x-=1
                                    if tablero[y][x] !=0:
                                        vacio=False
                                        luz=False
                                break
                        if vacio==True:
                            molde_barco=[]
                            y = (j[0][1])-1
                            x = (j[0][0])-2
                            for _ in range(0,c):
                                x+=1
                                tablero[y][x] = i
                                coordenada=[[(x+1),(y+1)],'f']
                                molde_barco.append(coordenada)
                            y = (j[0][1])-1
                            x = (j[0][0])-1
                            for _ in range(0,i-c):
                                x-=1
                                tablero[y][x] = i
                                coordenada=[[(x+1),(y+1)],'f']
                                molde_barco.append(coordenada)
                            barcos[i].append(molde_barco)
                        else:
                            crear_b[i]+=1
            if not luz:
                print('reintentar')
                crear_barcos(crear_b)
            else:
                inicio_juego(tablero,tablero2,filas,columnas,barcos)
        crear_barcos(crear_b)
    
    def inicio_juego(tablero,tablero2,filas,columnas,barcos):
        gmo=True
        for i in range(0,filas):
            print(tablero[i])
        print('------------------------------------------')
        while gmo==True:
            m=1
            print('\t',end='')
            print('\t'.join(f'{x}' for x in range(1,columnas+1)),end='\n')
            for i in range(0,filas):
                print(m,end='\t')
                print('\t'.join(f'{x}' for x in tablero2[i]),end='\n')
                m+=1
            intro=input('Posición donde lanzar el torpedo A,B: ')
            comando = [int(x) for x in intro.split(',')]
            
            if len(comando)==2:
                if isinstance(comando[0],int) and isinstance(comando[1],int):
                    if columnas>=comando[0]>0 and filas>=comando[1]>0:
                        x = comando[0]-1
                        y = comando[1]-1
                        casilla = tablero[y][x]
                        encontrado=False
                        tocados=0
                        if casilla !=0:
                            for barco_ind in barcos[casilla]:
                                if encontrado==False:
                                    for cord_vm in barco_ind:
                                        if comando in cord_vm:
                                            if cord_vm[1] != 'h':
                                                cord_vm[1]='h'
                                                print('¡Impacto!')
                                                for von in barco_ind:
                                                    if von[1] == 'h':
                                                        tocados+=1
                                                        encontrado=True
                                                        tablero2[y][x]='X'
                                                        
                                                if tocados==len(barco_ind):
                                                    print('¡Barco hundido!')
                                                break
                                            else:
                                                print('Parte de barco ya tocada')
                                                for von in barco_ind:
                                                    if von[1] == 'h':
                                                        tocados+=1
                                                if tocados==len(barco_ind):
                                                    print('¡Barco hundido!')
                                                    encontrado=True

                        else:
                            tablero2[y][x]='W'
                            print('Agua')
                    else:
                        print('Introduzca una coordenada vAlida')
                else:
                    print('Introduzca una coordenada valida')
            else:
                print('Introduzca una coordenada válida')
            gmo=False
            for tamaño in barcos:
                for barca in barcos[tamaño]:
                    for vom in barca:
                        if vom[1]=='f':
                            gmo=True
            if gmo==False:
                Fin_Del_Juego()
            print('\n')

    def Fin_Del_Juego():
        print('¡Victoria! ¡Todos los barcos han sido hundidos!')
        respuesta = input('Quieres jugar otra vez? (Si/No)')
        while (respuesta != 'Si') and (respuesta != 'No'):
            respuesta = input('Quieres jugar otra vez? (Si/No)')
        if respuesta == 'Si':
            set_up()
        else:
            print('Gracias por jugar')
            


    



    set_up()

if __name__ == '__main__':
    main()

# for i in range(0,filas):
#     print(tablero[i])
# Barcos:
# [Barco_tamaño a elegir]
# [Barcos de la lista a elegir]
# [Posiciones de los barcos/Eje de rotacion]
# [Cada posicion individual]
# [Coordenadas de la posicion/si está vivo o muerto]
# [Elegir la 'x' o la 'y']
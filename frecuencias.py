import math

def rango(arr):
    return max(arr) - min(arr)

def pasosRango(arr):
    return "R = {} - {} = {}".format(max(arr), min(arr), rango(arr))

def intervalo(n):
    k = 1+1.322*math.log(n)
    if(round(k)%2 == 1):
        return round(k)
    
    if(math.ceil(k)%2 == 1):
        return math.ceil(k)
    
    return math.ceil(k) + 1
    
def pasosInterv(n):
    temp = 1+1.322*math.log(n)
    k = intervalo(n)
    pasos =f"k = 1 + 1.322 * log({n})"
    
    if(temp == k):
        return pasos + f"= {temp}"
        
    
    return pasos + f"= {temp:.3f} =>{k}"

def amplitud(arr):
    a = rango(arr)/intervalo(len(arr))
    return math.ceil(a)

def pasosAmplitud(arr):
    n = len(arr)
    return  f"A = R/k = {rango(arr)}/{intervalo(n)} = {rango(arr)/intervalo(n):.3} => {amplitud(arr)}"

def listaRangos(arr, n):
    arr = sorted(arr)
    r = rango(arr)
    a = amplitud(arr)
    lista = []
    
    i = arr[0]
    i-=n
    maxNum = max(arr)
    while(i < maxNum):
        lista.append(i)
        i+=a
    
    
    return lista



def marcaClase(n, k):
    return (2*n + k)/2

def buscarRango(arr, ran, amp):
    lsRan = []
    for a in arr:
        if a >= ran and a < (ran + amp):
            lsRan.append(a)  
            
    return lsRan

def lsAbsoluta(arr, i):
    ran = listaRangos(arr, i)
    amp = amplitud(arr)
    frec=[]
    
    for r in ran:
        frec.append(buscarRango(arr, r, amp))
    
    ran2 = ran[-1] + amp
    ultRango = frec[-1]
    
    if ran2 == max(arr):
        ultRango.append(buscarRango(arr, ran2, ran2+1))
    
    return frec

def absoluta(arr, i):
    abs = lsAbsoluta(arr,i)
    lsAbs = []
    for i in abs:
        lsAbs.append(len(i))
        
    return lsAbs
        
def relativa(abs, n):
    lsRel = []
    for i in abs:
        lsRel.append(i/n)
    
    return lsRel
   
def acumulado(arr):
    i = 0;
    acum = []
    for a in arr:
        i+=a
        acum.append(i)
    
    return acum

def formRan(rango, a):
    return f"{rango}-{rango+a}"

def formateo(n):
    return "{:.2f}".format(n) 

def imprimirLista(arr, n):
    j=0
    for i in(range (len(arr))):
        j+=1
        print(f"{arr[i]},\t ", end=" ")
        if(j == n):
            print()
            j=0
    

def tabla(arr,i):
    n = len(arr)
    ran = listaRangos(arr, i)
    amp = amplitud(arr)
    abs = absoluta(arr, i)
    absAcum = acumulado(abs)
    rel = relativa(abs, n)
    relAcum = acumulado(rel)
    print()
    print("Rangos\t  X\tf\tF\tfr\tFr")
    for i in  range(len(ran)):
        print("[{})\t{:.2f}\t{}\t{}\t{:.2f}\t{:.2f}"
              .format(formRan(ran[i], amp),marcaClase(ran[i], ran[i]+amp),
                      abs[i], absAcum[i], rel[i], relAcum[i]))
        
def solvFrecuencias(arr, i):
    print(f"n = {len(arr)}")
    print(pasosRango(arr))
    print(pasosInterv(len(arr)))
    print(pasosAmplitud(arr))
    
    tabla(arr, i)
   
def pedirValores():
    lsValores = []
    
    print("Ingresa los valores [ENTER para terminar]")
    while True:
        inp = input("> ")
        if(inp == ""):
            return lsValores

        lsValores.append(int(inp))
        
#---------------------- SIUUU -------------
#Ingresar los valores separados por comas
valores = [
    2,7,10,16,19,
    22,6,25,5,20,
    13,32,13,29,18,
    20,13,6,12,35,
    17,11,4,9,33
]
####### Se puede sobreescribir el valor por si no se quiere borrar el anterior
valores = [60,66,77,70,66,68,57,70,66,52,75,65,69,71,58,66,67,74,61,63,69,80,59,66,70,67,78,75,64,71,81,62,64,69,68,72,83,56,65,74,67,54,65,65,69,61,67,73,57,62,67,68,63,67,71,68,76,61,62,63,76,61,67,67,64,72,64,73,79,58,67,71,68,59,69,70,66,62,63,66]

#valores = []
columnas = 4    #Filas a desplegar todos los valores
balanceo = 0    #Si se desea balancear la tabla (defecto 0)    

teclado = input("Ingresar valores por teclado? (S/N): ").lower()

if(teclado == "s"):
    valores = pedirValores()

if(len(valores) > 0):
    valores = sorted(valores)
    print("VALORES:")
    imprimirLista(valores, columnas)
    print("\n")
    solvFrecuencias(valores, balanceo)
else:
    print("INGRESA VALORES")
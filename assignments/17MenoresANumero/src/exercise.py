
def MenoresAlDiez(x) :
    Map = []
    for a in range(len(x) ):
        for b in range(len(x[a])) :
            if x[a][b]<10 :
                Map.append(x[a][b])
    return(Map)           
def main():
    Lista= []
    fila = int(input())
    columna = int(input())
    for a in range (fila) :
        Lista.append([])
        for b in range (columna) :
            num = int(input())
            Lista[a].append(num)
    respuesta = MenoresAlDiez(Lista)
    print(respuesta)
   

if __name__=='__main__':
    main()

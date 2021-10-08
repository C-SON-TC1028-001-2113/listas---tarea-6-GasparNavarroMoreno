def main():
    x = -1
    suma = 0
    y = 1
    z = 1
    orden = []
    while x <= -1 :
        x = int(input())
    if x == 0 :
        print(orden)
    elif x==1 :
        orden.append(0)
        print(orden)
    elif x==2 :
        orden.append(0)
        orden.append(1)
        print(orden)
    else :
        orden.append(0)
        orden.append(1)
        orden.append(1)
        for i in range(x-3) :
            suma = y + z
            x = y
            y = suma
            orden.append(suma)
        print(orden)

if __name__=='__main__':
    main()

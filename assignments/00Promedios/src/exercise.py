def main():
    #escribe tu código abajo de esta línea
    print("Promedio de 10 numeros")
    suma=0
    cp=0
    ci=0
    for i in range(10):
        n=int(input("Dame un numero"))
        if n%2 ==0:
            cp=cp+1
        else:
            ci=ci+1
        suma=suma+n
    promedio=suma/10
    print(f"El Promedio de los valores capturados es: {promedio}")
    print(f"El total de numeros pares es {cp}")
    print(f"El total de numeros impares es {ci}")


if __name__=='__main__':
    main()

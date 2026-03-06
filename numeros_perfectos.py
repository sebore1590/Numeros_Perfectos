import json

def pedirNumeros():
    limiteInicial = int(input("Ingrese desde que numero desea buscar números perfectos: "))
    limiteFinal = int(input("Ingrese hasta que limite desea buscar números perfectos: "))

    if limiteInicial > limiteFinal:
        print("El limite inicial debe ser menor al limite final")
        exit()

    if limiteInicial < 0:
        print("El rango solo permite numeros positivos")
        exit()

    return limiteInicial, limiteFinal

def calculaNumerosPerfectos(limiteInicial, limiteFinal):

    numerosPerfectos = []

    for num in range(limiteInicial, limiteFinal + 1):

        sumaDivisores = 0

        for i in range(1, (num // 2) + 1):
            if num % i == 0:
                sumaDivisores += i

        if sumaDivisores == num:
            print(f"Numero perfecto encontrado: {num}")
            numerosPerfectos.append(num)

    return numerosPerfectos

limiteInicial, limiteFinal = pedirNumeros()

print(f"Buscando numeros perfectos desde {limiteInicial} hasta {limiteFinal}")

numerosPerfectos = calculaNumerosPerfectos(limiteInicial, limiteFinal)

print(f"Los numeros perfectos son: {numerosPerfectos}")

datos = {
    "limite_busqueda": f"{limiteInicial} - {limiteFinal}",
    "numeros_perfectos": numerosPerfectos
}

with open("numeros_perfectos.json", "w") as archivo:
    json.dump(datos, archivo, indent=4)

print("Resultados guardados en numeros_perfectos.json")
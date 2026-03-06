import json

def pedir_numeros():
    limite_inicial = int(input("Ingrese desde que numero desea buscar números perfectos: "))
    limite_final = int(input("Ingrese hasta que limite desea buscar números perfectos: "))

    if limite_inicial > limite_final:
        print("El limite inicial debe ser menor al limite final")
        exit()

    if limite_inicial < 0:
        print("El rango solo permite numeros positivos")
        exit()

    return limite_inicial, limite_final

def calculaNumerosPerfectos(limite_inicial, limite_final):

    numerosPerfectos = []

    for num in range(limite_inicial, limite_final + 1):

        suma_divisores = 0

        for i in range(1, (num // 2) + 1):
            if num % i == 0:
                suma_divisores += i

        if suma_divisores == num:
            print(f"Numero perfecto encontrado: {num}")
            numerosPerfectos.append(num)

    return numerosPerfectos

limite_inicial, limite_final = pedir_numeros()

print(f"Buscando numeros perfectos desde {limite_inicial} hasta {limite_final}")

numerosPerfectos = calculaNumerosPerfectos(limite_inicial, limite_final)

print(f"Los numeros perfectos son: {numerosPerfectos}")

datos = {
    "limite_busqueda": f"{limite_inicial} - {limite_final}",
    "numeros_perfectos": numerosPerfectos
}

with open("numeros_perfectos.json", "w") as archivo:
    json.dump(datos, archivo, indent=4)

print("Resultados guardados en numeros_perfectos.json")
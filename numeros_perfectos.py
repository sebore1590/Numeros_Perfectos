
import json

limite_inicial = int(input("Ingrese desde que numero desea buscar números perfectos: "))
limite_final = int(input("Ingrese hasta que limite desea buscar números perfectos: "))
if limite_inicial > limite_final:
    print(f"El limite inicial debe ser menor al limite final")
    exit()
if limite_inicial < 0:
    print(f"El rango solo permite numeros positivos")
    exit()

print(f"Buscando números perfectos desde {limite_inicial} hasta {limite_final}...")

numeros_perfectos = []

for num in range(limite_inicial, limite_final + 1):
    suma_divisores = 0

    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            suma_divisores += i
    if suma_divisores == num:
            print(f"Numero perfecto encontrado: {num}")
            numeros_perfectos.append(num)

datos = {
    "limite_busqueda": f"{limite_inicial} - {limite_final}",
    "numeros_perfectos": numeros_perfectos
}

with open("numeros_perfectos.json", "w") as archivo: #crear
    json.dump(datos, archivo, indent=4) #sobreescribir

print("Resultados guardados en numeros_perfectos.json")




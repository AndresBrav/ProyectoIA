from collections import deque


def buscar_camino(matriz, inicio, fin):
    filas = len(matriz)
    columnas = len(matriz[0])

    # Definir las direcciones posibles: arriba, abajo, izquierda, derecha
    direcciones = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Utilizar una cola para realizar la búsqueda en anchura
    cola = deque([(inicio, [])])

    while cola:
        actual, camino = cola.popleft()

        if actual == fin:
            # Hemos llegado al destino, devolver el camino
            return camino + [actual]

        for direccion in direcciones:
            nueva_posicion = (actual[0] + direccion[0], actual[1] + direccion[1])

            # Verificar si la nueva posición está dentro de los límites de la matriz y si es transitable
            if (
                0 <= nueva_posicion[0] < filas
                and 0 <= nueva_posicion[1] < columnas
                and matriz[nueva_posicion[0]][nueva_posicion[1]] != "X"
            ):
                # Agregar la nueva posición a la cola con el camino actualizado
                cola.append((nueva_posicion, camino + [actual]))
                # Marcar la posición como visitada para evitar bucles infinitos
                matriz[nueva_posicion[0]][
                    nueva_posicion[1]
                ] = "X"  # Marcar como visitada

    # Si no se encuentra un camino, devolver None
    return None


# Ejemplo de uso
matriz_ejemplo = [
    ["Sol", "Aves", "Luna", "Mar", "Pino"],
    ["Solis", "Aves", "Nube", "Aves", "Miel"],
    ["Alba", "Paz", "Mar", "Aves", "Pino"],
    ["Solis", "Río", "Río", "Río", "Sol"],
    ["Miel", "Pino", "Alba", "Sol", "Río"],
]

inicio_ejemplo = (0, 0)
fin_ejemplo = (4, 4)

camino_encontrado = buscar_camino(matriz_ejemplo, inicio_ejemplo, fin_ejemplo)

if camino_encontrado:
    print(f"Camino encontrado: {camino_encontrado}")
else:
    print("No se encontró un camino.")

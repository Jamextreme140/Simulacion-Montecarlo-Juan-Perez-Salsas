# Macias Bustamante Jaime Humberto
from tabulate import tabulate
import random as rnd

headers = ["n", "#ran", "L. vendidos", "Costo de prep.", "Ingreso x venta", "Utilidad"]
table = []
times = int(input("¿Cuantas veces desea ejecutar la simulación?: "))


def simulacion(t):
    selldata = []
    existence = []
    for i in range(t):
        # print("Iteración #" + str(i))
        n = rnd.random()
        lv = 0  # litros vendidos
        if 0 <= n <= 0.025:
            lv = 10
        elif 0.025 <= n <= 0.1:
            lv = 12
        elif 0.1 <= n <= 0.225:
            lv = 14
        elif 0.225 <= n <= 0.625:
            lv = 16
        elif 0.625 <= n <= 0.7875:
            lv = 18
        elif 0.7875 <= n <= 0.9:
            lv = 20
        elif 0.9 <= n <= 0.925:
            lv = 22
        elif 0.925 <= n <= 1:
            lv = 24
        existence.append(lv)
        # costo de preparacion ($15 x litro)
        p_cost = 15 * lv
        # vende en $35
        sell = 35 * lv
        utility = sell - p_cost
        # ganancia esperada
        selldata.append(utility)
        # se agrega a la tabla
        curr = [i + 1, n, lv, p_cost, sell, utility]
        table.append(curr)

    avg = sum(selldata) / len(selldata)
    total = sum(existence)
    print(tabulate(table, headers, tablefmt="github"))
    print("Existencia requerida: ", total)
    print("Ganancia esperada promedio: ", avg)


if __name__ == '__main__':
    simulacion(times)

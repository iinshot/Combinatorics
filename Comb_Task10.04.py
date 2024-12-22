from itertools import product

# x1 < 9, x2 > 8, x3 < 7, x4 > 6, x5 < 5, x6 > 3, x7 < 3
global_context = {
    "x1": (0, 8),
    "x2": (9, 60),
    "x3": (0, 6),
    "x4": (7, 60),
    "x5": (0, 4),
    "x6": (4, 60),
    "x7": (0, 2)
}


# генерирует неотрицательные целые решения уравнения
# x1 + x2 + x3 + x4 + x5 + x6 + x7 = 60
# и выводит в файл
def generate(summa, context):
    # summa: сумма переменных x1, ..., x7
    # context: словарь с ограничениями

    with open("output4.txt", "w") as file:
        count = 0

        # создание списка диапазонов в соответствии с ограничениями
        ranges = [
            range(context.get("x1", (0, float('inf')))[0], context.get("x1", (0, float('inf')))[1] + 1),
            range(context.get("x2", (0, float('inf')))[0], context.get("x2", (0, float('inf')))[1] + 1),
            range(context.get("x3", (0, float('inf')))[0], context.get("x3", (0, float('inf')))[1] + 1),
            range(context.get("x4", (0, float('inf')))[0], context.get("x4", (0, float('inf')))[1] + 1),
            range(context.get("x5", (0, float('inf')))[0], context.get("x5", (0, float('inf')))[1] + 1),
            range(context.get("x6", (0, float('inf')))[0], context.get("x6", (0, float('inf')))[1] + 1),
            range(context.get("x7", (0, float('inf')))[0], context.get("x7", (0, float('inf')))[1] + 1)
        ]

        # генерация всех комбинаций чисел
        for sol in product(*ranges):
            if sum(sol) == summa:
                file.write(f"({', '.join(map(str, sol))})\n")
                count += 1
        print(f"Количество решений: {count}")


result = 60
generate(result, global_context)
def bubble_sort(arr):
    n = len(arr)
    # Проходим по всем элементам массива
    for i in range(n):
        # Последние i элементов уже отсортированы
        for j in range(0, n - i - 1):
            # Меняем местами, если элемент найден больше следующего
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    # Запрашиваем количество чисел
    n = int(input("Введите количество чисел для сортировки: "))
    numbers = []

    # Запрашиваем числа
    for _ in range(n):
        num = float(input("Введите число: "))  # Можно использовать int, если нужны только целые числа
        numbers.append(num)

    # Сортируем числа
    bubble_sort(numbers)

    # Выводим отсортированные числа
    print("Отсортированные числа:", numbers)

# Запуск программы
if __name__ == "__main__":
    main()
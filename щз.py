import time
import random
# LSD
def time_counter(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Функция {func.__name__} сработала за {end_time - start_time} секунды")
        return result
    return wrapper
def counting_sort(arr, exp):
    n = len(arr)
    base = 10
    output = [0] * n  # Создаем массив для выходных данных такой же длины, как и входной массив
    count = [0] * base  # Создаем массив для подсчета количества элементов на каждом разряде (0-9)

    # Проходим по всем элементам во входном массиве и увеличиваем счетчик для каждого разряда
    for i in range(n):
        index = (arr[i] // exp) % 10  # Определяем текущий разряд числа
        count[index] += 1  # Увеличиваем счетчик для текущего разряда
    # Находим префиксную сумму в массиве count
    for i in range(1, 10):
        count[i] += count[i - 1]
    # Строим выходной массив на основе информации из массива count
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10  # Определяем текущий разряд числа
        output[count[index] - 1] = arr[i]  # Заполняем выходной массив
        count[index] -= 1  # Гарантирует, что относительный порядок равных элементов останется неизменным
        i -= 1

    # Копируем отсортированные данные обратно в исходный массив
    for i in range(n):
        arr[i] = output[i]


@time_counter
def radix_sort(arr):
    max_num = max(arr)  # Находим максимальное число в массиве
    exp = 1  # Инициализируем разряд, с которого начнем сортировку

    # Пока есть разряды у максимального числа
    while max_num // exp > 0:
        counting_sort(arr, exp)  # Вызываем сортировку подсчетом для текущего разряда
        exp *= 10  # Переходим к следующему разряду (делаем сдвиг вправо на один разряд)


if __name__ == "__main__":
    #arr = [random.randint(0, 10000) for _ in range(10000)]
    arr = [19,123,4,8325,5]
    radix_sort(arr)
    print("After sorting:", arr[:2], arr[-3:])

# На небольших данных существенно медленнее чем на больших

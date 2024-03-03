import time
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
    output = [0] * n
    count = [0] * 256

    for i in range(n):
        index = (ord(arr[i][exp]) if exp < len(arr[i]) else 0)  # Получаем ASCII-код символа
        count[index] += 1 # Отмечаем количество букв в массиве [1,0,0,0,0,5,0,0,0,0,10]

    for i in range(1, 256):
        count[i] += count[i - 1]
    #print(count)
    i = n - 1
    while i >= 0:
        index = (ord(arr[i][exp]) if exp < len(arr[i]) else 0)
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

@time_counter
def radix_sort(arr):
    max_length = max(len(s) for s in arr)
    exp = max_length - 1
    while exp >= 0:
        counting_sort(arr, exp)
        exp -= 1

if __name__ == "__main__":
    #arr = ["midnight", "badge", "bag" ,"worker" ,"banner" ,"wander"]
    arr = ["z","za","zab","zb","ab","a","az","c","fadfafasfasf"]
    print("Before sorting:", arr)
    radix_sort(arr)
    print("After sorting:", arr)

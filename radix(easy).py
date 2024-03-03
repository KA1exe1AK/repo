import random
import time
def time_counter(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Функция {func.__name__} сработала за {end_time - start_time} секунды")
        return result
    return wrapper

@time_counter
def radix_sort(arr):
    base = 10
    buckets = [[] for _ in range(base)]
    power_of_ten = 1
    d = max([len(str(x)) for x in arr])
    for pow in range(d):
        for elem in arr:
            buckets[elem // power_of_ten % 10].append(elem)
        print(pow, buckets)
        arr.clear()
        for bucket in buckets:
            arr += bucket
            bucket.clear()
        power_of_ten *= 10
        print(arr,'arr')
    return arr

if __name__ == "__main__":
    #arr = [random.randint(0, 10000) for _ in range(10000)]
    arr = [1,256,128,14,56,3,10]
    print(arr)
    print(radix_sort(arr))

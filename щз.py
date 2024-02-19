import random

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
    return arr

if __name__ == "__main__":
    #arr = [random.randint(0, 10000) for _ in range(random.randint(1, 100))]
    arr = [1,256,128,14,56,3,10]
    print(arr)
    print(radix_sort(arr))

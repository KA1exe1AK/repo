def heapsort(arr):
    def max_heapify(index, size):
        left_child = 2 * index + 1  # Индекс левого потомка
        right_child = 2 * index + 2  # Индекс правого потомка
        largest = index  # Изначально предполагаем, что наибольший элемент - текущий
        # Если левый потомок существует и его значение больше, чем значение текущего наибольшего элемента
        if left_child < size and arr[left_child] > arr[largest]:
            largest = left_child
        # Если правый потомок существует и его значение больше, чем значение текущего наибольшего элемента
        if right_child < size and arr[right_child] > arr[largest]:
            largest = right_child
        # Если сработал один из if
        if largest != index:
            arr[largest], arr[index] = arr[index], arr[largest]
            max_heapify(largest, size)

    def build_max_heap():
        # Начинаем с середины массива и двигаемся к началу
        # Количество узлов с дочерними элементами
        for i in range(len(arr) // 2 - 1, -1, -1):
            max_heapify(i, len(arr))

    build_max_heap()
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(0, i)  # Перестраиваем кучу без учета последнего элемента


arr = [6, 16, 1, 18, 7, 10]
heapsort(arr)
print('Sorted list:', arr)

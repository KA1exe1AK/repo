# Функция для обхода в глубину
def dfs(v, parent, adj):
    for u in adj[v]:
        if u != parent[v]:
            parent[u] = v
            dfs(u, parent, adj)


def pruefer_code(adj):
    # Определяем количество вершин в дереве
    n = len(adj)
    # Создаем список parent, в котором будем хранить родителей каждой вершины.
    # Изначально все вершины считаются без родителей, поэтому заполняем список -1.
    parent = [-1] * n
    # Задаем корневую вершину дерева как n-1 и вызываем dfs для заполнения списка parent
    parent[n - 1] = -1
    dfs(n - 1, parent, adj)

    # Инициализируем указатель ptr, который будет использоваться для поиска листовой вершины
    ptr = -1
    # Создаем список degree, в котором будем хранить степени вершин.
    # Степень вершины равна количеству смежных с ней вершин.
    degree = [len(edges) for edges in adj]

    # Ищем начальную листовую вершину для начала кодирования
    for i in range(n):
        if degree[i] == 1 and ptr == -1:
            ptr = i

    # Создаем пустой список для хранения кода Прюфера
    code = []
    # Инициализируем переменную leaf, которая будет указывать на текущую листовую вершину
    leaf = ptr
    # Проходим по всем вершинам, кроме двух последних, чтобы построить код Прюфера
    for _ in range(n - 2):
        # Получаем родителя текущей листовой вершины
        next_ = parent[leaf]
        # Добавляем индекс родителя в код Прюфера
        code.append(next_)
        # Уменьшаем степень родительской вершины на 1, так как мы удаляем текущую листовую вершину
        degree[next_] -= 1
        # Если степень родительской вершины стала равной 1 и она меньше указателя ptr,
        # то обновляем текущую листовую вершину
        if degree[next_] == 1 and next_ < ptr:
            leaf = next_
        # В противном случае, увеличиваем указатель ptr и ищем следующую листовую вершину
        else:
            ptr += 1
            while degree[ptr] != 1:
                ptr += 1
            leaf = ptr

    return code

# Пример использования
adj = [[1], [0, 2, 3], [1, 4], [1, 5], [2], [3, 6, 7], [5], [5]]
code = pruefer_code(adj)
print("Prufer код:", code)

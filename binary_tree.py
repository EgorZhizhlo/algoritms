# БИНАРНОЕ ДЕРЕВО
# Многоуровневая структура данных. Каждый узел имеет не более 2 дочерних узлов

# Класс узла дерева
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
# value - значение, которое хранится в узле
# left - ссылка на левый дочерний узел(изначально None)
# right - ссылка на правый дочерний узел(изначально None)

# Класс бинарного дерева
class BinaryTree:  
  # Инициализируем начальный узел через класс TreeNode
    def __init__(self, root_value):
            self.root = TreeNode(root_value)
    # root_value - значение узла
    # Заполнение дерево элементами через алгоритм обхода в ширину
    def insert(self, value):
        # создаем очередь
        queue = [self.root]
        # пока очередь не пустая циклино проходим по дереву в ширину и находим свободную ветку
        while queue:
            # извлекаем узел из очереди
            current_node = queue.pop(0)
            # если левого дочернего узла нет, то помещаем туда элемент
            if not current_node.left:
                current_node.left = TreeNode(value)
                break
            # иначе добавляем узел в очередь для дальнейшего прохождения и поиска свободного места
            else:
                queue.append(current_node.left)
            # если правого дочернего узла нет, то помещаем туда элемент
            if not current_node.right:
                current_node.right = TreeNode(value)
                break
            # иначе добавляем узел в очередь для дальнейшего прохождения и поиска свободного места
            else:
                queue.append(current_node.right)

    # ОБХОД ДЕРЕВА РЕКУРСИВНО
    # Обход в глубину(DFS)
    # 1 тип: прямой(спускаемся слева направо до конца и на каждом этапе выводим узел)
    def pre_order(self, node):
        if node:
            print(node.value, end=' ')
            self.pre_order(node.left)
            self.pre_order(node.right)
    # 2 тип: прямой(спускаемся слева направо до конца и на каждом этапе выводим узел)


    # 3 тип: прямой(спускаемся слева направо до конца и на каждом этапе выводим узел)

    # Обход в ширину(BFS)
    # 1 тип: прямой(спускаемся слева направо до конца и на каждом этапе выводим узел)
# Функция заполнения дерева с клавиатуры
def main():
    root_value = int(input())
    bt = BinaryTree(root_value)
    
    while True:
        user_input = input()
        if user_input.lower() == 'q':
            print("Bye!")
            break
        try:
            value = int(user_input)
            bt.insert(value)
        except ValueError:
            print("Error!")
    bt.pre_order(bt.root)


if __name__ == "__main__":
    main()

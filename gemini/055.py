class Node:
    def __init__(self, value):
        self.value = value  # ノードのデータ
        self.next = None    # 次のノードへの参照

class LinkedList:
    def __init__(self):
        self.head = None  # 先頭ノード（最初は空）

    def append(self, value):
        new_node = Node(value)
        if self.head is None:  # 最初のノード
            self.head = new_node
        else:
            current = self.head
            while current.next:  # 最後のノードまで移動
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()
# 出力: 10 -> 20 -> 30 -> None

def rev_ll(ll):
    if ll.node==None:
        return ll.head
    new_head=ll.node
    
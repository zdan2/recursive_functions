import collections

class Node:
    # ノード作成時に値を渡せるように __init__ を修正
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 木を生成する関数 (クラスの外に定義)
def create_tree(num_nodes):
    if num_nodes == 0:
        return None

    # 1からnum_nodesまでの値を持つリスト
    node_values = list(range(1, num_nodes + 1))
    
    # 最初の値をルートノードとして設定
    root = Node(node_values.pop(0))
    
    # 次に子を追加すべき親ノードを管理するためのキュー
    queue = collections.deque([root])
    
    # 値がなくなるまでループ
    while node_values:
        # キューから親ノードを取り出す
        parent = queue.popleft()
        
        # 左の子を作成してキューに追加
        left_value = node_values.pop(0)
        parent.left = Node(left_value)
        queue.append(parent.left)
        
        # もし値がまだ残っていれば、右の子も作成してキューに追加
        if node_values:
            right_value = node_values.pop(0)
            parent.right = Node(right_value)
            queue.append(parent.right)
            
    return root

# 生成された木を確認するための補助関数（任意）
def print_tree(node, level=0, prefix="Root:"):
    if node is not None:
        print(" " * (level * 4) + prefix, node.value)
        if node.left is not None or node.right is not None:
            print_tree(node.left, level + 1, "L---")
            print_tree(node.right, level + 1, "R---")

# --- 実行 ---
#print("木を生成します...")
# 15個のノードを持つ木を生成
#my_tree = create_tree(15)

# 木の構造を表示して確認
#print_tree(my_tree)
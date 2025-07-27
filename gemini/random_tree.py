import random

class Node:
    """2分木のノードを表すクラス"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        # デバッグ時に見やすいようにノードの値を返す
        return f"Node({self.value})"

def create_random_binary_tree(num_nodes: int):
    """
    指定されたノード数で、ランダムな構造の2分木を生成する。
    ノードの値は重複のないランダムな整数となる。

    Args:
        num_nodes (int): 生成するノードの総数。

    Returns:
        Node: 生成された2分木の根(root)ノード。num_nodesが0の場合はNoneを返す。
    """
    if num_nodes <= 0:
        return None

    # 1. ノードに割り当てるユニークな整数値を生成
    # 例: 10ノードなら、1から100の範囲からランダムに10個選ぶ
    node_values = random.sample(range(1, num_nodes * 10), num_nodes)
    
    # 2. 最初の値をrootノードとして設定
    root = Node(node_values.pop(0))
    
    # 3. 子を追加できる親ノードの候補リスト
    potential_parents = [root]
    
    # 4. 残りの値を新しいノードとして木に追加していく
    while node_values:
        new_value = node_values.pop(0)
        new_node = Node(new_value)
        
        # 親候補リストからランダムに親を選ぶ
        parent_node = random.choice(potential_parents)
        
        # 5. 親の左か右、空いている方にランダムに接続する
        available_slots = []
        if parent_node.left is None:
            available_slots.append('left')
        if parent_node.right is None:
            available_slots.append('right')
            
        chosen_slot = random.choice(available_slots)
        
        if chosen_slot == 'left':
            parent_node.left = new_node
        else:
            parent_node.right = new_node
            
        # 新しく追加したノードも、将来親になる可能性がある
        potential_parents.append(new_node)
        
        # 6. 親ノードの左右両方が埋まったら、親候補から除外する
        if parent_node.left is not None and parent_node.right is not None:
            potential_parents.remove(parent_node)
            
    return root

def print_tree(node, prefix="", is_left=True):
    """
    木の構造を分かりやすくコンソールに表示する関数
    """
    if not node:
        return

    if node.right:
        print_tree(node.right, prefix + ("│   " if is_left else "    "), False)

    print(prefix + ("└── " if is_left else "┌── ") + str(node.value))

    if node.left:
        print_tree(node.left, prefix + ("    " if is_left else "│   "), True)


# --- メインの実行ブロック ---
if __name__ == "__main__":
    try:
        num_of_nodes = int(input("生成したいノードの数を入力してください (例: 15): "))
        if num_of_nodes < 1:
            print("ノード数は1以上にしてください。")
        else:
            print(f"\n{num_of_nodes}個のノードを持つランダムな2分木を生成します...")
            random_tree_root = create_random_binary_tree(num_of_nodes)
            
            print("--- 生成された木の構造 ---")
            # 視覚的に見やすいように、木を90度回転させて表示します
            print_tree(random_tree_root)
            print("------------------------")

    except ValueError:
        print("無効な入力です。整数を入力してください。")
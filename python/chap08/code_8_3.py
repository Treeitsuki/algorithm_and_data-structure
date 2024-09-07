class Node:
    def __init__(self, name=""):
        self.next = None  # 次のNodeを指す
        self.name = name  # Nodeの名前

def insert(v, p):
    """Node p の後に Node v を挿入する"""
    v.next = p.next
    p.next = v

# 例: ノードを作成して挿入する
node1 = Node("first")
node2 = Node("second")
node3 = Node("third")

# node2 を node1 の後に挿入
insert(node2, node1)

# node3 を node1 の後に挿入 (結果として node3 が node1 の次、node2 はその次)
insert(node3, node1)

# ノードを順番に出力
current_node = node1
while current_node:
    print(current_node.name)
    current_node = current_node.next

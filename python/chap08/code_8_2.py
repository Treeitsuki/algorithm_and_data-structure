class Node:
    def __init__(self, name=""):
        self.next = None  # 次のNodeを指す
        self.name = name  # Nodeの名前

# 例: Nodeを作成して接続する
node1 = Node("first")
node2 = Node("second")
node1.next = node2  # node1の次をnode2に設定

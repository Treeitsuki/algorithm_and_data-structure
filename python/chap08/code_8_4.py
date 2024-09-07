class Node:
    def __init__(self, name=""):
        self.next = None  # 次のNodeを指す
        self.name = name  # Nodeの名前

# nil をグローバル変数として宣言
nil = None

def init():
    """リストの初期化。nil は自己参照するように設定"""
    global nil
    nil = Node()
    nil.next = nil  # リストの終わりを示す

def printList():
    """リストの要素を出力"""
    cur = nil.next
    while cur != nil:
        print(f"{cur.name} -> ", end="")
        cur = cur.next
    print()  # 改行

def insert(v, p=None):
    """p の次にノード v を挿入。p が指定されない場合は nil を使う"""
    if p is None:
        p = nil
    v.next = p.next
    p.next = v

# メイン処理
if __name__ == "__main__":
    # リストを初期化
    init()

    # 挿入する名前のリスト
    names = ["yamamoto", "watanabe", "ito", "takahashi", "suzuki", "sato"]

    # 各ノードを作成して挿入し、リストを出力
    for i, name in enumerate(names):
        node = Node(name)
        insert(node)

        # 現在のリストを出力
        print(f"step {i}: ", end="")
        printList()

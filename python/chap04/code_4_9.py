def func(i, w, a):
    # ベースケース
    if i == 0:
        return w == 0
    
    # a[i - 1]を選ばない場合
    if func(i -1, w, a):
        return True
    
    # a[i - 1]を選ぶ場合
    if func(i - 1, w - a[i - 1], a):
        return True
    
    # どちらも満たさない場合はfalse
    return False

def main():
    # 入力
    N = int(input())
    W = int(input())
    a = list(map(int, input().split()))
    
    # 再帰的に解く
    if func(N, W, a):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

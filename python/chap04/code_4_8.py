# フィボナッチ数列を求める再帰関数をメモ化
memo = [-1] * 50

def fibo(N):
    # ベースケース
    if N == 0:
        return 0
    elif N == 1:
        return 1
    
    # メモをチェック
    if memo[N] != -1:
        return memo[N]
    
    # メモを更新しながら再帰呼び出し
    memo[N] = fibo(N-1) + fibo(N-2)
    return memo[N]

def main():
    fibo(49)
    
    # memo[0], ..., memo[49] に答えが格納されている
    for N in range(2, 50):
        print(f"{N}項目: {memo[N]}")

if __name__ == '__main__':
    main()
# フィボナッチ数列を求める再帰関数
def fibo(N):
    # Nが0または1の場合
    if N == 0:
        return 0
    elif N == 1:
        return 1
    
    # 再帰呼び出し
    return fibo(N-1) + fibo(N-2)

def main():
    print(fibo(6))

if __name__ == '__main__':
    main()
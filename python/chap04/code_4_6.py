# フィボナッチ数列を求める再帰関数
def fibo(N):
    print(f"fibo({N})を呼び出しました")
    
    # Nが0または1の場合
    if N == 0:
        return 0
    elif N == 1:
        return 1
    
    # 再帰呼び出し
    result = fibo(N-1) + fibo(N-2)
    print(f"{N}項目 = {result}")
    
    return result

    
def main():
    fibo(6)

if __name__ == '__main__':
    main()
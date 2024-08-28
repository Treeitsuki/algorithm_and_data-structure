def main():
    INF = 2000000000    # 十分大きな値に設定
    
    N, v = map(int, input().split())
    a = list(map(int, input().split()))

    # 線形探索
    min_value = INF
    for num in a:
        if num < min_value:
            min_value = num

    print(min_value)

if __name__ == '__main__':
    main()
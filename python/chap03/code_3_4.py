def main():
    INF = 2000000000
    
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    min_value = INF
    for ai in a:
        for bj in b:
            #K未満の場合はスキップ
            if ai + bj < K:
                continue
            
            #最小値を更新
            if ai + bj < min_value:
                min_value = ai + bj

    print(min_value)

if __name__ == '__main__':
    main()
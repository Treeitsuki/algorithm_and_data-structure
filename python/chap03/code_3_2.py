def main():
    N, v = map(int, input().split())
    a = list(map(int, input().split()))

    # 線形探索
    found_id = -1
    for i in range(N):
        if a[i] == v:
            found_id = i
            break
    
    print(found_id)

if __name__ == '__main__':
    main()
def main():
    N, W = map(int, input().split())
    a = list(map(int, input().split()))

    # ビット全探索
    exist = False
    for bit in range(1 << N):
        sum = 0 # 部分集合に含まれる要素の和
        for i in range(N):
            if bit & (1 << i): # i が部分集合に含まれるかどうか
                sum += a[i]

        if sum == W:
            exist = True
            break
    
    if exist:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
def main():
    N, v = map(int, input().split())
    a = list(map(int, input().split()))

    # 線形探索
    exist = False
    for num in a:
        if num == v:
            exist = True
            break
    
    if exist:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
# ユークリッドの互除法によって最大公約数を求める
def gcd(m, n):
    # nが0の場合は、mを返す
    if n == 0:
        return m
    else:
        return gcd(n, m % n)
    
def main():
    print(gcd(51, 15))
    print(gcd(15, 51))

if __name__ == '__main__':
    main()
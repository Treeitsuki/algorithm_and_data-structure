import math

# 2点 (x1, y1) と (x2, y2) の間の距離を計算する関数
def calc_dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def main():
    N = int(input())
    x = []
    y = []
    
    for _ in range(N):
        x_val, y_val = map(float, input().split())
        x.append(x_val)
        y.append(y_val)
        
    #最小距離を非常に大きな数で初期化
    minimum_dist = 10**9
    
    #全ての点の組み合わせに対して距離を計算
    for i in range(N):
        for j in range(i + 1, N):
            dist_i_j = calc_dist(x[i], y[i], x[j], y[j])
            
            #最小距離を更新
            if dist_i_j < minimum_dist:
                minimum_dist = dist_i_j

    #最小距離を出力
    print(minimum_dist)
    
if __name__ == '__main__':
    main()
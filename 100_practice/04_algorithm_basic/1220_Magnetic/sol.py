import sys
sys.stdin = open("input.txt", 'r')

def magnetic_count(data):
    total_count = 0
    for j in range(100):
        magnetic = False
        for i in range(100):
            if data[i][j] == 1:
                magnetic = True
            elif magnetic and data[i][j] == 2:
                total_count += 1
                magnetic = False
    return total_count

tc = 0
while True:
    try:
        data = []
        tc += 1
        T = int(input())    # T = 100
        for _ in range(T):
            arr = list(map(int, input().split()))
            data.append(arr)
        cnt = magnetic_count(data)
        print(f'#{tc} {cnt}')
    except EOFError:
        break
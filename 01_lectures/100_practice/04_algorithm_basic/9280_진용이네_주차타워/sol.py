import sys
sys.stdin = open("sample_input.txt", "r")

from collections import deque

def parking_log(n, m, Ri, Wi, inout):
    # 주차장 상태 - 비어 있음
    parking_lot = [None] * n
    # 대기열 - 주차 공간 없을 때
    wait_queue = deque()
    # 차량이 주차되어 있는 상태
    car_pos = dict()
    # 총 요금
    total_fee = 0

    for event in inout:

        if event > 0:
            car_num = event - 1
            slot_index = -1
            for i in range(n):
                # 비어 있는 주차 공간 찾기
                if parking_lot[i] is None:
                    slot_index = i
                    break
                    
            if slot_index != -1:
                parking_lot[slot_index] = car_num
                car_pos[car_num] = slot_index
                total_fee += Ri[slot_index] * Wi[car_num]
            else:
                wait_queue.append(car_num)
        else:
            car_num = abs(event) - 1
            slot_index = car_pos[car_num]
            parking_lot[slot_index] = None
            del car_pos[car_num]

            if wait_queue:
                next_car = wait_queue.popleft()
                parking_lot[slot_index] = next_car
                car_pos[next_car] = slot_index
                total_fee += Ri[slot_index] * Wi[next_car]

    return total_fee

TC = int(input())
for tc in range(1, TC+1):
    n, m = map(int, input().split())
    Ri = [int(input()) for _ in range(n)]
    Wi = [int(input()) for _ in range(m)]
    inout = [int(input()) for _ in range(2 * m)]
    result = parking_log(n, m, Ri, Wi, inout)
    print(f"#{tc} {result}")
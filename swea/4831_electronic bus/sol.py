import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # K : 이동가능정류장수
    # N : 정류장 갯수
    # M : 충전기 갯수
    K, N, M = list(map(int, input().split()))
    b = list(map(int, input().split())) # 충전정류장 번호

    charge = 0
    now = 0
   # 충전할 필요가 없이 도착하는 경우
    if K >= N :
        charge = 0
    
    # 충전하면서 지나가야 하는 경우
    else:
        # 버스가 아직 종점에 도착하지 않았다면 계속 반복
        while now < N:
            # 현재 위치(now)를 기준으로 최대로 갈 수 있는 범위를 찾는다.
            for i in range(now+K, now, -1):
                # 1. 최대 범위가 종점을 넘는 경우
                if i >= N:
                    now = N
                    break
                # 2, 최대 범위가 종점을 넘지 않는 경우
                if i in b:
                    now = i
                    charge += 1
                    break

                # 현재 위치에서 최대거리까지 다 확인을 했는데 충전소가 없다면 충전 불가능
            else:
                charge = 0
                now = N

    print(f'#{tc} {charge}')
n,m,h,k = list(map(int, input().split()))
runner = {}
dr = [-1, 0, 1, 0]
dc = [0,1,0,-1]
arr = [[0] * n for _ in range(n)]
for i in range(m):
    x, y, d = map(int, input().split())
    runner[i] = [x-1, y-1, d]

for _ in range(h):
    ti, tj = map(lambda x: int(x)-1, input().split())
    arr[ti][tj] = -1 # 나무 위치 표시

turn = []
for i in range(1, n):
    turn.append(i)
    turn.append(i)
turn.append(n-1)

turn_idx=0
turn_cnt = 0
si, sj, sd = n//2, n//2, 0

ans=0
for t in range(1, k+1):
    # 도망자 이동
    catch=0
    for runner_idx in runner:
        ci, cj, d = runner[runner_idx]
        dist = abs(ci - si) + abs(cj - sj)
        if dist>3: continue
        nr, nc = ci+dr[d], cj+dc[d]
        if (nr, nc) == (si, sj): continue # 술래이면

        if 0<=nr<n and 0<=nc<n: # 좌표 내 이면
            runner[runner_idx] = [nr, nc, d]
        else: # 좌표 바깥이면
            nd = (d+2)%4
            nr = ci + dr[nd]
            nc = cj + dc[nd]
            if (nr, nc) == (si, sj): continue # 술래이면
            runner[runner_idx] = [nr, nc, nd]
    
    # 술레이동
    si, sj = si+dr[sd], sj+dc[sd]
    turn_cnt+=1
    if (si, sj) == (0,0) or (si, sj) == (n//2, n//2):
        turn = turn[::-1]
        sd = (sd+2)%4
        turn_cnt=0
        turn_idx=0
    elif turn_cnt == turn[turn_idx]:
        sd =(sd+1)%4
        turn_cnt=0
        turn_idx+=1
    
    # 제거하자
    for mul in range(3):
        tr, tc = si +dr[sd] * mul, sj +dc[sd]*mul
        if tr <0 or tr>=n or tc<0 or tc>=n: continue
        if arr[tr][tc] == -1: continue #나무 일 때

        for runner_idx in list(runner.keys()):
            ri, ci, d = runner[runner_idx]
            if tr == ri and tc == ci:
                runner.pop(runner_idx)
                catch+=1

    ans = ans + t*catch

print(ans)


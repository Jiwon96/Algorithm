N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
move_dist = [0] * M
participant = {}
for i in range(M):
    participant[i] = list(map(lambda x: int(x) -1, input().split()))
exit_pos = list(map(lambda x: int(x) -1, input().split()))

dr = [-1, 1, 0, 0, 0]
dc = [0,0,-1,1, 0]

# 좌 상단을 좌표를 구하는
def get_min_pos(diff_dist):
    for init_r in range(exit_pos[0] - diff_dist, exit_pos[0] + 1):
        for init_c in range(exit_pos[1] - diff_dist, exit_pos[1] + 1):
            if 0<= init_r  < N and 0<=init_c < N and 0<=init_r + diff_dist <N and 0<=init_c+diff_dist<N:
                for pp in participant:
                    if init_r<=participant[pp][0]<=init_r+diff_dist and init_c<=participant[pp][1]<=init_c+diff_dist:
                        return (init_r, init_c)


def transpose_pos(r, c, ti, tj, diff_dist):
    temp = ti
    ti = tj
    tj = diff_dist - temp
    #participant[pi] = [ti + r, tj + c]
    return [ti+r, tj+c]

for k in range(1, K+1):
    for part_idx in participant:
        min_dist = abs(exit_pos[0] - participant[part_idx][0]) + abs(exit_pos[1] - participant[part_idx][1])
        min_dir = 4 #원래 자리
        for d in range(4):
            nr, nc = participant[part_idx][0] + dr[d], participant[part_idx][1] + dc[d]
            if 0<=nr<N and 0<=nc<N and arr[nr][nc] == 0: #범위 안이고, 벽이 아니면
                dist = abs(nr - exit_pos[0]) + abs(nc - exit_pos[1])
                if min_dist > dist:
                    min_dist = dist
                    min_dir = d
                elif min_dist == dist:
                    min_dir = min(min_dir, d)
        if min_dir == 4:
            continue
        move_dist[part_idx]+=1
        participant[part_idx] = [participant[part_idx][0] + dr[min_dir], participant[part_idx][1] + dc[min_dir]]
    
    
    #도착했으면 끝
    for part_idx in list(participant.keys()):
        if [participant[part_idx][0], participant[part_idx][1]] == exit_pos:
            participant.pop(part_idx)
    
    if len(participant) ==0:
        break


    diff_dist = 2*(N+1)
    for part_idx in participant:
        diff_dist = min(diff_dist ,max(abs(participant[part_idx][0] - exit_pos[0]), abs(participant[part_idx][1] - exit_pos[1])))
    r, c = get_min_pos(diff_dist)

    temp_arr = [arr[tr][c:c+diff_dist+1] for tr in range(r, r+diff_dist+1)]
    temp_arr = list(map(list, zip(*temp_arr[::-1])))

    for i in range(diff_dist+1):
        temp_arr[i] = list(map(lambda x: max(0, x-1), temp_arr[i]))
    
    for idx in range(diff_dist+1):
        arr[r+idx][c:c+diff_dist+1] = temp_arr[idx]
    ## 위치 변경하기 90도 회전
    for pi in participant:
        if r <= participant[pi][0] <= r + diff_dist and c <= participant[pi][1] <= c + diff_dist:
            participant[pi] = transpose_pos(r, c, participant[pi][0] - r, participant[pi][1] - c, diff_dist)

    exit_pos = transpose_pos(r, c, exit_pos[0] - r, exit_pos[1] - c, diff_dist)

print(sum(move_dist))
print(exit_pos[0] +1, exit_pos[1]+1)
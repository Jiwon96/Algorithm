N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans=0

def bfs(i, j, v, g):
    q =[]
    v[i][j] = g
    q.append((i,j))
    cnt=1
    while q:
        ri, ci = q.pop(0)
        for di, dj in ((-1, 0), (1,0), (0,-1),(0, 1)):
            nr, nc = ri+di, ci+dj
            if 0<=nr<N and 0<=nc<N and v[nr][nc] == -1 and arr[i][j] == arr[nr][nc]:
                v[nr][nc] = g
                cnt+=1
                q.append((nr, nc))

    return cnt

def rotate(si, sj, N, tarr):
    narr = [x[:] for x in tarr]
    for i in range(N):
        for j in range(N):
            narr[si+i][sj + j] = tarr[si+N-1-j][sj+i]
    return narr

for rotate_cnt in range(4): # i번 회전
    g=0
    group_num = []  # 그룹 i를 이루고 있는 숫자값
    v = [[-1] * N for _ in range(N)]  # 그룹 숫자 나타내는 변수
    arr_num = []
    # 그룹 만들기
    for i in range(N):
        for j in range(N):
            if v[i][j] == -1:
                cnt = bfs(i, j, v, g) # 그룹만들기
                group_num.append(cnt)
                arr_num.append(arr[i][j])
                g+=1


    # 그룹  i,j에 해당되는 그룹 변수 구하기
    group_edge =[[0] * g for _ in range(g)]
    #변수 구하기
    for ri in range(N):
        for ci in range(N):
            for di, dj in ((-1, 0), (1,0), (0, -1),(0,1)):
                nr, nc = ri+di, ci+dj
                if 0<=nr<N and 0<=nc<N and v[ri][ci] != v[nr][nc]:
                    group_edge[v[ri][ci]][v[nr][nc]] +=1
    
    # 점수 구하기

    temp = 0
    for i in range(g):
        for j in range(i, g):
            if group_edge[i][j]>0:
                temp+=((group_num[i] + group_num[j]) * arr_num[i] * arr_num[j]*group_edge[i][j])

    # 52 96 144 42
    ans+=temp

    # rotate
    half_n = N//2
    narr = [x[:] for x in arr]
    for i in range(1, half_n+1):
        for di, dj in ((-1, 0), (1,0),(0, -1), (0,1)):
            ri, ci = half_n + di * i, half_n + dj*i
            narr[ri][ci] = arr[ci][N-1-ri]

    narr = rotate(0, 0, half_n, narr)
    narr = rotate(half_n+1, 0, half_n, narr)
    narr = rotate(0,half_n+1,half_n, narr)
    narr = rotate(half_n+1, half_n + 1, half_n, narr)

    arr = narr

print(ans)
L, N, Q = map(int, input().split())
arr = [[2] * (L+2)] + [[2] + list(map(int, input().split())) + [2] for _ in range(L)] + [[2] * (L+2)]
units={}
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
init_k = [0] * (N+1)
v = [[0] * (L+2) for _ in range(L+2)]

for knight_idx in range(1, N+1):
    r,c,h,w,k = map(int, input().split())
    units[knight_idx] = [r,c,h,w,k]
    init_k[knight_idx] = k
    for i in range(r, r+h):
        v[i][c:c+w] = [knight_idx] * w

def push_unit(start, dr):
    q=[]
    pset = set()
    damage = [0] * (N+1)

    q.append(start)
    pset.add(start)
    while q:
        cur = q.pop(0)
        ci, cj, h, w, k = units[cur]

        ni, nj = ci+di[dr], cj+dj[dr]
        for i in range(ni, ni+h):
            for j in range(nj, nj+w):
                if arr[i][j] == 2:
                    return
                if arr[i][j] == 1:
                    damage[cur]+=1

        for idx in units:
            if idx in pset: continue

            ti, tj, th, tw, tk = units[idx]

            if ni<=ti+th-1 and nj <= tj+tw-1 and ni + h-1 >= ti  and nj+w-1 >= tj:
                q.append(idx)
                pset.add(idx)
    damage[start] = 0

    for idx in pset:
        si,sj,h,w,k = units[idx]
        for i in range(si, si + h):
            v[i][sj:sj + w] = [0] * w  # 기존위치 지우기
    for idx in pset:
        si, sj, h, w, k = units[idx]

        if k <= damage[idx]:  # 체력보다 더 큰 데미지면 삭제
            units.pop(idx)
        else:
            ni, nj = si + di[dr], sj + dj[dr]
            units[idx] = [ni, nj, h, w, k - damage[idx]]
            for i in range(ni,ni+h):
                v[i][nj:nj+w]=[idx]*w     # 이동위치에 표시

for _ in range(Q):
    idx, dr = map(int, input().split())

    ### 왜 이렇게 함수화를 했을까?

    ### check 이후 연산을 했어야함. -> 만약에 check가 False이면 연산을 하지 않는 코드가 들어가야됨. -> loop break가 쓰이는데 이는 굉장히 지저분하다.

    if idx in units:
        push_unit(idx, dr)

ans = 0
for idx in units:
    ans+=init_k[idx]-units[idx][4]
print(ans)


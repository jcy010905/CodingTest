from collections import deque

def solution(n, m, hole):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 지도 생성 및 함정 표시
    graph = [[0] * m for _ in range(n)]
    for a, b in hole:
        graph[a-1][b-1] = 1  # 함정은 1로 표시

    # BFS 큐 및 방문 배열 초기화
    queue = deque()
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]  # [신발 사용 여부에 따라 방문 체크]
    visited[0][0][False] = True  # 시작점은 신발을 사용하지 않은 상태로 방문 처리
    queue.append((0, 0, False))  # (x 좌표, y 좌표, 신발 사용 여부)

    L = 0  # 탐색 깊이 (최단 경로 길이)

    while queue:
        for _ in range(len(queue)):
            x, y, used = queue.popleft()

            # 상하좌우로 이동
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                # 보드 경계 안에 있고, 아직 방문하지 않았으며, 함정이 없는 경우
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][used] and graph[nx][ny] == 0:
                    # 목적지 도착 시
                    if (nx, ny) == (n - 1, m - 1):
                        return L + 1
                    visited[nx][ny][used] = True
                    queue.append((nx, ny, used))

            # 신발을 사용하면서 두 칸 이동
            if not used:
                for i in range(4):
                    nx = x + 2 * dx[i]
                    ny = y + 2 * dy[i]
                    
                    # 보드 경계 안에 있고, 아직 방문하지 않았으며, 함정이 없는 경우
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][True] and graph[nx][ny] == 0:
                        # 목적지 도착 시
                        if (nx, ny) == (n - 1, m - 1):
                            return L + 1
                        visited[nx][ny][True] = True
                        queue.append((nx, ny, True))

        L += 1  # 탐색 깊이를 증가시킴

    return -1  # 목적지에 도달할 수 없는 경우

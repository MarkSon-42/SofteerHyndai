# comments by chatGPT

# deque 클래스를 불러옴. 이는 BFS에 필요한 큐(queue)를 구현하기 위함입니다.
from collections import deque

# Python의 표준 입력 라이브러리를 불러옴.
import sys

# 입력을 더 빠르게 받기 위해 sys.stdin.readline()을 사용함.
input = sys.stdin.readline

# 사용자로부터 정사각형 맵의 크기 n을 입력 받음.
n = int(input())

# 그래프를 입력 받음. 각 줄을 rstrip()으로 끝의 개행문자를 제거하고, map 함수로 int형으로 변환한 뒤, 리스트로 만듬.
graph = [list(map(int, input().rstrip())) for _ in range(n)]

# 결과를 담을 리스트 초기화.
result = []

# 네 방향(상하좌우)을 탐색하기 위한 좌표의 변화값을 정의.
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs 함수를 정의.
def bfs(i, j):
    # 빈 deque를 생성함. 이는 BFS에 사용될 큐(queue)임.
    queue = deque()
    queue.append((i, j)) # 시작 노드를 큐에 넣음.
    graph[i][j] = 0 # 시작 노드를 방문 표시.
    cnt = 1 # 방문한 노드의 수를 세기 위한 카운터 초기화.

    while queue: # 큐가 빌 때까지
        x, y = queue.popleft() # 큐에서 노드를 하나 꺼냄.
        for k in range(4): # 네 방향에 대해
            nx = x + dx[k] # 다음 노드의 x 좌표를 계산
            ny = y + dy[k] # 다음 노드의 y 좌표를 계산
            # 만약 다음 노드가 그래프의 범위 내에 있고 아직 방문하지 않은 노드라면
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                queue.append((nx, ny)) # 큐에 넣고
                graph[nx][ny] = 0 # 방문 표시를 하고
                cnt += 1 # 카운터를 증가시킴.
    return cnt # 모든 인접한 노드를 방문한 후, 방문한 노드의 수를 반환함.

# 그래프의 모든 노드에 대해
for i in range(n):
    for j in range(n):
        # 만약 해당 노드가 아직 방문하지 않은 노드라면
        if graph[i][j] == 1:
            result.append(bfs(i, j)) # BFS를 수행하고 그 결과를 결과 리스트에 추가함.

# 결과를 정렬함.
result.sort()
print(len(result))
for i in result:
    print(i)

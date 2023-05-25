# dfs로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 종료
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False
    # 현재 노드들 아직 방문하지 않았다면
    if graph[x][y] == 1:
        # 장애물의 개수 체크
        cnt.append(1)
        # 해당 노드 방문 처리
        graph[x][y] = 0
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False



N = int(input())
cnt = []

graph = []
# 모든 위치(노드)에 대하여 장애물 블록을 만듬.
for i in range(N):
    graph.append(list(map(int, input())))

result = 0
result_list = []
for i in range(N):
    for j in range(N):
    # 현재 위치에서 DFS수행
        if dfs(i, j) == True:
            result += 1
            # 길이를 통해 장애물의 개수 확인
            result_list.append(len(cnt))
            cnt = []

# 장애물의 수 오름차순 정렬 후 출력
result_list.sort()
for i in result_list:
    print(i)


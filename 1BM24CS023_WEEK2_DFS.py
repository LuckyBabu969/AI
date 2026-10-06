from copy import deepcopy
moves=[(1,0),(-1,0),(0,1),(0,-1)]
def successor(state):
    for i in range(3):
        for j in range(3):
            if state[i][j]==0:
                x,y=i,j
    result=[]
    for dx,dy in moves:
        nx,ny=x+dx,y+dy
        if 0<=nx<3 and 0<=ny<3:
            new=deepcopy(state)
            new[x][y],new[nx][ny]=new[nx][ny],new[x][y]
            result.append(new)
    return result
def dfs(state,goal,path,visited):
    if state==goal:
        path.append(state)
        return True
    visited.add(tuple(map(tuple,state)))
    for next_state in successor(state):
        key=tuple(map(tuple,next_state))
        if key not in visited:
            path.append(state)
            if dfs(next_state,goal,path,visited):
                return True
            path.pop()
    return False
def display(state):
    for row in state:
        print(*row)
    print()
start=[[1,2,3],[4,0,6],[7,5,8]]
goal=[[1,2,3],[4,5,6],[7,8,0]]
path=[]
print("Initial State:")
display(start)
print("Goal State:")
display(goal)
if dfs(start,goal,path,set()):
    print("Solution Path:")
    for state in path:
        display(state)
else:
    print("No solution")
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
def dls(state,goal,depth,path,visited):
    if state==goal:
        path.append(state)
        return True
    if depth==0:
        return False
    visited.add(tuple(map(tuple,state)))
    for next_state in successor(state):
        key=tuple(map(tuple,next_state))
        if key not in visited:
            path.append(state)
            if dls(next_state,goal,depth-1,path,visited):
                return True
            path.pop()
    visited.remove(tuple(map(tuple,state)))
    return False
def ids(start,goal):
    depth=0
    while True:
        path=[]
        if dls(start,goal,depth,path,set()):
            return path
        depth+=1
def display(state):
    for row in state:
        print(*row)
    print()
start=[[1,2,3],[4,0,6],[7,5,8]]
goal=[[1,2,3],[4,5,6],[7,8,0]]
print("Initial State:")
display(start)
print("Goal State:")
display(goal)
path=ids(start,goal)
print("Solution Path:")
for state in path:
    display(state)
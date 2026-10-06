import heapq
GOAL=(1,2,3,4,5,6,7,8,0)
def misplaced_tiles(state):
    count=0
    for i in range(9):
        if state[i]!=0 and state[i]!=GOAL[i]:
            count+=1
    return count
def get_neighbors(state):
    neighbors=[]
    zero=state.index(0)
    row=zero//3
    col=zero%3
    if row>0:
        new_state=list(state)
        new_state[zero],new_state[zero-3]=new_state[zero-3],new_state[zero]
        neighbors.append(tuple(new_state))
    if row<2:
        new_state=list(state)
        new_state[zero],new_state[zero+3]=new_state[zero+3],new_state[zero]
        neighbors.append(tuple(new_state))
    if col>0:
        new_state=list(state)
        new_state[zero],new_state[zero-1]=new_state[zero-1],new_state[zero]
        neighbors.append(tuple(new_state))
    if col<2:
        new_state=list(state)
        new_state[zero],new_state[zero+1]=new_state[zero+1],new_state[zero]
        neighbors.append(tuple(new_state))
    return neighbors
def a_star(start):
    pq=[]
    heapq.heappush(pq,(misplaced_tiles(start),0,start,[]))
    visited=set()
    while pq:
        f,g,state,path=heapq.heappop(pq)
        if state in visited:
            continue
        visited.add(state)
        if state==GOAL:
            return path,g
        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                new_g=g+1
                new_f=new_g+misplaced_tiles(neighbor)
                heapq.heappush(pq,(new_f,new_g,neighbor,path+[neighbor]))
    return None,-1
def print_board(state):
    for i in range(0,9,3):
        print(state[i:i+3])
    print()
start=(1,2,3,4,0,6,7,5,8)
print("Initial State:")
print_board(start)
print("MISPLACED TILES")
path,cost=a_star(start)
if path is not None:
    print("Solution:")
    print_board(start)
    for state in path:
        print_board(state)
    print("Number of moves:",cost)
else:
    print("No solution found.")
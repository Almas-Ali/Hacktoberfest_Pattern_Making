import copy
start_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
goal_state = [[2, 8, 1], [0, 4, 3], [7, 6, 5]]
q = []
cnt = 1


def find_pos(start):
    for i in range(len(start)):
        for j in range(len(start[i])):
            if start[i][j] == 0:
                return (i, j)


def compare(curr, goal):
    if curr == goal:
        return 1
    else:
        return 0


def up(state, u, v):
    state[u][v] = state[u-1][v]  # up
    state[u-1][v] = 0
    return state


def right(state, l, m):
    state[l][m] = state[l][m+1]  # right
    state[l][m+1] = 0
    return state


def left(state, n, o):
    state[n][o] = state[n][o-1]  # left
    state[n][o-1] = 0
    return state


def down(state, r, s):
    state[r][s] = state[r+1][s]  # down
    state[r+1][s] = 0
    return state


def states(start, goal):
    pos = find_pos(start)
    i = pos[0]
    j = pos[1]
    global cnt
    if i-1 >= 0:
        state_1 = copy.deepcopy(start)
        state1 = up(state_1, i, j)
        if compare(state1, goal):
            print(cnt)
            print(state1)
            return 1
        else:
            if state1 not in q:
                q.append(state1)
                cnt += 1

    if j+1 <= 2:
        state_2 = copy.deepcopy(start)
        state2 = right(state_2, i, j)
        if compare(state2, goal):
            print(cnt)
            print(state2)
            return 1
        else:
            if state2 not in q:
                q.append(state2)
                cnt += 1

    if j-1 >= 0:
        state_3 = copy.deepcopy(start)
        state3 = left(state_3, i, j)
        if compare(state3, goal):
            print(cnt)
            print(state3)
            return 1
        else:
            if state3 not in q:
                q.append(state3)
                cnt += 1

    if i+1 <= 2:
        state_4 = copy.deepcopy(start)
        state4 = down(state_4, i, j)
        if compare(state4, goal):
            print(cnt)
            print(state4)
            return 1

        else:
            if state4 not in q:
                q.append(state4)
                cnt += 1


def func():
    if not compare(start_state, goal_state):
        q.append(start_state)
    i = 0
    while(q):
        spop = q[i]
        i += 1
        if(states(spop, goal_state)):
            break


func()
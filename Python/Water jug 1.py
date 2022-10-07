x = 0
y = 0

state = [[0, 0]]

while(x != 2):
    if [4, y] not in state and x < 4:
        x = 4
        state.append([x, y])
        print(x, y)
    if [x, 3] not in state and y < 3:
        y = 3
        state.append([x, y])
        print(x, y)
    if [0, y] not in state and x > 0:
        x = 0
        state.append([x, y])
        print(x, y)
    if [x, 0] not in state and y > 0:
        y = 0
        state.append([x, y])
        print(x, y)
    if [4, y-(4-x)] not in state and x+y >= 4 and y > 0:
        y = y-(4-x)
        x = 4
        state.append([x, y])
        print(x, y)
    if [x-(3-y), 3] not in state and x+y >= 3 and x > 0:
        x = x-(3-y)
        y = 3
        state.append([x, y])
        print(x, y)
    if [x+y, 0] not in state and (x+y) <= 4 and y >= 0:
        x = x+y
        y = 0
        state.append([x, y])
        print(x, y)
    if [0, y+x] not in state and (x+y) <= 3 and x >= 0:
        y = x+y
        x = 0
        state.append([x, y])
        print(x, y)
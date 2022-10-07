x = 12
y = 0
z = 0
state = [[12,0,0]]

while(x != 6):
    if [x-(8-y), 8, z] not in state and x+y >= 8 and x > 0:
        x = x-(8-y)
        y = 8
        state.append([x, y, z])
        print(x, y, z)
    if [x, y-(5-z), 5] not in state and y+z >= 5 and y > 0:
        y = y-(5-z)
        z = 5
        state.append([x, y, z])
        print(x, y, z) 
    if [x+z, y, 0] not in state and (x+z) <= 12 and z >= 0:
        x = x+z
        z = 0
        state.append([x, y, z])
        print(x, y, z)
    if [x, 0, z] not in state and y > 0:
        y = 0
        state.append([x, y, z])
        print(x, y, z)
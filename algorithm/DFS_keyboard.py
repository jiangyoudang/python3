

# return possible result
def find(keyboard, pos, visited, res):
    directions = [
        (1,1), (1,0), (1, -1),
        (0,1), (0,-1),
        (-1, 0), (-1, 1), (-1,-1)
                  ]
    has_space = False

    for direction in directions:
        x,y = pos
        xd, yd = direction
        x, y = x+xd, y+yd

        if 0<= x < len(keyboard) and 0 <= y < len(keyboard):
            if (x,y) not in visited:
                has_space = True
                visited.append((x,y))
                find(keyboard, (x,y), visited, res)
                visited.pop()

    if not has_space:
        res.append(''.join([keyboard[p[0]][p[1]] for p in visited]))

keyboard = ['123','456','789']
# keyboard = ['12','34']

res = []
for i in range(len(keyboard)):
    for j in range(len(keyboard[0])):
        find(keyboard, (i,j), [(i,j)], res)

print(res)
print(len(res))
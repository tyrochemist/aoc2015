floor = 0
position = 0
with open('input.txt') as directions_raw:
    directions = directions_raw.read()
for count, i in enumerate(directions):
    if i == '(':
        floor += 1
    elif i == ')':
        floor -= 1
    if floor < 0:
        position = count+1
        break
print(f'First enter basement at position {position}')

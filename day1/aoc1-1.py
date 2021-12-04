floor = 0
with open('input.txt') as directions_raw:
    for i in directions_raw.read():
        if i == '(':
            floor += 1
        elif i == ')':
            floor -= 1

print(f'Go to floor {floor}')

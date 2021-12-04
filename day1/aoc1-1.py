with open('input.txt') as directions_raw:
    directions = directions_raw.read()
floor = directions.count('(') - directions.count(')')
print(f'Go to floor {floor}')

import random as rd
HERO = {
    'Name': '',
    'Health': 100,
    'Inventory': {
                'Sword': 25,
                'Health Flask': 30
                },
    'Armor':25,
    'Model': '$',
    'Base damage': 25,
    'Luck': rd.randint(0, 3),
    'Position': [0, 0]
}

ENEMY = {
    'Health': 100,
    'Inventory':{
        'Morgen': 35,
        'Health Flask': 30
                },
    'Armor': 10,
    'Model': '@',
    'Base damage': 20,
}

HERO['Name'] = str(input("Введите имя героя: "))

# Старт игры
Drop = ['Граль','мусор','мусор','Амулет','мусор','мусор','Ожирелье','мусор']
HEALTH_HERO = HERO['Health'] + (HERO['Armor'] * 0.75)
DAMAGE_HERO = HERO['Inventory']['Sword'] + HERO['Base damage']

HEALTH_ENEMY = ENEMY['Health'] + (ENEMY['Armor']*1.25)
DAMAGE_ENEMY = ENEMY['Inventory']['Morgen']+ENEMY['Base damage']

Flask_HERO = HERO['Inventory']['Health Flask']
Flask_ENEMY = ENEMY['Inventory']['Health Flask']

model_health = '+'
HEALTH_BAR_HERO = HERO['Health']//10
HEALTH_BAR_ENEMY = HERO['Health']//10
BAR_HERO = f'{HERO["Name"]}\n{model_health*HEALTH_BAR_HERO}\n'
BAR_ENEMY = f'ENEMY\n{model_health*HEALTH_BAR_ENEMY}\n'

print(HEALTH_BAR_ENEMY)
print(HEALTH_BAR_HERO)

# Боевка
MAP = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    ]
counter_hero = 0
counter_enemys = 0
while counter_hero != 1 and counter_enemys != 3:
    for y in range(5):
        for x in range(5):
            if rd.randint(1, 50) in [10,25,50,20,30,35]:
                if rd.randint(0, 1) == 1:
                    if counter_hero < 1:
                        MAP[y-1][x-1] = HERO['Model']
                        HERO['Position'] = [x, y]
                        counter_hero+=1
                    else:
                        if counter_enemys < 5:
                            MAP[y][x] = ENEMY['Model']
                            counter_enemys += 1
temp = 0
while True:
    for i in MAP:
        print('\n')
        for j in i:
            print(''.join(str(j)), end='\t')
        
    print(HERO['Position'], 'Позиция героя')
    #Позиционирование - print(HERO['Position'])
    x = HERO['Position'][1]
    y = HERO['Position'][0]
    MAP_fight = MAP
    fight = False
    if MAP_fight[y+1][x] == '@':
        MAP_fight[y+1][x] = 0
        fight = True
    if MAP_fight[y-1][x] == '@':
        MAP_fight[y-1][x] = 0
        fight = True
    if MAP_fight[y][x+1] == '@':
        MAP_fight[y][x+1] = 0
        fight = True
    if MAP_fight[y][x-1] == '@':
        MAP_fight[y][x-1] = 0
        fight = True
    if MAP_fight[y+1][x] == '$':
        MAP_fight[y+1][x] = 0
    if MAP_fight[y-1][x] == '$':
        MAP_fight[y-1][x] = 0
    if MAP_fight[y][x+1] == '$':
        MAP_fight[y][x+1] = 0
    if MAP_fight[y][x-1] == '$':
        MAP_fight[y][x-1] = 0
    print(fight, MAP_fight[y][x])
    if fight:
        while True:
            if (HEALTH_HERO > 1) and (HEALTH_ENEMY > 1):
                Drop = ['Кинжал','мусор','мусор','Топор','мусор','мусор','мусор','мусор']
                HEALTH_HERO = HERO['Health'] + (HERO['Armor'] * 0.25)
                DAMAGE_HERO = HERO['Inventory']['Sword'] + HERO['Base damage']

                HEALTH_ENEMY = ENEMY['Health'] + (ENEMY['Armor']*1.25)
                DAMAGE_ENEMY = ENEMY['Inventory']['Morgen']+ENEMY['Base damage']

                Flask_HERO = HERO['Inventory']['Health Flask']
                Flask_ENEMY = ENEMY['Inventory']['Health Flask']
                if rd.randint(1,7) in [6,1,2]:
                    ENEMY['Health'] -= DAMAGE_HERO
                    ENEMY['Armor'] = ENEMY['Armor'] - (ENEMY['Armor'] * 0.25)
                    if ENEMY['Health'] <= 20:
                        ENEMY['Health'] += Flask_ENEMY
                else:
                    HERO['Health'] -= DAMAGE_ENEMY
                    HERO['Armor'] = HERO['Armor'] - (HERO['Armor'] * 0.25)
                    if HERO['Luck'] >= 2:
                        HERO['Health'] += Flask_HERO
                    if HERO['Health'] <= 20:
                        HERO['Health'] += Flask_HERO
            else:
                if HERO['Health'] > ENEMY['Health']:
                    HERO['Health'] += (100 * 0.1)
                    print('You win')
                    print('Здоровье героя:', HERO['Health'])
                    HERO['Inventory'][Drop[rd.randint(0, 7)]] = 0
                    print(HERO['Inventory'])
                    break
                else:
                    print('Game Over')
                    print('Здоровье врага:',ENEMY['Health'])
                    break
    if HERO['Health'] <= 0:
        break
    else:
        move = input('\n\n(Ваши дейтсвия:)\n 1)сходить налево\n 2)сходить направо\n 3)Сходить вниз\n 4)Сходить вверх\n-->')
        if move == '1':
            temp = HERO['Position']
            if temp[1] > 0:
                MAP[temp[0]][temp[1]] = 0
                MAP[temp[0]][temp[1]-1] = HERO['Model']
                HERO['Position'] = [temp[0],temp[1]-1]
        elif move == '2':
            temp = HERO['Position']
            if temp[1] < 4:
                MAP[temp[0]][temp[1]] = 0
                MAP[temp[0]][temp[1]+1] = HERO['Model']
                HERO['Position'] = [temp[0],temp[1]+1]
        elif move == '3':
            temp = HERO['Position']
            if temp[0] < 4:
                MAP[temp[0]][temp[1]] = 0
                MAP[temp[0]+1][temp[1]] = HERO['Model']
                HERO['Position'] = [temp[0]+1,temp[1]]
        elif move == '4':
            temp = HERO['Position']
            if temp[0] > 0:
                MAP[temp[0]][temp[1]] = 0
                MAP[temp[0]-1][temp[1]] = HERO['Model']
                HERO['Position'] = [temp[0]-1,temp[1]]
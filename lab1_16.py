import datetime
import random
import itertools
fteam = [
    'Барселона','Ювентус','Реал Мадрид','Манчестер Юнайтед',
    'Арсенал','Спартак','Челси','Зенит',
    'ЦСКА','Ливерпуль','Локомотив','Лацио',
    'Луиз','ПСЖ','Шахтёр','Динамо'
    ]

random.shuffle(fteam)
fteam2 = []
for team in range(0,len(fteam),4):
    fteam2.append((fteam[team],fteam[team+1],fteam[team+2],fteam[team+3]))

dtm = [
    datetime.datetime(2020,9,16,22,45),
    datetime.datetime(2020,9,30,22,45),
    datetime.datetime(2020,10,14,22,45),
    datetime.datetime(2020,10,28,22,45),
    datetime.datetime(2020,11,11,22,45),
    datetime.datetime(2020,11,25,22,45),
    datetime.datetime(2020,12,9,22,45),
    datetime.datetime(2020,12,23,22,45)
    ]
c = 0
i = 0
t = 1
for teams in fteam2:
    i += 1
    print('{} группа: \n'.format(i), end='')
    for team in teams:
        print(team, end=' ')
        if t%2 == 0:
            print('\nРасписание матча: ',dtm[c].strftime('%m/%d/%Y, %H:%M')+'\n')
            c += 1
        else:
            print('- ', end='')
        t += 1


new_dict = {}
with open('mfc.csv', 'r', encoding='utf8') as f:
    for line in f:
        visitor = line[:-1].split(';')
        if new_dict.get(visitor[0]) is None:
            new_dict[visitor[0]] = {"08:00":[],\
                                    "09:00":[],\
                                    "10:00":[],\
                                    "11:00":[],\
                                    "12:00":[],\
                                    "13:00":[],\
                                    "14:00":[],\
                                    "15:00":[],\
                                    "16:00":[],\
                                    "17:00":[],\
                                    "counter": 0\
                                    }
        new_dict[visitor[0]][visitor[1]].append(int(visitor[2]))
        new_dict[visitor[0]]['counter'] += 1

for day in new_dict:
    for t in new_dict[day]:
        if t == 'counter':
            continue
        proc = len(new_dict[day][t]) / new_dict[day]['counter']
        str2console = day + ' ' + t + '#' * int(proc*20)
        print(str2console)

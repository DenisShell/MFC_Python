# день, час, время в очереди
dict_days = {'1': '2021-04-12',
            '2': '2021-04-13',
            '3': '2021-04-14',
            '4': '2021-04-15',
            '5': '2021-04-16'}
while True:
    data = input().strip()
    data_list = data.split(';')
    with open('mfc.csv', 'a', encoding='utf-8') as f:
        data_list[0]
        str2file = dict_days[data_list[0]] + ';' +\
                    data_list[1].rjust(2, '0') + ':00;' +\
                    data_list[2] + '\n'
        f.write(str2file)
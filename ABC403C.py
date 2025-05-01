N, M, Q = map(int, input().split())

XX = set()
YesNo = []

for i in range(Q):
    str_list = list(map(int, input().split()))
    if str_list[0] == 1 :
        XX.add((str_list[1],str_list[2]))
    elif str_list[0] == 2 :
        XX.add((str_list[1],'all'))
    elif str_list[0] == 3 :
        if (str_list[1],str_list[2]) in XX or (str_list[1],'all') in XX:
            YesNo.append('Yes')
        else:
            YesNo.append('No')

print('\n'.join(YesNo))

N =  int(input())
travel = [[0,0,0]] #出発点忘れずに

for _ in range(N):
    travel.append(list(map(int, input().split())))

Flag = True

for i in range(N):
    t_diff = travel[i+1][0] - travel[i][0]
    xy_diff = abs(travel[i+1][1] - travel[i][1]) + abs(travel[i+1][2] - travel[i][2])

    if xy_diff > t_diff or (t_diff - xy_diff) % 2 != 0:
        Flag = False
        break

if Flag:
    print("Yes")
else:
    print("No")
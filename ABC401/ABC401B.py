N = int(input())

Flag = False

count = 0

for i in range(N):
    word = input()
    if word == "login":
        Flag =True
    elif word == "logout":
        Flag = False
    elif word == "private" and Flag ==False:
        count +=1

print(count)
# string操作は難しい。

S=input()

while True:
    if S.endswith("dreamer"):
        S = S[:-7]
    elif S.endswith("eraser"):
        S = S[:-6]
    elif S.endswith("dream"):
        S = S[:-5]
    elif S.endswith("erase"):
        S = S[:-5]
    elif S =="":
        print("YES")
        exit()
    else:
        print("NO")
        exit()


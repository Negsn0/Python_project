A,B,C,D=map(int, input().split())

if A<C:
    print("No")
elif A>C:
    print("Yes")
elif A==C:
    if B<D:
        print("No")
    else:
        print("Yes")

exit()
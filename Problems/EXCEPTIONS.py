1 Exceptions
for i in range(int(input())):
    try:
        A,B=map(int,input().split())
        print(A//B)
    except Exception as Exception:
        print("Error Code:",Exception)
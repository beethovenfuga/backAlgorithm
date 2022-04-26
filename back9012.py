import sys
n = int(sys.stdin.readline())
answer = []
for i in range(n):
    check = 0
    case = sys.stdin.readline().strip()
    for j in case:
        if j =='(':
            check += 1
        elif j == ')':
            check-=1
        if check <0:
            break
    if check != 0:
        answer.append("NO")
    else:
        answer.append("YES")
for i in answer:
    print(i)

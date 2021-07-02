def solution(s, oper):
    operation = {}
    def get_count(s):
        count = {}
        for i in s:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        return count
    c = get_count(s)
    maxs = sorted(c.items(), key= lambda x: x[1])[-1][0]
    for i in oper:
        operation[i[0]] = i[1]
    i = 0 
    s = list(s)
    while i < len(s):
        if s[i] == maxs:
            i += 1
        else:
            if s[i] in operation:
                s[i] = operation[s[i]]
            else:
                return "No"
    val = get_count(s)
    if len(val) > 1:
        return "NO"
    return "YES"

s = input()
n = int(input())
operations = []
while n:
    operations.append(input().split())
    n -= 1
print(solution(s,operations))


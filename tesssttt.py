target = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def solve(S):
    # Write your code here
    count = 0
    res = ""
    for i in range(len(S)):
        if S[i] == target[0]:
            res = target.pop(-1)
            res = res + S[i]
            count = 1
        if len(target) > 0 and count == 1:
            res = res + S[i]
        if len(target) == 0:
            break
    return i
    

S = input()

out_ = solve(S)
print (out_)
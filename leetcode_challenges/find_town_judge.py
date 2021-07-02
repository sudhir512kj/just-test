def findJudge(n, trust):
        Map = {}
        for i in range(len(trust)):
            Map[trust[i][0]] = trust[i][1]
        for each in Map:
            if Map[each] not in Map.keys():
                return Map[each]
        return -1

print(findJudge(3,[[1,2],[2,3]]))
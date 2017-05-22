visit={ }
load={ }
N, M, V = map(int, input().split())

for i in range(M):
    fromN, toN = map(int, input().split())
    visit[fromN]=0
    visit[toN]=0
    if load.get(fromN)==None:
        load[fromN]=[ ]
    if load.get(toN)==None:
        load[toN]=[ ]
    load[fromN].append(toN)
    load[toN].append(fromN)

for a in load:
    load[a].sort()
    
way=[]
def DFS(startV):
    way.append(startV)
    visit[startV]=1 
    for toN in load.get(startV):
        if visit.get(toN) == 0:
            DFS(toN)

bfsWay=[]
def BFS(startV):#1
    flag=0
    for toN in load.get(startV):
        if visit.get(toN)==0:
            bfsWay.append(toN)
            visit[toN]=1
            flag=1
    if flag!=0:
        for nextN in bfsWay:
            BFS(nextN)

DFS(V)

for i in visit.keys():#visit초기화
    visit[i]=0
bfsWay.append(V)
visit[V] = 1
BFS(V)

result=''
for i in way:
    result+=str(i)+' '
print(result[:len(result)-1])
result=''
for i in bfsWay:
    result+=str(i)+' '
print(result[:len(result)-1])

#4.Design an application for a thermal power station and electrical lines that are connected among various power stations. 
# The costs of electrification involved appear as weights on the edges. Obtain the minimum possible connection among the thermal stations
# so that any two thermal stations can be linked with the minimum cost involved.


maxi=99999
n=int(input("Enter the number of vertices:  "))
selected=[False for i in range(n)]
parent=[0 for i in range(n)]

def find(i):
    while parent[i]!=i:
        i=parent[i]
    return i
def uni(i,j):
    x=find(i)
    y=find(j)
    parent[x]=y

def prims_mst(n,cost):
    n_edge=0
    selected[0]=True
    while n_edge<n-1:
        x=y=0
        minimum=maxi
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and cost[i][j]:
                        if  cost[i][j]<minimum:
                            minimum=cost[i][j]
                            x=i
                            y=j
        print(x,"->",y,"=",cost[x][y])
        selected[y]=True
        n_edge+=1

def kruskal_mst(n,cost):
    min_cost=0
    for i in range(n):
        parent[i]=i
    e_ctr=0
    while e_ctr<n-1:
        a=b=0
        mini=maxi
        for i in range(n):
            for j in range(n):
                if cost[i][j]<=mini and find(i)!=find(j):
                    mini=cost[i][j]
                    a=i
                    b=j
        uni(a,b)
        print("Edge ",e_ctr+1," (",a+1,",",b+1,") cost: ",mini)
        e_ctr+=1
        min_cost+=mini
        print("The minimum cost is ",min_cost)
cost=[[int(x) for x in input().split()] for j in range(n)] 
for i in range(n):
    for j in range(n):
        if cost[i][j]==0:
            cost[i][j]=maxi
print("Scheduling Tree using Prims algorithm : ")
prims_mst(n,cost)
print("Scheduling Tree using Kruskal algorithm : ")
kruskal_mst(n,cost)
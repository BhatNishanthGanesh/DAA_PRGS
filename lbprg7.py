# 7.Design an application for drilling an optimal printed circuit board. To drill two holes of different diameters consecutively, 
# the head of the machine has to move to a toolbox and change the drilling equipment. This is quite time consuming. Thus, it is clear
# that one has to choose some diameter, drill all holes of the same diameter, change the drill, drill the holes of the next diameter, etc. 
# Thus, this drilling problem has to minimize the travel time for the machine head. Find the optimal time to drill the circuit board.

class Sales:
    def __init__(self):
        self.cost_opt=0
        self.a=[[0 for _ in range(100)] for _ in range(100)]
        self.visit=[0]*100
    def mincost_opt(self,city,n):
        self.visit[city]=1
        print(city,"-->",end="\t")
        ncity=self.least_opt(city,n)
        if ncity==999:
            ncity=1
            print(ncity)
            self.cost_opt+=self.a[city][ncity]
            return
        self.mincost_opt(ncity,n)
    def least_opt(self,c,n):
        kmin=999
        nc=999
        min_val=999
        for i in range(1,n+1):
            if self.a[c][i]!=0 and self.visit[i]==0:
                if self.a[c][i]<min_val:
                    min_val=self.a[c][i]+self.a[i][1]
                    kmin=self.a[c][i]
                    nc=i
        if min_val!=999:
            self.cost_opt+=kmin
        return nc
def main():
    X=Sales()
    n=int(input("Enter the number of cities: "))
    print("Enter the cost matrix: ")
    for i in range(1,n+1):
        row=list(map(int,input().split()))
        for j in range(1,n+1):
            X.a[i][j]=row[j-1]
        X.visit[i]=0
    print("Entered cost matrix is: ")
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(X.a[i][j],end="\t")
        print()
    print("The optimal solution: ")
    print("The path is: ")
    X.mincost_opt(1,n)
    print("The minimum cost is : ",X.cost_opt)
    
    
if __name__=="__main__":
    main()
                
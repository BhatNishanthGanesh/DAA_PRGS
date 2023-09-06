# 6.The owner of a gourmet coffee shop wishes to mix a 10-pound bag of coffee  using various types of coffee beans in such a way 
# to produce the coffee blend at  the maximum cost. The weights of the objects in the problem correspond to the  quantity in pounds
# available of each type of coffee bean. The value of each  quantity of coffee beans is the total cost of that quantity in rupees.
# Apply the Knapsack algorithm to maximize the profit.


def knap_sack(wt,val,w,n):
    sol=[[0 for _ in range(w+1)] for _ in range(n+1)]
    select=[0]*(n+1)

    for i in range(n+1):
        for j in range(w+1):
            if j<wt[i]:
                sol[i][j]=sol[i-1][j]
            else:
                sol[i][j]=max(sol[i-1][j],sol[i-1][j-wt[i]]+val[i])
    print("The optimal solution is ",sol[n][w])
    i,j=n,w
    while i>0 and j>0:
        if sol[i][j]!=sol[i-1][j]:
            select[i]=1
            j-=wt[i]
        i-=1
        
    print("The path is: ")
    for i in range(n+1):
        if select[i]==1:
            print(i,end=" ")
    print()
    
def main():
    n=int(input("Enter the total number of items: "))
    wt=[0]*(n+1)
    val=[0]*(n+1)
    print("Enter the weight of ",n," items separated by spaces: ")
    wt_input=input().split()
    for i in range(1,n+1):
        wt[i]=int(wt_input[i-1])
    print("Enter the values of ",n," items separated by spaces: ")
    val_input=input().split()
    for i in range(1,n+1):
        val[i]=int(val_input[i-1])
    w=int(input("Enter the capacity of the bag: "))
    knap_sack(wt,val,w,n)

if __name__=="__main__":
    main()
    
#2.Design and implement an application that considers the problem of scheduling n jobs of known durations t1, t2,...,tn for execution 
# by a single processor. The jobs can be executed in any order, one job at a time. Find and display the  schedule that minimizes the 
# total time spent by all the jobs in the system by maximizing the profit.

class Job:
    def __init__(self,taskId,deadline,profit):
        self.taskId=taskId
        self.deadline=deadline
        self.profit=profit
def ScheduleJobs(jobs,T):
    profit=0
    slots=[-1]*T
    jobs.sort(key=lambda x:x.profit ,reverse=True)
    for job in jobs:
        for j in reversed(range(job.deadline)):
            if j<T and slots[j]==-1:
                slots[j]=job.taskId
                profit+=job.profit
                break
    print("The sequence of jobs are: ",list(filter(lambda x:x!=-1,slots)))
    print("The optimal profit is ",profit)

if __name__=="__main__":
    jobs=[]
    n=int(input("Enter the total number of jobs: "))
    for i in range(n):
        taskId=int(input(f"Enter the taskId of job {i+1}: "))
        deadline=int(input(f"Enter the deadline of job {i+1}: "))
        profit=int(input(f"Enter the profit of job {i+1}: "))
        jobs.append(Job(taskId,deadline,profit))
    T=int(input("Enter the minimum time slots: "))
    ScheduleJobs(jobs,T)
    
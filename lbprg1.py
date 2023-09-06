# 1.Design an application to create a list of  TV channels(minimum 10) that includes the numbers of viewers and viewing time .
# Rate the channels based on the  number of viewers (1 High - 6 low). Plot graphs to analyze the running times of  different sorting algorithms.



import matplotlib.pyplot as plt
import time
import random

class TVChannel:
    def __init__(self,name,viewers,viewing_time):
        self.name=name
        self.viewers=viewers
        self.viewing_time=viewing_time
def create_channel(i):
    name=f"channel {i}"
    viewers=random.randint(500,2000000)
    viewing_time=random.randint(30,180)
    return TVChannel(name,viewers,viewing_time)

def rateChannel(Channel):
    if Channel.viewers>=1500000:
        return "Rank1-Excellent"
    elif Channel.viewers>=1000000:
        return "Rank2-Great"
    elif Channel.viewers>=500000:
        return "Rank3-Good"
    elif Channel.viewers>=300000:
        return "Rank4-Average"
    elif Channel.viewers>=100000:
        return "Rank5-Poor"
    else:
        return "Rank6-Just Shut down"
    
def plot_sorting_algorithm():
    sorting_agorithms=["Quick sort","Insertion sort","Selection sort","Merge sort","Bubble sort"]
    running_times=[]
    
    for algorithm in sorting_agorithms:
        data=[random.randint(1,1000) for _ in range(1000)]
        start_time=time.time()
        
        if algorithm=="Quick sort":
            quick_sort(data)
        elif algorithm=="Insertion sort":
            insertion_sort(data)
        elif algorithm=="Selection sort":
            selection_sort(data)
        elif algorithm=="Merge sort":
            merge_sort(data)
        elif algorithm=="Bubble sort":
            Bubble_sort(data)
        
        end_time=time.time()
        running_time=end_time-start_time
        running_times.append(running_time)
    
    plt.bar(sorting_agorithms,running_times)
    plt.xlabel("Sorting algorithms..")
    plt.ylabel("Running times")
    plt.title("Sorting algorithm in running time")
    plt.show()

def Bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
        
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
        
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr[0]
        smaller=[x for x in arr[1:] if x<=pivot]
        greater=[x for x in arr[1:] if x>pivot]
        return quick_sort(smaller)+[pivot]+quick_sort(greater)
    return quick_sort(smaller)+[pivot]+quick_sort(greater)
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        mid=len(arr)//2
        left_half=arr[:mid]
        right_half=arr[mid:]
        left_half=merge_sort(left_half)
        right_half=merge_sort(right_half)
        return merge(left_half,right_half)
def merge(left,right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while i<len(left):
        result.append(left[i])
        i+=1
    while j<len(right):
        result.append(right[j])
        j+=1
    return result

def main():
    channels=[]
    while True:
        print("\n TV Channel APP")
        print("1.Create 10 channels")
        print("2.Rate channels..")
        print("3.Plot sorting algorithms")
        print("4.Exit")
        choice=int(input("Enter the choice: "))
        if choice==1:
            for i in range(0,10):
                channel=create_channel(i+1)
                channels.append(channel)
            print("Channels created successfully...")
        elif choice==2:
            for channel in channels:
                rate_channel=rateChannel(channel)
                print(f"{channel.name}: \n {channel.viewers} viewiers {channel.viewing_time} hours {rate_channel}")
        elif choice==3:
            plot_sorting_algorithm()
        elif choice==4:
            print("Exiting the app...")
            break
        else:
            print("Invalid choice..")
            
if __name__=="__main__":
    main()
            
# 8.Design an application for the university to schedule an exam. Given a list of different subjects and students who are enrolled
# in many subjects, many subjects would have common students of the same batch, some backlogged students, etc.
# Find the solution to the following:
# a.Obtain the schedule for the exam so that no two exams with a common student are scheduled at the same time.
# b.How many minimum time slots are needed to schedule all exams?



from collections import defaultdict

class Graph:
    def __init__(self,subjects):
        self.subjects=subjects
        self.graph=defaultdict(list)
    def add_edge(self,subject1,subject2):
        self.graph[subject1].append(subject2)
        self.graph[subject2].append(subject1)
    def graph_coloring(self):
        color_map={}
        available_color=set(range(1,len(self.subjects)+1))
        for subject in self.subjects:
            used_colors=set()
            for neighbour in self.graph[subject]:
                if neighbour in color_map:
                    used_colors.add(color_map[neighbour])
            available_color=available_color-used_colors
            if available_color:
                color_map[subject]=min(available_color)
            else:
                color_map[subject]=len(available_color)+1
                used_colors.add(color_map[subject])
        return color_map
    def get_minimum_time_slots(self):
        color_map=self.graph_coloring()
        return max(color_map.values())
        
def main():
    num_subjects=int(input("Enter the number of subjects: "))
    Subjects=[]
    students={}
    for i in range(num_subjects):
        subject=input(f"Enter the subject {i+1}: ")
        Subjects.append(subject)
        num_students=int(input("Enter the number of students: "))
        for j in range(num_students):
            studentlist=[]
            student=input(f" Enter the student {j+1} for {subject}: ")
            studentlist.append(student)
        students[subject]=studentlist
    graph=Graph(Subjects)
    num_edges=int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        edges=input("Edge (Subject1 Subject2):").split()
        graph.add_edge(edges[0],edges[1])
    minimum_time_slots=graph.get_minimum_time_slots()
    print(f"The minimum time slot is {minimum_time_slots}")
if __name__=="__main__":
    main()
    
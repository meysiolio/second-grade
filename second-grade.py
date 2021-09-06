if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        
    #sorted_students = sorted(students,key=lambda x:x[1])
    
    min_index = [i for i,j in enumerate(students) \
     if j[1] == min(students,key=lambda x:x[1])[1]]
     
    students = sorted(students,key=lambda x:x[1])
     
    for k in min_index:
        del students[0]
    
    min_score = min(students,key=lambda x:x[1])[1]
    min_names_index = [i for i,j in enumerate(students) if j[1] == min_score]
    min_names = []
    
    for t in min_names_index:
        min_names.append(students[t][0])
        
    for s in sorted(min_names):
        print(s)

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

listofStudentMarks = list(student_marks[query_name])
averageofMarks = sum(listofStudentMarks) / len(listofStudentMarks)
print("%.2f" % averageofMarks)

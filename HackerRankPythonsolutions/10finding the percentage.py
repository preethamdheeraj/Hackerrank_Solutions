if __name__ == "__main__":
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

listof_student_marks = list(student_marks[query_name])
averageofMarks = sum(listof_student_marks) / len(listof_student_marks)
print("%.2f" % averageofMarks)

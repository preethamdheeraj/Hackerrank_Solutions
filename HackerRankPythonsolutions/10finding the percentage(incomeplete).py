if __name__ == "__main__":
    n = int(input("the number of student records:"))
    student_marks = {}
    for _ in range(n):  # the _ is a temp variable
        name, * \
            line = input(
                "enter names of students and marks of students").split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("enter the name of the student to find average")

print(name)
print(line)

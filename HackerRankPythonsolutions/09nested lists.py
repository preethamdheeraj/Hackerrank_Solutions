students = []
second_lowest_names = []
numberOfStudents = int(input())

for i in range(numberOfStudents):
    name = input()
    score = float(input())
    students.append([name, score])

second_lowest_score = sorted(list(set([score for name, score in students])))[1]
for name, score in students:
    if score == second_lowest_score:
        second_lowest_names.append(name)
second_lowest_names.sort()

for name in second_lowest_names:
    print(name)

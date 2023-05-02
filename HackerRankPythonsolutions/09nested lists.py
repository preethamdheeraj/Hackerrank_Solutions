numberOfStudents = int(input())
names = []
scores = []
for i in range(numberOfStudents):
    names.append(input())
    scores.append(float(input()))

sorted_scores = []
for score in scores:
    sorted_scores.append(score)
sorted_scores.sort()
second_smallest = 0
for i in range(1, len(sorted_scores)):
    if sorted_scores[i] != sorted_scores[i - 1]:
        second_smallest = sorted_scores[i]
        break

sorted_names = []
for i in range(len(scores)):
    if scores[i] == second_smallest:
        sorted_names.append(names[i])
sorted_names.sort()
for names in sorted_names:
    print(names)

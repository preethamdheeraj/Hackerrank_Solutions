number = int(input())
scores = list(map(int, input().split()))

max_scores = max(scores)
scores = [score for score in scores if score != max_scores]

if not scores:
    runner_up_score = None
else:
    runner_up_score = max(scores)

print(runner_up_score)

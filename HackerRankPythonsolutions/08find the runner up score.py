number = int(input())
scores = list(map(int, input().split()))

maxScores = max(scores)
scores = [score for score in scores if score != maxScores]

if not scores:
    runner_up_score = None
else:
    runner_up_score = max(scores)

print(runner_up_score)

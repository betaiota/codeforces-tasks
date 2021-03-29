n, k = map(int, input().split())
participants = [int(a) for a in input().split()]
count = 0
for grade in participants:
    if grade >= participants[k-1] and grade > 0:
        count += 1
print(count)
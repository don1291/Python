score1 = float(input("Enter the score:  "))
score2 = float(input("Enter the second score:  "))
score3 = float(input("Enter the third score:  "))

total = 0

if score1 > score2 or score1 > score3:
    total += score1
if score2 > score1 or score2 > score3:
    total += score2
else:
    score3 > score1 or score3 > score2
    total += score3


avg = total / 2

print("Avg: " + format(avg,",.2f"))

year = int(input())

while True:
    year += 1
    happy_year = set()
    for i in range(len(str(year))):
        happy_year.add(str(year)[i])

    if len(happy_year) == len(str(year)):
        condition = False
        break

print(happy_year)





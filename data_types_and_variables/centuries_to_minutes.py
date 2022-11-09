century = int(input())

year = 1
years = 100 * century
days = years * 365.2422
hours = int(days) * 24
minutes = hours * 60


print(f"{century} centuries = {years} years = {int(days)} days = {(hours)} hours = {minutes} minutes")

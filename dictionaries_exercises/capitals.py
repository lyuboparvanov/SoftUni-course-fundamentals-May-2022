countries = input().split(', ')
capitals = input().split(', ')
dictt = dict(zip(countries,capitals))
# dict = {countries[index]: capitals[index] for index in range(len(capitals))}
# for key, value in dict.items():
#     print(f"{key} -> {value}")
print(dictt)
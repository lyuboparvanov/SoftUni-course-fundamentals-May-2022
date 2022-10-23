from math import ceil

number_of_people = int(input())
capacity = int(input())
if capacity > 0:
    number_of_courses = ceil(number_of_people/capacity)
    print(number_of_courses)
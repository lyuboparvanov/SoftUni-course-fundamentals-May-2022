def loading_bar(percentage):
    if percentage == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    return f"{percentage}% [{'%' * (percentage // 10)}{'.' * abs((percentage - 100)//10)}]\nStill loading..."




number = int(input())
print(loading_bar(number))
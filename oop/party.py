class Party:
    def __init__(self):
        self.people = []

    def people_invited(self, name):
        self.name = name
        self.people.append(name)

    def who_is_going(self):
        return ', '.join(self.people)

    def number_of_guests(self):
        return len(self.people)

party = Party()
while True:
    command = input()
    if command == 'End':
        break

    name = command
    party.people_invited(name)

print(f"Going: {party.who_is_going()}")
print(f"Total: {party.number_of_guests()}")

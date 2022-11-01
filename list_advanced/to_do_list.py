
note_book = []
while True:
    notes = input()
    if notes == 'End':
        break

    current_note = notes.split('-')
    priority = int(current_note[0])
    type_of_note = current_note[1]
    note_book.append((priority, type_of_note))
result = [n[1] for n in sorted(note_book)]
print(result)
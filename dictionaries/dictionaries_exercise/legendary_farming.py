
legendary_items = {'shards': 0, 'fragments': 0, 'motes': 0}
junk_items = {}
obtained = False
while True:
    if obtained:
        break
    command = input().split()
    for i in range(0, len(command), 2):
        qty = command[i]
        item = command[i+1].lower()


        if item == 'shards':
            legendary_items[item] += int(qty)
            if legendary_items[item] >= 250:
                legendary_items[item] -= 250
                obtained = True
                print(f"Shadowmourne obtained!")
                break

        elif item == 'fragments':
            legendary_items[item] += int(qty)
            if legendary_items[item] >= 250:
                legendary_items[item] -= 250
                obtained = True
                print(f"Valanyr obtained!")
                break

        elif item == 'motes':
            legendary_items[item] += int(qty)
            if legendary_items[item] >= 250:
                legendary_items[item] -= 250
                obtained = True
                print(f"Dragonwrath obtained!")
                break

        else:
            if item not in junk_items:
                junk_items[item] = int(qty)
            else:
                junk_items[item] += int(qty)


for k,v in legendary_items.items():
    print(f"{k}: {v}")

for key,value in junk_items.items():
    print(f"{key}: {value}")
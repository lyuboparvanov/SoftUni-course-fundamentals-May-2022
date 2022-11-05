class Inventory:
    def __init__(self, __capacity: int):
        self.capacity = __capacity
        self.added_items = 0
        self.items = []

    def add_item(self, item: str):
        if self.added_items < self.capacity :
            self.added_items += 1
            self.items.append(item)
        else:
            return f"not enough room in the inventory"

    def get_capacity(self):
        return self.capacity


    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.capacity - self.added_items}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)

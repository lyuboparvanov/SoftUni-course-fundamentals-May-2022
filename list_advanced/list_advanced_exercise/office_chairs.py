def chairs_checker(rooms):
    total_free_chairs = 0
    needed_chairs = 0

    for current_room in range(1, rooms + 1):
        num_of_chairs, visitors = input().split()
        needed_chairs_per_floor = len(num_of_chairs) - int(visitors)
        if needed_chairs_per_floor < 0:
            needed_chairs += abs(needed_chairs_per_floor)
            print(f"{abs(needed_chairs_per_floor)} more chairs needed in room {current_room}")
        else:
            total_free_chairs += needed_chairs_per_floor
    if total_free_chairs >= needed_chairs:
        print(f"Game On, {total_free_chairs} free chairs left")



number_of_rooms = int(input())
chairs_checker(number_of_rooms)

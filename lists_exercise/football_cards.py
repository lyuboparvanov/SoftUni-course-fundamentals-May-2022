all_cards = input().split()
given_cards = []
game_terminated = False
team_a = 11
team_b = 11
for current_card in all_cards:
    if current_card not in given_cards:
        given_cards.append(current_card)
        if current_card[0] == 'A':
            team_a -= 1
        elif current_card[0] == 'B':
            team_b -= 1

        if team_a < 7 or team_b < 7:
            game_terminated = True
            break
print(f"Team A - {team_a}; Team B - {team_b}")
if game_terminated:
    print(f"Game was terminated")